---
name: Semantic ToolHub Change
about: Template for proposing changes to the Semantic ToolHub
title: Semantic Tool Hub Change Request
labels: enhancement
assignees: ''

---

Thank you for contributing to the semantic toolhub. Using this template, you can propose changes to the database.

Just so you know, using this template is optional; you can also go directly through the Wikidata UI or make a pull request for changes in the `jsonl`-data collection. For more information, visit the readme on the repository's main page.

# Semantic ToolHub Integration Form.
If you want to propose changes for an existing wikidata item, please name the wikidata ID and only fill out the things you want to be changed. Remove the sample data.

## WikiData-ID
e.g.: https://www.wikidata.org/wiki/Q124653457 - This **must** be declared for items that shall be changed. Also, make sure that the tools are not already created in WikiData

Use either the [semantic toolhub directly](https://semantic-tool-hub.github.io/) or http://wikidata.org to find potentially already existing items.

## GitHub-Link
Please state the Git-Hub Link to a source. 

From the Git link, we will derive
- The License (No License = Proprietary Software!)
- Last Update
- Programming Language
- Description (if available)

## Description (If not in git)
State a Description (if not it is not described in GitHub

## Application Type
Is your application usable through a (Select only one!)
- Command Line Application **CLI**
- Graphical User Interface **GUI**
- Application Programming Interface **API**

## Official Website
If the project has an official website, let us known here

## Paper URL
Have you written a Paper about the code? Past the URL here.

## Functionalities
This is (probably) the most important information. Please state the capabilities of the tool. Use the exact wording as providing by the taxonomy on the Main-Page of the Repo.
- E.g..heuristic based knowledge graph validation
- E.g., triplestore
