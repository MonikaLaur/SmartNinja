a_dict = {}
points = {"alfred":10,
          "bettina": 100,
          "christian": 50,
          "doris": 75}

print points #  {'christian': 50, 'bettina': 100, 'doris': 75, 'alfred': 10}

#reference

print points["alfred"] # 10

for name in ["alfred", "bettina"]:
    print name, points[name] # alfred 10 bettina 100

#change
for name in ["alfred", "bettina"]:
    points[name] += 10
print points # {'christian': 50, 'bettina': 110, 'doris': 75, 'alfred': 20}

points ["alfred"] = 30
print points # {'christian': 50, 'bettina': 110, 'doris': 75, 'alfred': 30}
points ["franz"] = 40
print points # {'franz': 40, 'christian': 50, 'bettina': 110, 'doris': 75, 'alfred': 30}

#update
points.update ( {"erwin":-10, "alfred":200 } )
print points # {'erwin': -10, 'christian': 50, 'alfred': 200, 'franz': 40, 'bettina': 110, 'doris': 75}