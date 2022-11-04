import sys
import re
import numpy as np

# get filename
filename = sys.argv[1]

# opening and reading the file 
with open(filename) as fh:
   fstring = fh.readlines()
  
# regex pattern of IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  
# empty list object
lst=[]
  
# extracting the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])
  
# displaying count of the unique IP addresses
print(len(np.unique(lst)))
