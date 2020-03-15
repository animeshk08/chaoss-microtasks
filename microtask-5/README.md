# Microtask 5:

Execute micro-mordred to collect, enrich and visualize data from Git and GitHub repositories.

## Steps to follow

1 . Use docker compose configuration to instantiate the required components
i.e ElasticSearch, Kibiter and MariaDB.

A configuration file can be found [here](./data/docker-compose.yml).

```
elasticsearch:
  restart: on-failure:5
  image: bitergia/elasticsearch:6.1.0-secured
  command: elasticsearch -Enetwork.bind_host=0.0.0.0 -Ehttp.max_content_length=2000mb
  environment:
    - ES_JAVA_OPTS=-Xms2g -Xmx2g
  ports:
    - 9200:9200

kibiter:
  restart: on-failure:5
  image: bitergia/kibiter:secured-v6.1.4-5
  environment:
    - PROJECT_NAME=Development
    - NODE_OPTIONS=--max-old-space-size=1000
    - ELASTICSEARCH_URL=https://elasticsearch:9200
    - ELASTICSEARCH_USER=kibanaserver
    - ELASTICSEARCH_PASSWORD=kibanaserver
  links:
    - elasticsearch
  ports:
    - 5601:5601
    
mariadb:
  restart: on-failure:5
  image: mariadb:10.0
  expose:
    - "3306"
  ports:
    - "3306:3306"
  environment:
    - MYSQL_ROOT_PASSWORD=
    - MYSQL_ALLOW_EMPTY_PASSWORD=yes
    - MYSQL_DATABASE=test_sh
  command: --wait_timeout=2592000 --interactive_timeout=2592000 --max_connections=300
  log_driver: "json-file"
  log_opt:
      max-size: "100m"
      max-file: "3"

``` 

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
url = https://admin:admin@localhost:9200

[es_enrichment]
url = https://admin:admin@localhost:9200

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
# commonly: Unknown
unaffiliated_group = Unknown
autoprofile = [customer,git,github]
matching = [email]
sleep_for = 120

[panels]
kibiter_time_from= "now-30y"
kibiter_default_index= "git"
kibiter_url = http://admin:admin@localhost:5601
community = true
github-repos = true


[phases]
collection = true
identities = true
enrichment = true
panels = true

[git]
raw_index = git_chaoss
enriched_index = git_chaoss_enriched
latest-items = true
category = commit
studies = [enrich_demography:git, enrich_areas_of_code:git, enrich_onion:git]

[github]
raw_index = github_issues_chaoss
enriched_index = github_issues_chaoss_enriched
api-token = xxxx
sleep-for-rate = true
no-archive = true
category = issue
sleep-time = 300

[github:pull]
raw_index = github_pulls_chaoss
enriched_index = github_pulls_chaoss_enriched
api-token = xxxx
sleep-for-rate = true
no-archive = true
category = pull_request
sleep-time = 300
studies = [enrich_onion:github]

[github:repo]
raw_index = github_pulls_chaoss
enriched_index = github_repo_enriched
category = repository
no-archive = true

[enrich_demography:git]
date_field = utc_commit
author_field = author_uuid

[enrich_areas_of_code:git]
#no_incremental = true
in_index = git_chaoss
out_index = git-aoc_chaoss_enriched

[enrich_onion:git]
in_index = git_chaoss_enriched
out_index = git-onion_enriched
contribs_field = hash
no_incremental = false

[enrich_onion:github]
#no_incremental = true
in_index_iss = github_issues_chaoss_enriched
in_index_prs = github_pulls_chaoss_enriched
out_index_iss = github_issues_onion-enriched
out_index_prs = github_prs_onion-enriched
data_source_iss = github-issues
data_source_prs = github-prs
```
3 . Create a [project.json](./data/projects.json) file which includes the data sources you want to fetch the data from.

```
{
    "grimoire": {
        "git": [
            "https://gitlab.com/nsnam/ns-3-dev"
        ],
        "github": [
            "https://github.com/chaoss/grimoirelab-elk"
        ],
        "*github:pull": [
            "https://github.com/chaoss/grimoirelab-elk"
        ],
        "github:repo": [
            "https://github.com/chaoss/grimoirelab-elk"
        ]
    }
}
```

4 . Run the docker compose configurations to bring up lasticSearch, Kibiter and MariaDB using
 the below command:
 ```
docker-compose -f docker-compose.yml up
```

5 . Run micro.py by editing its configurations and including the following parameters
`--raw --enrich --panels --cfg ./setupp.cfg --backends git github` .

6 . Sit back and wait for the the results or you could see the beauty of GrimoireLab
 by including `--debug` parameter in the configurations :)
 
## Screenshots

Logs on completion of execution:

<img src="./images/LogCompletion.png" width="800" alt="Log Completion">

Kibiter Dashboard for Git data source:

<img src="./images/Git_dashboard.png" width="800" alt="Git Dashboard">

Kibiter Dashboard for Github data source:

<img src="./images/GithubIssues.png" width="800" alt="Github Dashboard">












