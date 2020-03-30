#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from elasticsearch import Elasticsearch
import pandas

start_time = time.time()

# Create a client instance of ElasticSearch
client = Elasticsearch()

# Total number of ElasticSearch documents to get with API call
total_docs = 20

# Make API call to cluster
# Include the required fields in _source parameter

print("\nMaking API call to ElasticSearch for", total_docs, "documents.\n")
response = client.search(
    index='groupsio_enriched',
    _source=["uuid", "project", "project_1", "origin", "grimoire_creation_date", "body_extract", "Subject_analyzed"],
    body={},
    size=total_docs,
)

# grab list of docs from nested dictionary response
print("Storing document in the list")
elastic_docs = response["hits"]["hits"]

# Get all the indexes from _source

#  Create an empty Pandas DataFrame object for docs
docs = pandas.DataFrame()

# Iterate each ElasticSearch doc in list
print("\nCreating objects from ElasticSearch data.")
for num, doc in enumerate(elastic_docs):
    # Get _source data dict from document
    source_data = doc["_source"]

    # Get _id from document
    _id = doc["_id"]

    # Create a Series object from doc dict object
    doc_data = pandas.Series(source_data, name=_id)

    # Append the Series object to the DataFrame object
    docs = docs.append(doc_data)


# Comment the below line in case JSON is not needed
# Export ElasticSearch document to JSON file
print("\nExporting the index fields to JSON file")
docs.to_json("groupsio.json")

# Export ElasticSearch document to CSV file
print("\nExporting the index fields to CSV file")
docs.to_csv("groupsio.csv", ",")

# Export ElasticSearch document to Excel File
print("\nExporting the index fields to CSV file")
docs.to_excel("groupsio.xlsx")

print("\nTime lapsed:", time.time() - start_time)
