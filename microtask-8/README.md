# Microtask 8:
Execute micro-mordred to collect and enrich data from a groupsio repository.
You need to register to a group (e.g., https://lists.onap.org/g/main) and
follow the instructions at https://github.com/chaoss/grimoirelab-sirmordred#groupsio.
Then, write a script to read the enriched index and import the attributes `uuid`, `project`,
`project_1`, `origin`, `grimoirelab_creation_date`, `body and subject_analyzed` to a CSV file.
Import the obtained file to an excel sheet (in a manual or automatic way)

## Steps to follow

1 . Use docker compose configuration to instantiate the required components
i.e ElasticSearch, Kibiter and MariaDB.

A configuration file can be found [here](./../microtask-5/data/docker-compose.yml).

2 . Prepare a configuration file for Mordred. The configuration used is [setup.cfg](./data/setup.cfg) as shown below:
```
[general]
short_name = Grimoire
update = false
min_update_delay = 10
debug = true
# /var/log/mordred/
logs_dir = logs
# Number of items per bulk request to Elasticsearch
bulk_size = 100
# Number of items to get from Elasticsearch when scrolling
scroll_size = 100
menu_file = ../menu.yaml
aliases_file = ../aliases.json

[projects]
projects_file = ./projects.json

[es_collection]
url = http://admin:admin@localhost:9200

[es_enrichment]
url = http://admin:admin@localhost:9200

[sortinghat]
host = 127.0.0.1
user = root
password =
database = test_sh
load_orgs = true
orgs_file = data/orgs_sortinghat.json
identities_api_token = 'xxxx'
identities_file = [data/perceval_identities_sortinghat.json]
affiliate = true
unaffiliated_group = Unknown
autoprofile = [customer,git,github]
matching = [email]
sleep_for = 120

[panels]
kibiter_time_from= "now-30y"
kibiter_default_index= "git"
kibiter_url = http://admin:admin@localhost:5601
community = true

[phases]
collection = true
identities = true
enrichment = true
panels = true

[groupsio]
raw_index = groupsio_raw
enriched_index = groupsio_enriched
email = {email}
password = {password}
```
3 . Create a [project.json](./data/projects.json) file which includes the data sources you want to fetch the data from.
```
{
    "Chaoss": {
        "groupsio": [
            "zabiplane"
        ]
    }
}
```
4 . Run the docker compose configurations to bring up ElasticSearch, Kibiter and MariaDB using
 the below command:
 ```
docker-compose -f docker-compose.yml up
```

5 . Run micro.py by editing its configurations and including the following parameters
`--raw --enrich --panels --cfg ./setupp.cfg --backends groupsio` .

6 . Install the following Python packages:
```
pip3 install elasticsearch
pip3 install pandas
pip3 install openpyxl
```

7 . Run [script.py](./data/script.py) to convert the ElasticSearch document to [JSON](./data/groupsio.json),
 [CSV](./data/groupsio.csv) and [Excel](./data/groupsio.xlsx) File.
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from elasticsearch import Elasticsearch
import pandas

start_time = time.time()

# Create a client instance of Elasticsearch
client = Elasticsearch()

# Total number of Elasticsearch documents to get with API call
total_docs = 20

# Make API call to cluster
# Include the required fields in _source parameter

print("\nMaking API call to Elasticsearch for", total_docs, "documents.\n")
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

# Iterate each Elasticsearch doc in list
print("\nCreating objects from Elasticsearch data.")
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
# Export Elasticsearch document to JSON file
print("\nExporting the index fields to JSON file")
docs.to_json("groupsio.json")

# Export Elasticsearch document to CSV file
print("\nExporting the index fields to CSV file")
docs.to_csv("groupsio.csv", ",")

# Export Elasticsearch document to Excel File
print("\nExporting the index fields to CSV file")
docs.to_excel("groupsio.xlsx")

print("\nTime lapsed:", time.time() - start_time)
```

Output logs of `script.py`:

<img src="./images/Groupsio_Log.png" width="800" alt="Groupsio Log">

8 . Open [groupsio.xlsx](./data/groupsio.xlsx) locally in any spreadsheet reader.

Opening the file in LibreOffice Calc:

<img src="./images/Groupsio_Excel.png" width="800" alt="Groupsio Excel Output">

9 . To open the [groupsio.csv](./data/groupsio.csv) file on [Google Sheets](https://www.google.com/sheets/about/) follow the below steps:

* Go to [Google Sheets](https://www.google.com/sheets/about/), sign in and create a spreadsheet
 to which the CSV is to be imported.
 
* Copy the Spreadsheet Id from the URL as shown below and update the `sheet_id` in [config.ini](./data/config.ini) file. Also set 
  `csv_file` to the name of the CSV file you want to upload to Google Sheets.
  
<img src="./images/Google_sheets_sheetid.png" width="800" alt="Google Sheets spreadsheet id">  

* Go to [Google Sheets API documentation](https://developers.google.com/sheets/api/quickstart/python) and click on 
  `Enable the Google Sheets API`. This will enable the API and also download `credential.json` file. Paste the file
   in the current working directory. 

<img src="./images/Google_sheets_API_doc.png" width="800" alt="Google Sheets API DOC">

* Run [import_gsheets.py](./data/import_gsheets.py). You will be prompted to Sign in to your Google Account the first
  time, make sure you sign in using the same account used to create the spreadsheet. After successful Sign in a `token.pickle`
  file will be download in your current working directory. This file will be used to avoid future Sign in prompts.
     
<img src="./images/Google_sheets_signin.png" width="800" alt="Google Sheets Sign in">  
 
* Open the created spreadsheet again in your browser, the CSV will now be uploaded to the spreadsheet.
  
<img src="./images/Google_sheets_uploaded.png" width="800" alt="Google Sheets CSV uploaded">  

