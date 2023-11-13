
print("keys".center(60, "-"))
player = {'name': 'Rahul', 'age': 34, 'runs': 65, 'oppn': 'Pak', 'venue': 'Lahore', 'year': '1998'}

print(f"player :{player}")
kys = player.keys()
print(kys)

# values
print("-" * 60)
vls = player.values()
print(vls)

print("-" * 60)
player = {'name': 'Rahul', 'age': 34, 'runs': 65, 'oppn': 'Pak', 'venue': 'Lahore', 'year': '1998'}
print(f"player :{player}")

print("-" * 60)
print(player.get('name', "Please enter a valid key....."))

print("fromkeys".center(60, "-"))
cities = ['che', 'mum', 'blr', 'del', 'hyd', 'kol']

print(f"cities :{cities}")

res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 23)
print(f"res :{res}")

print("setdefault".center(60, "-"))

player = {'name': 'Rahul', 'age': 34, 'runs': 65, 'oppn': 'Pak'}
print(f"player :{player}")

player.setdefault('age', 36)
player.setdefault('venue', 'chepauk')
player.setdefault("runs", 150)

print(f"player :{player}")

print("pop".center(60, "-"))
player = {'name': 'Rahul', 'age': 34, 'runs': 65, 'oppn': 'Pak', 'venue': 'Lahore', 'year': '1998'}
print(f"player :{player}")

res = player.pop('year')
print(f"res :{res}")

res = player.pop('age')
print(f"res :{res}")

# res = player.pop()
# print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(60, "-"))
player = {'name': 'Rahul', 'age': 34, 'runs': 65, 'oppn': 'Pak', 'venue': 'Lahore', 'year': '1998'}
print(f"player :{player}")

res = player.popitem()          # last item
print(f"res :{res}")
print(f'player :{player}')

print("items".center(60, "-"))
player = {'name': 'Rahul', 'age': 34, 'runs': 65, 'oppn': 'Pak', 'venue': 'Lahore', 'year': '1998'}
print(f"player :{player}")

print("-" * 60)
for k, v in player.items():
    print(k, "=>", v)

print("update".center(60, "-"))
player1 = {'name': 'Rahul', 'age': 34, 'runs': 65, 'oppn': 'Pak', 'venue':'chinaswamy'}
player2 = {'name': 'Sachin', 'age': 32, 'runs': 185, 'oppn': 'SA', 'year':2001}

print(f"player1 :{player1}")
print(f"player2 :{player2}")

print("-" * 60)
player1.update(player2)
print(f"player1 :{player1}")

