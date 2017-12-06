# coding=utf-8

capitals = {"France": "Paris",
            "Iceland": "Reykjavik",
            "Denmark": "Copenhagen",
            "Litauen": "Vilnius",
            "Canada": "Ottawa",
            "Österreich": "Wien"}

print "Study the following list: "
print
print capitals.items()

for k,v in capitals.items():
    print k,v

print capitals.keys() # ['Canada', '\xc3\x96sterreich', 'Iceland', 'France', 'Denmark', 'Litauen']
print capitals.values() # ['Ottawa', 'Wien', 'Reykjavik', 'Paris', 'Copenhagen', 'Vilnius']