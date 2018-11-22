import sys

# Local imports
import errors as errors
import execution as execution

__version__ = "0.2rc1"
# Parse the version_info data into a string
pyversion = str(list(sys.version_info)[:-2])[1:-1].strip("'").strip(" ").replace(",", ".").replace(" ", "")

def lineToList(line):
    output = []
    unparsed_output = []
    # Append the instruction
    unparsed_output.append(line.split(" ")[0])

    # Check if strings have to be delt with
    # For now, crash. TODO: implement strings
    # if '"' in line:
    #     print("Strings not yet implemented")
    #     exit()
    
    # For now, just add the rest ofo the line
    # This needs to be changed once strings are implemented
    for item in line.split(" ")[1:]:
    	unparsed_output.append(item)

    # Check for syntax errors
    for instruction in unparsed_output:
        i = 0
        for char in instruction:
            if char == "," and instruction[0] != '"':
                if i != (len(instruction) - 1):
                    errors.syntaxError(instruction, line_number)
            i += 1
        if instruction[0] == '"':
        	instruction = instruction.replace("_", " ").replace('"', "")
        
        if instruction[len(instruction) - 1] == ",":
            output.append(instruction[:-1])
        else:
            output.append(instruction)
    
    return output

if len(sys.argv) == 1:
	print("Pipeline "+ __version__ + " Interpreter")
	print("Running on Python "+ pyversion)
	line_number = 1
	while True:
		# get line from cli
		inp = input(">>")
		
		# deal with edge cases
		if inp == "exit":
			print("Goodbye!")
			break
		if inp == "":
			continue
		
		# format the line
		inp = lineToList(inp)
		# execute the line
		execution.run(inp, line_number, sys.argv[2:])
		line_number += 1
	exit(0)

# Load the file
try:
    with open(sys.argv[1], "r") as f:
        infile = f.read()
        f.close()
except:
    # Print an error message an exit
    errors.fileLoadError(sys.argv[1])

# Parse through the file
code = []
line_number = 1
for line in infile.split("\n"):
    # Skip blank lines
    if line == "":
        continue
	
    output = lineToList(line)
    
    # Append the line to the main code
    code.append(output)

    # Increment the line counter
    line_number += 1

# Execute the program
line_number = 1
for line in code:
    execution.run(line, line_number, sys.argv[2:])
    line_number += 1
