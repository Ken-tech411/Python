command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to quit the game
        ''')
    elif command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("The car started!")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print("The car stopped!")
    elif command == "quit":
        break
    else:
        print("Unknown command!")
