# Microtask 3:
Based on the JSON documents produced by Perceval and its source code, 
try to answer the following questions:

* What is the meaning of the JSON attribute 'timestamp'?
    
    The attribute ['timestamp'](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backend.py#L332)
    is the datetime(in unix timestamp format) when the item was
    fetched from the data source.
    
    
* What is the meaning of the JSON attribute 'updated_on'?
    
    The attribute ['updated_on'](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L163)
    is the datetime(in unix timestamp format) when the item was last
    updated in the data source.
    
    
* What is the meaning of the JSON attribute 'origin'?
    
    The attribute ['origin'](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backends/core/gitlab.py#L109)
    is the location(in URL format) of the data source.
   
  
* What is the meaning of the JSON attribute 'category'?
    
    The attribute 'category' is the types(kinds) of data that is fetched from the data source.
    For [GitHub](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backends/core/github.py#L109)
    backend the different categories are issue, pull_request  and repository.
    For [GitLab](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backends/core/gitlab.py#L100)
    backend the different categories are issue and merge_request.    
    

* How many categories do the GitHub and GitLab backends have?

    [GitHub](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backends/core/github.py#L109)
    backend the has three categories; issue, pull_request  and repository.
    [GitLab](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backends/core/gitlab.py#L100)
    backend the two categories; issue and merge_request.    


* What is the meaning of the JSON attribute 'uuid'?
    
    The attribute ['uuid'](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backend.py#L334)
    is a unique id for an item fetched by perceval. As mentioned in the [documentation](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L430),
    
    The UUID will be the SHA1 of the concatenation of the values
    from the list. The separator between these values is ':'.
    Each value must be a non-empty string, otherwise, the function
    will raise an exception.
    
    For GitHub and Gitlab backend the uuid for the item 
    is calculated using `origin` and `item_id` of the item.
    

* What is the meaning of the JSON attribute search_fields?

    The attribute 'search_fields' includes extra information
    about the item fetched by Perceval. The 'search_fields' for [Github](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backends/core/github.py#L161)
    backend include, `id`,`owner` and `repo`. The 'search_fields'
    for [GitLab](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backends/core/gitlab.py#L142)
    backend include, `id`, `owner`, `iid`, `project` and `groups`.
    Search fields are useful to avoid inspecting the content of
    the data attribute, since they expose a set of attributes to ease search operations.


* What is stored in the attribute data of each JSON document produced by Perceval?
    
    The attribute ['data'](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backend.py#L340)
    stores the actual data which is fetched from the data source. 
    In case, the data to be fetched is issues from Github backend, the issue data will
    be stored in the 'data' attribute. 


