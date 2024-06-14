import datetime
import logging
import dotenv
import os
import json
import wikibaseintegrator

import wikibaseintegrator.datatypes
import wikibaseintegrator.models
import wikibaseintegrator.wbi_enums
import wikibaseintegrator.wbi_helpers
import wikibaseintegrator.wbi_login
from wikibaseintegrator.wbi_config import config as wbi_config


logging.basicConfig(level=logging.INFO)

dotenv.load_dotenv(".env")
wikidata_translation_dict: dict
with open("jsonl_wikidata_translation.json", "r") as file:
    wikidata_translation_dict = json.load(file)

jsonl_tooldata_array = []
with open("tools_from_wikidata_w_gitupdate.jsonl", 'r') as file:
    for jsonl_tooldata_line in file:
        data = json.loads(jsonl_tooldata_line)
        # Process each line of the JSONL file
        # Example: Print the line
        jsonl_tooldata_array.append(data)


def create_claim(wikidata_property_id: str, wikidata_object_id: str) -> wikibaseintegrator.models.Claim:
    """
    Create a claim for a Wikibase item.

    Args:
        wikidata_property_id (str): The property ID for the claim.
        wikidata_object_id (str): The value for the claim.

    Returns:
        wikibaseintegrator.models.Claim: The created claim object.

    Examples:
        >>> create_claim("P856", "https://example.com")
        <wikibaseintegrator.models.Claim object at 0x7f9a3a2b3a90>
    """
    if wikidata_property_id == "P856":
        return wikibaseintegrator.datatypes.URL(prop_nr=wikidata_property_id, value=wikidata_object_id)
    elif wikidata_property_id in ["P366", "P136", "P275", "P277", "P6216"]:
        return wikibaseintegrator.datatypes.Item(prop_nr=wikidata_property_id, value=wikidata_object_id)
    elif wikidata_property_id == "P5017":
        return wikibaseintegrator.datatypes.Time(prop_nr=wikidata_property_id, time=datetime.datetime.fromisoformat(
            wikidata_object_id).strftime("+%Y-%m-%dT00:00:00Z"))


wikidata_user = os.getenv("wikidata_user")
wikidata_pw = os.getenv("wikidata_pw")
wbi_config['USER_AGENT'] = f'semantic_toolhub (https://www.wikidata.org/wiki/User:{wikidata_user})'

wikidata_login = wikibaseintegrator.wbi_login.Clientlogin(
    user=wikidata_user, password=wikidata_pw)
wiki = wikibaseintegrator.WikibaseIntegrator(
    login=wikidata_login, is_bot=False)
