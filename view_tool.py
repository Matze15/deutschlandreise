import json

map = []

with open('map.json','r') as f:
    map = json.load(f)

# map size
# print(len(map))

# average connection count
# sum = 0
# avg = 0
# for town in map:
#     sum += len(town['connections'])

# print(sum/len(map))

