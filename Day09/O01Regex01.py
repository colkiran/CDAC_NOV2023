
"""
match, search, find, findall

match will work only at the begning of the string.
search will work throughout the string
"""

import re

# st = "bat"
# res = re.match(r'b.t', st)
# st = "hello world"
# res = re.match(r'^hello', st)
# res = re.search(r'world$', st)
# res = re.search(r'ba*t', st)
# res = re.search(r'ba?t', st)
# res = re.search(r'ba+t', st)
# res = re.search(r'ba{3}t', st)
# res = re.search(r'ba{3,}t', st)
# res = re.search(r'ba{3,6}t', st)
# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiou]t', st)
# res = re.search(r'b[^aeiou]t', st)
# res = re.search(r'b(oa|es)t', st)

# all files with an extension .txt
st = "best.txt"

res = re.search(r'\.txt$', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found...")

