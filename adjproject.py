import random

class Person():
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
        self.uid = random.randint(1000, 9999)
        self.fNumber = 0

def build_adjacency(data):
    adj_dict = dict()
    for node in data:
        a = node[0]
        b = node[1]
        if a in adj_dict:
            adj_dict[a].append(b)
            a.fNumber += 1
        else:
            adj_dict[a] = [b]
        if b in adj_dict:
            adj_dict[b].append(a)
            b.fNumber += 1
        else:
            adj_dict[b] = [a]
    return adj_dict

def displayAdj(adj_dict):
    for key, val in adj_dict.items():
        print(f"{key.uid}: {key.fName} {key.lName}, number of friends: {key.fNumber+1}")
        for friend in val:
            print(f"  {friend.fName} {friend.lName} ({friend.uid})")

if __name__ == '__main__':
    p1 = Person("Anita", "Racinez")
    p2 = Person("Clem", "Jameson")
    p3 = Person("Lars", "Eriksson")
    p4 = Person("Jed", "Jones")
    data = [(p1, p2), (p2, p3), (p1, p4), (p2, p4)]
    displayAdj(build_adjacency(data))
