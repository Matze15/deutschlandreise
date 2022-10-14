import json

# idea:
# find the fastest route bewteen two towns with something similar to Dijkstra's algorithm (brute forcing)
# given end/start point and 8 targets in between, determine the fastest way for between each, then determine the fastest order (not sure how yet)

# import map
map = []
with open('map_new.json', 'r') as f:
    map = json.load(f)


# function that takes two towns as arguments and returns an array with the least cities connecting the two
def between(start, target):
    pass
