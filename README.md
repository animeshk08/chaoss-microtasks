# GSoC Idea: Implement the Social Currency Metrics System in GrimoireLabs 

The Social Currency Metrics System (SCMS) is a qualitative data collection, processing, and measurement system that augments quantitative community management metrics already available in CHAOSS properties. Implementing the SCMS will ultimately help community leaders, power users, and other stakeholders leverage qualitative data for social listening so that they can rely less on the behaviors quantitative data tracks and more on community sentiment. The SCMS empowers community leaders to make decisions based on what community members freely share about their opinions, wants, and needs.

The SCMS shows why trends occur and identifies commonly missed pitfalls in conclusions taken from quantitative data. With an SCMS platform built natively into a CHAOSS Bitergia property, open-source communities can use it to facilitate members’ input in decisions essential to community health.

The purpose of this project is to:
Build the SCMS in one of CHAOSS project’s systems that collects qualitative data from several channels, displays that information for manipulation and tagging, and outputs it to a metric dashboard such as the SCMS information page found here.

The aims of this project are to:

* Create an API that collects and returns data collected from a community of the GSoC participants’ choice.
* Gain familiarity with and create a way to grade, tag, and process large amounts of data.
* Develop creative ways to display complex datasets in the Bitergia Analytics System.
* Investigate ways to process qualitative data at scale using AI or similar technology.
* Encourage the larger development of social listening tools based on qualitative data.

For more information regarding the GSoc Idea visit [here](https://github.com/chaoss/governance/blob/master/GSoC-Ideas.md#idea-implement-the-social-currency-metrics-system-in-grimoirelabs).

## Microtasks

#### Microtask 0:

Download [PyCharm](https://www.jetbrains.com/pycharm/) and get
familiar with it (for instance, you can follow this
[tutorial](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)).

This task has been completed [here](./microtask-0).

#### Microtask 1:
Set up Perceval to be executed from PyCharm.

This task has been completed [here](./microtask-1).

#### Microtask 2:
Create a Python script to execute Perceval via its Python interface using
the GitLab and GitHub backends. Feel free to select any target repository.

This task has been completed [here](./microtask-2).

#### Microtask 3:
Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:

* What is the meaning of the JSON attribute 'timestamp'?
* What is the meaning of the JSON attribute 'updated_on'?
* What is the meaning of the JSON attribute 'origin'?
* What is the meaning of the JSON attribute 'category'?
* How many categories do the GitHub and GitLab backends have?
* What is the meaning of the JSON attribute 'uuid'?
* What is the meaning of the JSON attribute search_fields?
* What is stored in the attribute data of each JSON document produced by Perceval?

This task has been completed [here](./microtask-3).

#### Microtask 4:
Set up a dev environment to work on GrimoireLab. Have a look to https://github.com/chaoss/grimoirelab-sirmordred#setting-up-a-pycharm-dev-environment.

This task has been completed [here](./microtask-4).

#### Microtask 5:
Execute micro-mordred to collect, enrich and visualize data from Git and GitHub repositories.

This task has been completed [here](./microtask-5).

#### Microtask 6:
Using the dev tools in Kibiter, create a query that counts the number of
unique authors on a Git repository from 2018-01-01 until 2019-01-01.

This task has been completed [here](./microtask-6).

#### Microtask 7:
Install and use [elasticdump](https://www.npmjs.com/package/elasticdump) to download the mapping and data of
an ElasticSearch index (it can be anyone created in Microtask 5).

This task has been completed [here](./microtask-7).

#### Microtask 8:
Execute micro-mordred to collect and enrich data from a groupsio repository.
You need to register to a group (e.g., https://lists.onap.org/g/main) and
follow the instructions at https://github.com/chaoss/grimoirelab-sirmordred#groupsio.
Then, write a script to read the enriched index and import the attributes `uuid`, `project`,
`project_1`, `origin`, `grimoirelab_creation_date`, `body and subject_analyzed` to a CSV file.
Import the obtained file to an excel sheet (in a manual or automatic way)

This task has been completed [here](./microtask-8).

#### Microtask 9:
Build a Data Table visualization in Kibiter (you can use the [CHAOSS community dashboard](https://chaoss.biterg.io/app/kibana#/visualize/new?_g=())
that shows for emails (`mbox` index) the text of emails (split row by Term `body_extract` field).

This task has been completed [here](./microtask-9).

#### Microtask 10:
Submit at least a PR to one of the GrimoireLab repositories to fix an issue, improve the documentation, etc.

This task has been completed [here](./microtask-10).


For any queries and reviews please open a new issue.
You can also contact:

<b>Animesh Kumar</b><br>
Github: [animeshk08](https://github.com/animeshk08)<br>
Email: animuz111@gmail.com

Thank you to all the mentors for their guidance and reviews. :)
Looking forward to contribute more to Chaoss and GrimoireLabs in future. :rocket:





