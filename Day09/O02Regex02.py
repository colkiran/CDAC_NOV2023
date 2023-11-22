
import re

st = "This is a samPle Ample string"

# res = re.search(r'\w+', st)
# res = re.search(r'\d+', st)
# res = re.search(r'\D+', st)
# res = re.search(r'\W+', st)
# res = re.search(r'\s+', st)
# res = re.search(r'\S+', st)
# res = re.search(r'\AThis', st)
# res = re.search(r'string\Z', st)

res = re.search(r'\bample', st, re.I)

# re.I - ingnore case

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")
