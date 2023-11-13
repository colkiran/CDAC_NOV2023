
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag': [300, 350, 425, 400, 360],
    'sourav': [180, 250, 200, 350, 150],
    'laxman': [345, 300, 200, 150, 190],
    'yuvraj': [190, 150, 120, 250, 275]
}

print(players['sachin'])
print(sum(players['sachin']))
print("-" * 60)

plyrs = [k for k in players]
print(f'Players :{plyrs}')
print("-" * 60)

plyr_scr = {k: sum(v) for k, v in players.items()}
print(f"Player_Score :{plyr_scr}")
print("-" * 60)

plyr_scr = {k: (lambda scores :sum(scores) / len(scores))(v)
            for k, v in players.items()}
print(f"Average Scores :{plyr_scr}")
print("-" * 60)

basic = [{x: (lambda par: "Mr." + par) ("Sachin {}".format(x))}
         for x in range(1, 6)]
print(basic)
print("-" * 60)

scr = [plyr_scr for plyr_scr in players.values()]
print(f"scores :{scr}")
print("-" * 60)

scr = [x for plyr_scr in players.values() for x in plyr_scr]
print(f"scr :{scr}")
print("-" * 60)

scr = [x for plyr_scr in players.values() for x in plyr_scr if x >= 200]
print(f"Scores :{scr}")
print("-" * 60)

scores = {name: [scr for scr in score if scr >= 200]
          for name, score in players.items()}
print(f"scores :{scores}")
