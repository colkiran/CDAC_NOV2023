
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))
print("-" * 60)

d2 = {'name': 'Sachin', 'age': 32, 'runs': 85, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'rahul'), ('age', 31), ('runs', 102), ('oppn', 'SA')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name="Sachin", age=34, runs=125, oppn='Pak')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD

player = {'name': "Sachin", 'age':34, 'runs': 125, 'oppn':'Pak'}
print(f"player :{player}")

print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
for x in player:
    print(x, "=>", player[x])

#update

player['name'] = "Rahul"
player['runs'] = 65
player['venue'] = 'Lahore'
player['year'] = '1998'

print(f"player :{player}")

print("-" * 60)
# delete

del player['age']
del player['year']

print(f"player :{player}")

print(dir(player))
