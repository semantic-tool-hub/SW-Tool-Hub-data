
from SPARQLWrapper import SPARQLWrapper, JSON, CSV
import pandas as pd
import datetime

# wikidata endpoint
endpoint_url = "https://query.wikidata.org/sparql"

# SPARQL query
tools_query = """
SELECT DISTINCT ?tool ?toolLabel ?description ?genreLabel 
                (group_concat(DISTINCT ?website_raw; SEPARATOR="; ") as ?website)
                (group_concat(DISTINCT ?classLabel; SEPARATOR="; ") as ?classification)
                (group_concat(DISTINCT ?licenseELabel; SEPARATOR="; ") as ?license) 
                (group_concat(DISTINCT ?programmingLangLabel; SEPARATOR="; ") as ?programming_language) 
                (group_concat(DISTINCT ?sourceRepo; SEPARATOR="; ") as ?source_repos) 
                (MAX(?last_update ) AS ?update)
                (group_concat(DISTINCT ?sourceLabel; SEPARATOR="; ") as ?sources)
               (group_concat(DISTINCT ?beforesubClassLabel; SEPARATOR="; ") as ?s) 
WHERE {
  ?class wdt:P279 wd:Q124614077.
  ?subClasses (wdt:P279*) ?class.
  ?tool wdt:P366 ?subClasses ;
        wdt:P136 ?genre ;
        OPTIONAL { ?tool wdt:P275 ?licenseE . ?licenseE rdfs:label ?licenseELabel . FILTER(lang(?licenseELabel) = "en") }
        OPTIONAL { ?tool schema:description? ?description . FILTER(lang(?description) = "en") }
        OPTIONAL { ?tool wdt:P5017 ?last_update }
        OPTIONAL { ?tool wdt:P277 ?programmingLang . ?programmingLang rdfs:label ?programmingLangLabel . FILTER(lang(?programmingLangLabel) = "en")}
        OPTIONAL { ?tool wdt:P1324 ?sourceRepo }
        OPTIONAL { ?tool wdt:P856 ?website_raw}
        OPTIONAL { ?tool wdt:P1343 ?source . ?source rdfs:label ?sourceLabel .   FILTER(lang(?sourceLabel) = "en")  }  
                   
  ?subClasses rdfs:label ?classLabel .
  FILTER(lang(?classLabel) = "en")              
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
GROUP BY ?tool ?toolLabel ?description ?genreLabel ?update 
ORDER BY ?tool
"""

def get_tools_data(endpoint_url, tools_query):
  # Create a SPARQLWrapper instance
  sparql = SPARQLWrapper(endpoint_url)

  # Set the query and response format
  sparql.setQuery(tools_query)
  sparql.setReturnFormat(JSON)

  # Execute the query and get the results
  results = sparql.query().convert()

  df = pd.json_normalize(results["results"]["bindings"]).filter(like="value")
  df = df.rename(columns= lambda x: str(x)[:-6])
  df['update'] = pd.to_datetime(df['update'])
  df['update'] = df['update'].dt.strftime('%Y-%m-%d %H:%M:%S')
  df["tool"] = df["tool"].replace(r"http://www.wikidata.org/entity/", "", regex=True)
  df.genreLabel= df.genreLabel.map({"application programming interface": "API", "command-line interface": "CLI", "graphical user interface": "GUI"})
  df.classification = df.classification.map(lambda x:x.replace("knowledge graph", "KG"))
  #df = df.assign(open_source= df.licenseLabel != "proprietary license")
  #date_range = pd.date_range(start=df['update'].min(), end=datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=365), freq='Y')
  df = df.rename(columns={
    "tool": "wikidata_id",
    "toolLabel": "tool_name",
    "genreLabel": "tool_type",
    "sources": "information_source",
    "update" : "last_entry_date"
  })

  return  df

if __name__ == "__main__":
  df = get_tools_data(endpoint_url, tools_query)
  with open("tools_from_wikidata.jsonl", "w") as out_file:
    for _, row in df.iterrows():
        row_json = row.to_json()
        out_file.write(f"{row_json}\n")
