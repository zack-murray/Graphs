import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.reset
    
    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendships(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []
        
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Add friendships
        for i in range(num_users * avg_friendships // 2):
            friendships = possible_friendships[i]
            self.add_friendships(friendships[0], friendships[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        # Instantiate an empty queue
        q = Queue()

        # Add input user id to the queue
        q.enqueue([user_id])

        # While the q isn't empty
        while q.size() > 0:
            # Instantiate friend path
            path = q.dequeue()
            # Last person in the path
            most_recent = path[-1]
            # print('# OF ELEMENTS IN QUEUE')
            # print(q.size())
            # print('VISITED')
            # print(visited)
            # print('PATH')
            # print(path)

            # If last person in the path hasn't been visited
            if most_recent not in visited:
                # Add them
                visited[most_recent] = path

                # Loop through each friend
                for friend in self.friendships[most_recent]:
                    # Make a copy of path 
                    path_copy = list(path)
                    # Append friend connections
                    path_copy.append(friend)
                    # Add them to the queue
                    q.enqueue(path_copy)
                    # print('PATH COPY')
                    # print(path_copy)
                    
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('FRIENDSHIPS')
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('CONNECTIONS')
    print(connections)