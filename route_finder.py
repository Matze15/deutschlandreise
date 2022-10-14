import json
import copy

# idea:
# find the fastest route bewteen two towns with something similar to Dijkstra's algorithm (brute forcing)
# given end/start point and 8 targets in between, determine the fastest way for between each, then determine the fastest order (not sure how yet)

# import map
map = []
with open('map_new.json', 'r') as f:
    map = json.load(f)


# function that takes two towns as arguments and returns an array with the least cities connecting the two
def between(start, target): # e.g. start = 'Kiel'
    # avoid double checking same town
    checked = [start]
    # logging all paths temporarily
    current = [[start]]

    target_found = start == target

    while not target_found:
        # write to copy and later replace, not to confuse the for loop
        temp_current = copy.copy(current)
        # loop through each path
        for path in current:
            # loop through towns connected to the last node of each path
            for connection in map[path[len(path)-1]]:
                # check if the connection has previously appeared
                if not connection in checked:
                    # if it is a yet unknown node, create a copy of the path, add it, add the new path to temp_current
                    new_path = copy.copy(path)
                    new_path.append(connection)
                    temp_current.append(new_path)
                    # also add the node to the list of visited nodes
                    checked.append(connection)

                    #now check if the connection happens to be the target node
                    if connection == target:
                        # if so, return the path up until this point
                        target_found = True
                        return new_path
        
        # after the loop is done, overwrite the current current with the new temp_current
        current = copy.copy(temp_current)


von = input('Von: ')
nach = input('Nach: ')
weg = between(von,nach)
print(weg,len(weg))