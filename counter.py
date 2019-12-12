# Python script to return the top 10 most common words given a text file.

# messages.txt is a text file of all the Venmo messages I personally collected.
from collections import Counter 

f = open("messages.txt","r")
venmo_messages = f.read()
  
all_words = venmo_messages.split() 
  
Counter = Counter(all_words) 
  
most_common_words = Counter.most_common(10) 

# Prints top 10 most common words from Venmo data set.
print(most_common_words) 
