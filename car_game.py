carStarted = False
carStopped = False

while True:
    command = input("> ")

    if command.upper() == 'HELP':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit""")
    elif command.upper() == 'START':
        if carStarted:
            print("Car is already started")
        else:
            carStarted = True
            carStopped = False
            print("Car started...Ready to go!")
    elif command.upper() == 'STOP':
        if carStopped:
            print("Car is already stopped")
        else:
            carStopped = True
            carStarted = False
            print("Car stopped.")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")