for jsonl_tooldata_line in jsonl_tooldata_array:
    item = wiki.item.get(entity_id=jsonl_tooldata_line["wikidata_id"])
    update_claims = []
    changelog = []

    for jsonl_key, jsonl_value in jsonl_tooldata_line.items():
        if jsonl_value is None or jsonl_value == "":
            continue
        elif jsonl_key == "wikidata_id":
            continue
        elif jsonl_key == "tool_name":
            if item.labels.get("en").value != jsonl_value:
                item.labels.set(language="en", value=jsonl_value)
            continue
        elif jsonl_key == "description":
            if item.descriptions.get("en").value != jsonl_value:
                item.descriptions.set(language="en", value=jsonl_value)
            continue

        # Get the wikidata_IDs from the json file.
        wikidata_property_id = wikidata_translation_dict[jsonl_key]
        if isinstance(wikidata_property_id, dict):
            # If the wikidata_property_id is a dict, it means that it is a link to an existing item.
            wikidata_jsonl_objects = wikidata_translation_dict[jsonl_key]
            # jsonl_object is understood in the *object* as in the subject, predicate, object structure of triples
            wikidata_property_id = wikidata_translation_dict[jsonl_key]["_0"]
            if jsonl_key == "information_source" and jsonl_value not in wikidata_jsonl_objects:
                logging.warning(
                    f"The information source {jsonl_value} is not in the json translation.")
                continue
            wikidata_jsonl_objects = [wikidata_jsonl_objects[e]
                                      for e in jsonl_value.split("; ")]
        else:
            wikidata_jsonl_objects = [e for e in jsonl_value.split("; ")]

        # start comparing if the elements in wikidata also occur in the jsonl file. Otherwise, delete the claim.
        existing_claims = item.claims.get(wikidata_property_id)
        for existing_claim in existing_claims:
            existing_snak_of_claim = existing_claim.mainsnak
            if existing_snak_of_claim.datatype == "time":
                last_wikidata_time = datetime.datetime.fromisoformat(
                    existing_snak_of_claim.datavalue["value"]["time"][1:-1])
                jsonl_time = datetime.datetime.fromisoformat(jsonl_value)
                if jsonl_time.date() > last_wikidata_time.date() or len(existing_claims) > 1:
                    # Time Values of our taxonomy are not allowed to have more than one value.
                    changelog.append(
                        f"remove {last_wikidata_time} on prop {wikidata_property_id}")
                    existing_claim.remove()
            elif existing_snak_of_claim.datatype == "wikibase-item":
                value_of_snak = existing_snak_of_claim.datavalue["value"]["id"]
                # if value_of_snak not in wikidata_jsonl_objects:
                #     changelog.append(f"remove {value_of_snak} on prop {wikidata_property_id}")
                #     existing_claim.remove()
            elif existing_snak_of_claim.datatype == "url":
                value_of_snak = existing_snak_of_claim.datavalue["value"]
                if value_of_snak not in wikidata_jsonl_objects:
                    changelog.append(
                        f"remove {value_of_snak} on prop {wikidata_property_id}")
                    existing_claim.remove()

        # Do the opposite, see if there is information in the jsonl not in wikidata
        existing_claims = item.claims.get(wikidata_property_id)
        # if len(existing_claims) != len(wikidata_jsonl_objects):
        wikidata_values = []
        for wikidata_jsonl_object in wikidata_jsonl_objects:
            snaks = [claim.mainsnak for claim in existing_claims]
            if jsonl_key in ["classification", "tool_type", "programming_language", "license", "information_source"]:
                wikidata_values = [value.datavalue["value"]["id"] for value in snaks]
            elif jsonl_key in ["source_repos", "website"]:
                wikidata_values = [value.datavalue["value"] for value in snaks]
            elif jsonl_key == "last_entry_date" and len(snaks) > 0:
                jsonl_time = datetime.datetime.fromisoformat(jsonl_value)
                last_wikidata_time = datetime.datetime.fromisoformat(
                    snaks[0].datavalue["value"]["time"][1:-1])
                if last_wikidata_time.date() >= jsonl_time.date() and len(snaks) == 1:
                    continue
            # elif jsonl_key == "last_entry_date":
            #     values = [value.datavalue["value"]["time"] for value in snaks]
            if wikidata_jsonl_object not in wikidata_values:
                update_claims.append(create_claim(
                    wikidata_property_id=wikidata_property_id, wikidata_object_id=wikidata_jsonl_object))
                changelog.append(
                    f"Add {wikidata_jsonl_object} on {wikidata_property_id}")

    # Check for static, dependent attributes
    # If there is a license, then there *MUST* be a copyright status
    if len(item.claims.get("P275")) > 0:
        if len(item.claims.get("P6216")) == 0:
            changelog.append("Add Copyright Status: Copyrighed")
            update_claims.append(create_claim("P6216", "Q50423863"))

    if len(changelog) > 0:
        print(f"""_________
        {item.id}: {item.labels.get("en").value}
        changelog: {changelog}
        type 'yes' or 'y' to confirm changes:""")
        if input() in ["y", "yes"]:
            # Delete Claims
            item.write()
            item.add_claims(claims=update_claims,
                            action_if_exists=wikibaseintegrator.wbi_enums.ActionIfExists.REPLACE_ALL)
            # write new claims
            item.write()
