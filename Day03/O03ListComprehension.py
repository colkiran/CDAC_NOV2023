
l1 = list(range(1, 11))
squares = [n ** 2 for n in l1]
print(f"squares :{squares}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog."
print(f"sentence :{sentence}")

print("-" * 60)
words = [word for word in sentence.split()]
print(f"words :{words}")

print("-" * 60)
fruits = [
    ('apple', 285),
    ('orange', 80),
    ('grapes', 140),
    ('pineapple', 70),
    ('banana', 55),
    ('gauva', 90),
    ('watermelon', 150),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-" * 60)

price = ["fruit" for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[0] for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[1] for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [(fruit[1], fruit[1] * 0.9, fruit[1] * 0.75)
         for fruit in fruits]
print(f"price :{price}")

expFruits = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75)
             for fruit in fruits if fruit[1] >= 100]
print(f"Expensive Fruits :{expFruits}")
print("-" * 60)

words = [(word, len(word)) for word in sentence.split()]
print(f"words :{words}")
print("-" * 60)

words = [(word, len(word)) for word in sentence.split() if word != "the"]
print(f"words :{words}")
print("-" * 60)

boys = ['mike', 'louis', 'charles', 'richard', 'kennedy', 'peter', 'ruben']
girls = ['grace', 'jenifer', 'mary', 'tina', 'aliyah', 'belcia']

combine = [(boy, girl) for boy in boys for girl in girls]
print(f"combine :{combine}")

print("-" * 60)
combine = list(zip(boys, girls))
print(f"combine :{combine}")

