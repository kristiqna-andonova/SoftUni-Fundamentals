wagons = int(input())
train = [0] * wagons

while True:
    command = input().split()

    if command[0] == "End":
        print(train)
        break

    elif command[0] == "add":
        people = int(command[1])
        train[-1] += people

    elif command[0] == "insert":
        people = int(command[2])
        index_people = int(command[1])
        train[index_people] += people

    elif command[0] == "leave":
        people = int(command[2])
        index_people = int(command[1])
        train[index_people] -= people
