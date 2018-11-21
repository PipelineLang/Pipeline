import sys

# Local imports
import errors as errors
import execution as execution

__version__ = "0.1rc1"
pyversion = str(float(sys.version_info[0] + sys.version_info[1]) / 10)

if (sys.argv) == 1:
    print("Pipeline "+ __version__ + " Interpreter")
    print("Running on Python "+ pyversion)
    print("Sorry. The interactive mode is not yet implemented")

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
    output = []
    unparsed_output = []
    # Append the instruction
    unparsed_output.append(line.split(" ")[0])

    # Check if strings have to be delt with
    # For now, crash. TODO: implement strings
    if '"' in line:
        print("Strings not yet implemented")
        exit()
    
    # For now, just add the rest ofo the line
    # This needs to be changed once strings are implemented
    unparsed_output.append(line.split(" ")[1:])

    # Check for syntax errors
    for instruction in unparsed_output:
        i = 0
        for char in instruction:
            if char == ",":
                if i != (len(instruction) - 1):
                    errors.syntaxError(instruction, line_number)
            i += 1

        if instruction[len(instruction) - 1] == ",":
            output.append(instruction[:-1])
        else:
            output.append(instruction)
    
    # Append the line to the main code
    code.append(output)

    # Increment the line counter
    line_number += 1

# Execute the program
line_number = 1
for line in code:
    execution.run(line, line_number)
    line_number += 1
