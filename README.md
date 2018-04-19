objmatcher
==============================
Match Generated Object and Return Similarity Score. 

Using cosine similarity to measure the likeness between two objects.



#### ObjectMatcher Class
 
```python
 
from objmatcher import ObjectMatcher

matcher = ObjectMatcher()
data1 = matcher.generate_object()
data1.add_meta_data('name', 'foo fighters')
data1.add_meta_data('song', 'best of you')
data1.add_meta_data('song', 'the pretender')
data1.add_meta_data('genre', 'grunge')

data2 = matcher.generate_object()
data2.add_meta_data('name', 'nirvana')
data2.add_meta_data('song', 'smell like teen spirit')
data2.add_meta_data('genre', 'grunge')

matcher.match(data1, data2) ## Returns Matcher Class

 ```

#### Matcher Class

+ get_similarity_score()
+ get_average_scores()