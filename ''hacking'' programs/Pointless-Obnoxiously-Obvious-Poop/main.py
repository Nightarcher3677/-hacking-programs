import time
import os, sys

while True:
    command = input('||> ')
    if 'run' in command:
        try:
            file_to_run = command.split(' ')[1].strip()
            with open(file_to_run, 'r+') as fileopened:
                file = fileopened.read()
                print('Loading ' + file_to_run)
                if 'math' in str(file):
                    for item in file.split("\n"):
                        if "math" in item:
                            operator = item.split(' ')[1].strip()
                            num1unrefined = item.split(operator + ' ')[1].strip()
                            num2 = num1unrefined.split(' ')[1].strip()
                            str = str(num1unrefined) #initial string
                            reversed=''.join(reversed(str)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
                            num1edit = reversed #print the reversed string
                            num1 = num1edit.split(' ')[1].strip()
                            if '+' in operator:
                                try:
                                    result = float(num1) + float(num2)
                                    print(">", result)
                                except:
                                    print(f"Build Failed: Math error in file '{file_to_run}'")
                            elif '-' in operator:
                                print('- detected')
                                #try:
                                result = float(num1) - float(num2)
                                print(">", result)
                                #except:
                                #    print(f"Build Failed: Math error in file '{file_to_run}'")
                            elif '*' in operator:
                                try:
                                    result = float(num1) * float(num2)
                                    print(">", result)
                                except:
                                    print(f"Build Failed: Math error in file '{file_to_run}'")
                            elif '/' in operator:
                                try:
                                    result = (float(num1) / float(num2))
                                    print(">", result)
                                except:
                                    print(f"Build Failed: Math error in file '{file_to_run}'")
                            else:
                                print('Error: Operator load fail')

        except:
            try:
                try:
                    file_to_run = command.split(' ')[1].strip()
                    with open(file_to_run, 'r+') as fileopened:
                        file = fileopened.read()
                except:
                    print(f"FileError: File '{file_to_run}' was not found.")
            except:
                print(f"Build Failed: Unknown error in file '{file_to_run}'")
    elif 'exit' in command:
        sys.exit()
