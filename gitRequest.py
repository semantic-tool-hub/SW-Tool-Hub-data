import requests
import json
import datetime
import dotenv
import os

tool_data_array = []
with open("tools_from_wikidata.jsonl", 'r') as file:
    for line in file:
        data = json.loads(line)
        # Process each line of the JSONL file 
        # Example: Print the line
        tool_data_array.append(data)

dotenv.load_dotenv(".env")
git_access_token = os.getenv("github_token")
header = {"Authorization": f"BEARER {git_access_token}"}
resp = requests.get("https://api.github.com/rate_limit", headers=header)
rate = json.loads(resp.content)["resources"]["core"]
print(f"rate_limit: {rate["remaining"]}/{rate["limit"]}")


def create_git_api(git_repo): return "https://api.github.com/repos/" + \
    str.join("/", git_repo.split("/")[-2:])


for tool_data in tool_data_array:
    if "source_repos" in tool_data and "github" in tool_data["source_repos"]:
        resp = requests.get(create_git_api(
            tool_data["source_repos"]), headers=header)
        if resp.status_code == 200:
            git_metadata = json.loads(resp.content)
            tool_data["last_entry_date"] = str(datetime.datetime.strptime(
                git_metadata["pushed_at"], '%Y-%m-%dT%H:%M:%SZ'))
            tool_data["programming_language"] = git_metadata["language"]
            tool_data["description"] = git_metadata["description"]
            if git_metadata["license"] != None:
                tool_data["license"] = git_metadata["license"]["key"]

with open("tools_from_wikidata_w_gitupdate.jsonl", 'w') as file:
    file.write(str.join("\n", [json.dumps(e) for e in tool_data_array]))