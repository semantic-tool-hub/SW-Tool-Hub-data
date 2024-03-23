Semantic Toolhub Data Repository
================================

Welcome to the Semantic Toolhub GitHub repository! We aim to find the right semantic web tools for the usage scenario. The tool is available at <https://semantic-tool-hub.github.io/>. This repository stores the underlying data (as an export of WikiData) and describes how to edit and add software.

It also is the data basis for the paper **Semantic Tool Hub: Towards A Sustainable Community-Driven Documentation of Semantic Web Tools** by Achim Reiz, Fajar J. Ekaputra, and Nandana Mihindukulasooriya. The paper is currently under review.

## TLDR
The Semantic Toolhub is a community-driven repository to help knowledge engineers and developers find and document the right semantic web tools. It uses a taxonomy to describe the tool's capabilities and allows easy contribution through a [form-based](https://docs.google.com/forms/d/e/1FAIpQLSfDoLRg7J-9hM0pvNgFsfcZ9EEkgoXROWg_TPsW42oUcNF2kw/viewform) approach or by editing Wikidata.

Why Bother?
-----------

The semantic web community has developed numerous tools and software, which poses a challenge for those entering the field to identify the right tools for their use case. Many software tools are no longer maintained; searching through publications and source repositories can take time and effort. Our proposed workflow and Wikidata-based toolkit aim to support knowledge engineers and developers in finding and documenting the right tools. By categorizing existing tools into a pre-defined taxonomy and integrating them with GitHub metadata, we have created a condensed information database now integrated into Wikidata for further use. With Wikidata as the underlying data storage, we invite the community to add and edit further information to create a community-driven repository.

The Taxonomy
============

The taxonomy is the basis for describing the tool's capabilities. The taxonomy is structured using WikiDatas SubClassOf hierarchy ([P279](https://www.wikidata.org/wiki/Property:P279)) and itself a subclass of software engineering ([Q638608](https://www.wikidata.org/wiki/Q638608)).

