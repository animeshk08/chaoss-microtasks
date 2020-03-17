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

2. Run the srcipt [elasticdump_script](./elasticdump_script) using the below command:

   `./elasticdump_script`

This will create a file [git_chaoss_enriched_mapping.json](./data/git_chaoss_enriched_mapping.json) having the mapping of ElasticSearch index,
and a file [git_chaoss_enriched_data.json](./data/git_chaoss_enriched_data.json) having the data of ElasticSearch index.

> In the script `git_chaoss_enriched` is the index whose mapping is to be stored.

