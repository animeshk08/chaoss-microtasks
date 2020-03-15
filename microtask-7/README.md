# Microtask 7:
Install and use [elasticdump](https://www.npmjs.com/package/elasticdump) to download the mapping and data of
an ElasticSearch index (it can be anyone created in Microtask 5).

## Steps to follow

1 . Install elastic dump using the below command.
```
(local)

npm install elasticdump
./bin/elasticdump

(global)

npm install elasticdump -g
elasticdump

```
2 . To store the mapping of ElasticSearch index in a file [git_chaoss_enriched_mapping.json](./data/git_chaoss_enriched_mapping.json) run the below command.
 Here `git_echaoss_enriched` is the index whose mapping is to be stored.
``` 
sudo elasticdump   --input=http://localhost:9200/git_chaoss_enriched   --output=./../data/git_chaoss_enriched_mapping.json   --type=mapping

```    

3 . To store the data of ElasticSearch index in a file [git_chaoss_enriched_data.json](./data/git_chaoss_enriched_data.json) run the below command.
 Here `git_echaoss_enriched` is the index whose mapping is to be stored.
``` 
sudo elasticdump   --input=http://localhost:9200/git_chaoss_enriched   --output=./../data/git_chaoss_enriched_data.json   --type=data

```

