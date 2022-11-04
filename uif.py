import sys
import re
import numpy as np

filename = sys.argv[1]

# opening and reading the file 
with open(filename) as fh:
   fstring = fh.readlines()
  
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  
# initializing the list object
lst=[]
  
# extracting the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])
  
# displaying the extracted IP addresses
print(len(np.unique(lst)))