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

def emptyPipeError(command):
	# Convert list to string
    command_str = ""
    for section in command:
         command_str += section + " "
    print("[Runtime Error] The pipe is empty, yet a fetch was attempted")
    print(">    " + str(command_str))
    exit(1)

def invalidLocationError(loc_prefix):
	print("[Runtime Error] An attempt was made to save a value to: "+ str(loc_prefix))
	print("This is not allowed")
	exit(1)

def invalidTempSlot(loc):
	print("[Runtime Error] An attempt was made to save a value to: "+ str(loc))
	print("This does not exsist")
	exit(1)

def unknown(command):
	print("An unknown error occured...")
	print(command)
	exit(1)

def pipeTooSmallError(instruction):
	print("[Runtime Error] The pipe is too small to execute instruction: "+ instruction)
	exit(1)

def noSTDLError():
	print("Environment variable not set: PL_STDL_PATH")
	exit(1)