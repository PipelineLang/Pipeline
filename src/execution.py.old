import collections

# Local imports
import errors as errors

# Create the pipe
pipe = collections.deque([])

# Note: For the vars defined below, the first element has no use. They just save the translation between starting at 1 and 0

# Create the temp vars
temp = ["Temp",0,0,0,0,0,0,0,0,0,0]

# Create the location vars
locations = ["Locations",0,0,0,0,0,0,0,0,0,0]

# Keep track of allowed instructions
# This list is ordered in a way that slightly cuts down on search time
valid_instructions = ["fetch", "put", "add", "sub", "mul", "div", "run", "cmp", "disp", "import", "export", "nop"]
exceptions = [":", "<"]

# Keep track of the types of vars allowed
valid_vars = ["l", "t"]

# Instruction map is at the bottom of the file

def run(command, line, args):
    # Check if an invalid instruction was passed in
    if not command[0] in valid_instructions and command[0][0] not in exceptions:
        errors.invalidInstructionError(command, line)
    
    # Run the instruction
    instruction_map[command[0]](command, args)

# The actual instructions
def fetch(line, _):
	try:
		value = pipe.pop()
	except:
		errors.emptyPipeError(line)
	
	# Put the value in its location
	if line[1][0] != "t":
		errors.invalidLocationError(line[1][0])
	
	try:
		temp[int(line[1][1:])] = value
	except:
		errors.invalidTempSlot(line[1])
		

def put(line, _):
	if line[1][0] == "t":
		pipe.append(temp[int(line[1][1:])])
	else:
		try:
			pipe.append(eval(line[1]))
		except:
			errors.unknown(line)

def add(line, _):
	if type(line[1]) != type("") and type(line[2]) != type(""):
		pipe.append(eval(line[1]) + eval(line[2]))
	else:
		
		try:
			v1 = temp[int(line[1][1:])]
		except:
			errors.invalidTempSlot(line[1])
		try:
			v2 = temp[int(line[2][1:])]
		except:
			errors.invalidTempSlot(line[2])
		pipe.append(v1 + v2)

def sub(line, _):
	if type(line[1]) != type("") and type(line[2]) != type(""):
		pipe.append(eval(line[1]) - eval(line[2]))
	else:
		try:
			v1 = temp[int(line[1][1:])]
		except:
			errors.invalidTempSlot(line[1])
		try:
			v2 = temp[int(line[2][1:])]
		except:
			errors.invalidTempSlot(line[2])
		pipe.append(v1 - v2)
	
def mul(line, _):
	if type(line[1]) != type("") and type(line[2]) != type(""):
		pipe.append(eval(line[1]) * eval(line[2]))
	else:
		try:
			v1 = temp[int(line[1][1:])]
		except:
			errors.invalidTempSlot(line[1])
		try:
			v2 = temp[int(line[2][1:])]
		except:
			errors.invalidTempSlot(line[2])
		pipe.append(v1 * v2)
	
def div(line, _):
	if type(line[1]) != type("") and type(line[2]) != type(""):
		pipe.append(eval(line[1]) / eval(line[2]))
	else:
		try:
			v1 = temp[int(line[1][1:])]
		except:
			errors.invalidTempSlot(line[1])
		try:
			v2 = temp[int(line[2][1:])]
		except:
			errors.invalidTempSlot(line[2])
		pipe.append(v1 / v2)

def import_command(line, args):
	num = int(line[1])
	i = 0
	while i < num:
		pipe.append(eval(args[i]))
		i += 1

def export(line, _):
	try:
		value = pipe.pop()
	except:
		errors.emptyPipeError(line)
	exit(value)

def disp(line, _):
	if len(line) == 1:
		value = pipe.pop()
		print(value)
		pipe.append(value)
		
	else:
		print(line[1])

def nop(line, _):
	return

def cmp_command(line, _ ):
	half1 = []
	half2 = []
	
	latch = False
	for item in line:
		if item == ":":
			latch = True
		
		if latch:
			half2.append(item)
		else:
			half1.append(item)
	
	compare = half1[2] if type(half1) != type("") else temp[int(half1[2][1:])]
	if temp[int(half1[1][1:])] == eval(compare):
		run(half2[1:],0, [None])




# Map each instruction to a function
instruction_map = {
	"fetch":fetch,
	"put":put,
	"add":add,
	"sub":sub,
	"mul":mul,
	"div":div,
	"import":import_command,
	"export":export,
	"disp":disp,
	"nop":nop,
	"cmp":cmp_command
}