import json

map = []

# get user input 
def handle_user_input():
    town = input('Town name (Leave empty to finish process): ')
    if not town:
        return False
    else:
        connections = input(town + ' is connected to (seperate by commas): ').replace(' ', '').split(',')
        return {"name": town, "connections": connections}

# loop getting user input until ready
while True:
    user_input = handle_user_input()
    if user_input:
        map.append(user_input)
    else:
        break


# write map to map.json file
with open('map.json', 'w') as f:
    json.dump(map,f,ensure_ascii=False,indent=4)