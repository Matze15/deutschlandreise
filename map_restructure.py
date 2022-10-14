import json

# structuring map from [{name: Kiel, connections: [...]}] to {kiel: [...], flensburg: [...]}

old_map = []
new_map = {}

with open('map.json', 'r') as f:
    old_map = json.load(f)

for elem in old_map:
    new_map[elem['name']] = elem['connections']

with open('map_new.json', 'w') as f:
    json.dump(new_map, f, ensure_ascii=False, indent=4)