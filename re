import re

with open('files/test.log','r') as f:
    for line in f.readlines():
        result=re.findall('ht',line)
        print(result)
        # if result is not None:
        #     print(line)
