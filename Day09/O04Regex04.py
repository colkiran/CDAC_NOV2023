
import re

st = "the quick brown fox jumps over the lazy dog"

res = re.search(r'fox' , st)

if res:
    print("Match found")
    print("String that got rejected :", st[:res.start()])
    print("String that Matched the regex :",res.group(0))
    print("String that is unchecked :", st[res.end():])
else:
    print("Match not found")