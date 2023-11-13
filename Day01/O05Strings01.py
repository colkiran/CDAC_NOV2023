
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("slicing".center(60, "-"))
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")

print("Reverse Indexing".center(60, "-"))
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1]      :{st[::-1]}")


print("-" * 60)

# strings are immutable

# print(f"st :{st}")
# st[0] = "H"

# print(dir(st))

print("find".center(60, "-"))
print(f"st :{st}")

print(st.find("l"))
print(st.find("l", st.find("l")+1))
print(st.find("l", st.find("l", st.find("l")+1)+1))

print("replace".center(40, "-"))
print(f"st :{st}")
res = st.replace("h", "H")
print(f"res :{res}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

print("Maketrans".center(60, "-"))
print(f"st :{st}")

a = 'helowrd'
b = 'HELOWRD'
# lenght of a and b should be the same
tranTbl = st.maketrans(a, b)
print(f"Table :{tranTbl}")

res = st.translate(tranTbl)
print(f"res :{res}")
