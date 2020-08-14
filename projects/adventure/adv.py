from room import Room
from player import Player
from world import World
import random

from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
##################################################################################################

# Fill this out with directions to walk
# Document our every move, traversal_path = ['n', 'e', 's', 's', 'e' ..] 
traversal_path = []

# Keep track of how to get back when we reach dead ends, reversal_path = ['s', 'w', 'n', 'n', 'w' ..]
reversal_path = []

# Helper for reverse path
reversed_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Keep track of the unique rooms we've visited
visited = set()

# Mark the starting room as visited
visited.add(player.current_room.id)

# While the maze can still be explored
while len(visited) < len(room_graph):

    # Initialize our next room to none
    # next_room = None
    next_room = []

    # Loop through possible exits
    for possible_path in player.current_room.get_exits():
         # If there are rooms to exit to that aren't in visited
        if player.current_room.get_room_in_direction(possible_path).id not in visited:
            # Set next room to that direction
            next_room = possible_path
            # next_room.append(possible_path)
            # print('POSSIBLE PATH')
            # print(next_room)


    # If there are unvisited paths to be traversed 
    # if next_room is not None:
    if len(next_room) > 0: 

        random_direction = random.choice(next_room)
        # Append the direction you intend to move to the list
        # traversal_path.append(next_room)
        traversal_path.append(random_direction)

        # Append the opposite direction to the reversed list
        # reversal_path.append(reversed_directions[next_room])
        reversal_path.append(reversed_directions[random_direction])

        # Move the player to the unvisited tile and add it to the set
        # player.travel(next_room)
        player.travel(random_direction)  
        visited.add(player.current_room.id)
        # print('CURRENT ROOM ID')
        # print(player.current_room.id)
        # print('TRAVERSAL PATH')
        # print(traversal_path)
        # print('REVERSE PATH')
        # print(reversal_path)
        # print('VISITED ROOMS')
        # print(visited)


    else:
        # We've hit a dead-end

        # Pop the direction at the top of the reverse path stack
        # to start traversing back to possible exits
        next_room = reversal_path.pop()

        # Keep traversal path up to date
        traversal_path.append(next_room)

        # Start moving back the way you've traveled
        player.travel(next_room)


##################################################################################################
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
