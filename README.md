objmatcher
==============================
Match Generated Object and Return Similarity Score. 

Using cosine similarity to measure the likeness between two objects.



#### Data Class
 
```python
 
from objmatcher import match, Data

data = Data()

 ```

Available methods:
* add_meta_data()
* get_all_meta_data()
* get_meta_data_by_key()
* to_json()


#### MatchResult Class

Returned by __init__ match method

Availble methods:

* get_scores()
* get_score_by_key()
* get_average_scores()
* get_keys()