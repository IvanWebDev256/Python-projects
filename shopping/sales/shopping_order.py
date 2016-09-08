class Order(object):
    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        print("[command] [item] (command is a to add, d to delete, q to quit")
        line = input()
        command = line[:1]
        self.item = line[2:]
        if command == "q":
            self.quit = True
        elif command == "a":
            self.add = True
        elif command == "d":
            self.delete = True