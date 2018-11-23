import collections
import ast
import string

# Local imports
import errors as errors

# Create the pipe
pipe = collections.deque([])

# Keep track of allowed instructions
# This list is ordered in a way that slightly cuts down on search time
valid_instructions = ["rem", "put", "add", "sub", "mul", "div", "cmp", "disp", "import", "export", "nop", "ncmp", "hold", "rls"]
exceptions = ["#", "::"]

# Make a place to put the "held" value
hvar = 0

# Instruction map is at the bottom of the file

def run(command, line, args):
    # Check if an invalid instruction was passed in
    if not command[0] in valid_instructions and command[0] not in exceptions:
        errors.invalidInstructionError(command, line)
    
    # Run the instruction
    instruction_map[command[0]](command, args)

def checkPipe(instruction, needed):
	if len(pipe) < needed:
		errors.pipeTooSmallError(instruction)

def fixType(data):
	if type(data) == type(1.00):
		if data.is_integer():
			return int(data)
	if type(data) != type(""):
		return data
	if data == "True" or data == "False":
		return bool(data)
	for char in data:
		if char in string.ascii_lowercase:
			return ast.literal_eval('"'+str(data)+'"')
	return float(data)
# The actual instructions
def rem(line, args):
	checkPipe("rem", 1)
	pipe.pop()

def put(line, args):
	pipe.append(fixType(line[1]))

def add(line, args):
	checkPipe("add", 2)
	val1 = pipe.pop()
	val2 = pipe.pop()
	pipe.append(val2)
	pipe.append(val1)
	try:
		pipe.append(val1 + val2)
	except:
		errors.unknown(line)

def sub(line, args):
	checkPipe("sub", 2)
	val1 = pipe.pop()
	val2 = pipe.pop()
	pipe.append(val2)
	pipe.append(val1)
	try:
		pipe.append(val1 - val2)
	except:
		errors.unknown(line)

def mul(line, args):
	checkPipe("mul", 2)
	val1 = pipe.pop()
	val2 = pipe.pop()
	pipe.append(val2)
	pipe.append(val1)
	try:
		pipe.append(val1 * val2)
	except:
		errors.unknown(line)

def div(line, args):
	checkPipe("div", 2)
	val1 = pipe.pop()
	val2 = pipe.pop()
	pipe.append(val2)
	pipe.append(val1)
	try:
		pipe.append(val1 / val2)
	except:
		errors.unknown(line)

def import_command(line, args):
	num = int(line[1])
	i = 0
	while i < num:
		pipe.append(fixType(args[i]))
		i += 1

def export(line, args):
	checkPipe("export", 1)
	exit(fixType(pipe.pop()))

def disp(line, args):
	checkPipe("disp", 1)
	val = pipe.pop()
	print(val)
	pipe.append(val)

def nop(line, args):
	return

def cmp_command(line, args):
	command = line[2:]
	checkPipe("cmp", 2)
	val1 = fixType(pipe.pop())
	val2 = fixType(pipe.pop())
	pipe.append(val2)
	pipe.append(val1)
	if val1 == val2:
		run(command, 0, [])

def ncmp(line, args):
	command = line[2:]
	checkPipe("cmp", 2)
	val1 = fixType(pipe.pop())
	val2 = fixType(pipe.pop())
	pipe.append(val2)
	pipe.append(val1)
	if val1 != val2:
		run(command, 0, [])

def hold(line, args):
	hvar = pipe.pop()

def rls(line, args):
	pipe.append(hvar)
	


# Map each instruction to a function
instruction_map = {
	"rem":rem,
	"put":put,
	"add":add,
	"sub":sub,
	"mul":mul,
	"div":div,
	"import":import_command,
	"export":export,
	"disp":disp,
	"nop":nop,
	"cmp":cmp_command,
	"ncmp":ncmp,
	"hold":hold,
	"rls":rls
}