![grafik](https://github.com/semantic-tool-hub/SW-Tool-Hub-data/assets/12608619/4b5f9dd7-6a7f-4cf3-a760-5b890aae250f)

It is built on the [OntoCommons Report D4.3](https://ontocommons.eu/deliverables) and the [semantic web lifecycle](https://doi.org/10.1007/978-3-031-14343-4_33) by Breit et al.

The Taxonomy Development Process
--------------------------------

We developed the taxonomy in two phases. In the first phase, we attempted to categorize the tools deductively based on a public report (OntoCommonsCitation) and the Semantic Web Software Lifecycle by Breit et al. OntoCommonts divides the components of an ontology ecosystem into 19 categories, such as "Drafting," "Query Engine," or "Test specification." Breit et al. differentiate between two main categories, "development" and "operation.", having nine knowledge graph tasks.

However, we discovered that the categorization in the OntoCommons report was heavily focused on the ontology and only accounted for part of the graph perspective. For instance, the report's categorization did not distinguish between validation (such as SHACL validation) and evaluation (such as calculating ontology metrics). Breit et al.'s SW lifecycle categories were rather broad and did not sufficiently capture the intricacies of the software tools. Thus, we inductively refined the taxonomy and extended it along the data acquisition process in the second iteration. We frequently discussed inclusion criteria and examples for newly created categories and adjusted the data accordingly. The detailed criteria are presented in the table below.


| **Category** | Inclusion Criteria | *Examples* |
| --- | --- | --- |
| kg learning | Tools that help people learn SW technologies | *SHACL-Playground* |
| kg requirement elicitation | Tools generating or collecting competency questions including document templates | *ORSD document* |
| semantic artifact catalog | Managing a collection of KGs or ontologies | *Linked Open Vocabularies* |
| visual ontology editing | Ontology modeling with a visual editor | *Chowlk* |
| ontology visualization | Tools to automatically create ontology graph visualizations | *VOWL*, *OntoViz* |
| Numerical Analysis | Calculating ontology metrics | *NEOntometrics* |
| Ontology model validation | Checking for syntactical correctness and pitfalls | *OOPS!* |
| virtual knowledge graph | Tools allowing the connection of virtual knowledge graphs (thus, a triple interface for (mostly relational) data. | *Ontop* |
| kg materialization | Tools that allow mass ingestion of data | *GraphDB* |
| Schema-based kg validation | Tools using SHACL, SHEx | *PyShacl*, *Apache Jena* |
| heuristic-based kg validation | Tool using subsymbolic approaches to detect incorrect data | *F-UJI* |
| Pure Triplestore | Databases that only provide RDF storage | *GraphDB*, *ForestDB* |
| Multi-Model Database | Databases allowing the usage of various storage paradigm | *Virtuosog* |
| SPARQL Querying | Tools with a standardized SPARQL interface for querying | *Apache Jena* |
| Federated KG Querying | Tools for querying multiple data sources | *Cost-Fed* |
| Sparql Query Building | Tools for low-code query generation | *Wikidata Query Builder* |
| Sparql Query Result Visualization | Visualization of query results, e.g., graphs, diagrams | *YASGUI* |
| rdf streams | Tools for semantifying streaming data or querying Streaming Data using SPARQL | *Streaming Sparql* |
| standalone kg reasoning | Standalone Reasoning Tools | *HermiT*, *Pellet* |
| semantic web software with reasoning | 'Software that provides reasoning capabilities, without it being the main functionality | *Protégé* |
| kg API Engine with reasoner | API Frameworks with reasoning capabilities | *RDF4J* |
| reasoning in a database | Databases with reasoning functionality | *RDFox* |
| kg logic solving | Software for Proof management tools and Static Analysis | *HETS* |
| ontology publication | creation of ontology schema documentation | *Widoco* |
| KG Browser | kg data frontend | *wikidata*, *sampo* |
| kg issue tracking | Tracking user requests and issues | *github* |
| Ontology versioning management | Managing the ontology throughout its life | *Topbraid EDG* |
| kg data versioning | versioning of the instance data | *Quitstore* |

Contributing to the Taxonomy
----------------------------

It is important to note that the taxonomy is not a static document but rather a living framework that can be further edited and refined as needed. As new software tools and technologies emerge, creating new categories or refining existing ones may become necessary to ensure that the taxonomy remains relevant and valuable. We encourage users to contribute to the taxonomy by providing feedback and suggestions for improvement. By working together, we can comprehensively and accurately categorize the software tools and technologies used in the semantic web ecosystem.

The (Semantic Web Tool) Data
============================

One central goal of the semantic tool hub initiative is to make contributions easy and build a community-driven data elicitation approach. So, data editing and gathering are at the core of the semantic tool hub.

Adding New Tools Using a Form-Based Approach
--------------------------------------------

The easiest way to add new tools and data is to use a [form](https://docs.google.com/forms/d/e/1FAIpQLSfDoLRg7J-9hM0pvNgFsfcZ9EEkgoXROWg_TPsW42oUcNF2kw/viewform). Here, filing a new tool should take at most 5 minutes! We take it from here and create a new batch of wiki data entries. (Not in an instant, though). Please categorize your tool using the taxonomy shown above.

Editing Wikidata 
-----------------

Editing with Wikidata's frontend is a simple and straightforward process that allows altering and adding data in a high level of granularity. No authentication or authorization is needed to contribute, but having an account is highly recommended. You don't need a deep understanding of the data architecture to make changes, as the front end provides an easy way to edit and create entries.

Before creating new elements, it is obligatory to perform a thorough search to verify that the tool in question does not already exist. If so, you can add new linkages to the existing resource. If you want to add a new tool to the Semantic Toolhub, click "Create a new Item" in the left navigation bar. After providing a brief description and label, the axioms are added manually.

New axioms can be created using the *add statement* button, and new values to an existing property can be introduced using the *add value* button. It's best to orient yourself to existing examples of semantic web tools, like Levelgraph ([Q124653376](https://www.wikidata.org/wiki/Q124653376)). The table below gives an overview of the various data used by the semantic tool hub interface. However, feel free to add further categorizations and linkages.

| Property                                  | Object                                                                                                                                                      |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| instance of [(P31)](https://www.wikidata.org/wiki/Property:P31)                         | *fix:* semantic web software [(Q124653107)](https://www.wikidata.org/wiki/Q124653107) |
| has use [(P366)](https://www.wikidata.org/wiki/Property:P366)             | *pot. list* taxonomy elements (cf. Taxonomy)                                                                                                       |
| genre [(P136)](https://www.wikidata.org/wiki/Property:P136)               | *one of:* [API [(Q165194)](https://www.wikidata.org/wiki/Q165194), GUI [(Q782543)](https://www.wikidata.org/wiki/Q782543), CLI [(Q189053)](https://www.wikidata.org/wiki/Q189053)]                  |
| programmed in [(P277)](https://www.wikidata.org/wiki/Property:P277)       | *optional:* programming language, e.g.: JavaScript [(Q2005)](https://www.wikidata.org/wiki/Q2005)                                                                                   |
| copyright license [(P275)](https://www.wikidata.org/wiki/Property:P275)   | select license, e.g., MIT [(Q334661)](https://www.wikidata.org/wiki/Q334661)                                                                                                            |
| copyright status [(P6216)](https://www.wikidata.org/wiki/Property:P6216)  | *fix:* copyrighted [(Q50423863)](https://www.wikidata.org/wiki/Q50423863)                                                                                                                  |
| described by source [(P1343)](https://www.wikidata.org/wiki/Property:P1343)| *pot. list:* e.g., awesome RDF [(Q124650984)](https://www.wikidata.org/wiki/Q124650984)                                                                                                       |
| last update [(P5017)](https://www.wikidata.org/wiki/Property:P5017)        | *date:* last update on Code or software (e.g., from Git)                                                                                                   |
| source code repository URL [(P1324)](https://www.wikidata.org/wiki/Property:P1324) | *optional, url:* Source Code URL <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*has qualifiers:* <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version control system [(P8423)](https://www.wikidata.org/wiki/Property:P8423): *fix:* Git [(Q186055)](https://www.wikidata.org/wiki/Q186055) <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;web interface software [(P10627)](https://www.wikidata.org/wiki/Property:P10627): e.g., GitHub [(Q364)](https://www.wikidata.org/wiki/Q364) |

We hope you discover the Semantic Toolhub as a valuable resource and eagerly anticipate your contributions!
