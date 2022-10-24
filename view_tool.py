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

# town with max connections
# max = 0
# max_town = []
# for town in map:
#     if len(town['connections']) > max:
#         max = len(town['connections'])
#         max_town = [town['name']]
#     elif len(town['connections']) == max:
#         max_town.append(town['name'])

# print(max, max_town)