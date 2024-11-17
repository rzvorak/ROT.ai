import CreateInputVector as shitProgram
import time as time;

def recurse():
    counter = 0
    while True:
        try:
            shitProgram.createInputVector()
        except Exception as e:
            time.sleep(8)
            counter = counter + 1
            print("Starting again number ", counter)
            with open('output.txt', 'r') as f:
                lines = f.readlines()
                if(len(lines) > 1083):
                    break
                else:
                    recurse()

    print("holy shit you are done")

recurse()
        
