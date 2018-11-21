def parseError(message, line):
    print("[Parse Error] " +str(message)+ "\n    On line: "+ str(line))
    exit(1)

def fileLoadError(filename):
    print("[File Error] Unable to load: "+ str(filename))
    exit(1)

def syntaxError(instruction, line):
    print("[Syntax Error] On line: "+ str(line) + "\n>    "+ str(instruction))
    exit(1)

def invalidInstructionError(command, line):
    # Convert list to string
    command_str = ""
    for section in command:
        command_str += section + " "
    
    print("[Invalid Instruction] On line: "+ str(line) + "\n>    "+ str(command_str))
    exit(1)
