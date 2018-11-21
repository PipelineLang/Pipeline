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
valid_instructions = ["fetch", "put", "+", "-", "*", "/", "run", "cmp", "disp" "import", "export", "nop"]

# Keep track of the types of vars allowed
valid_vars = ["l", "t"]

def run(command, line):
    # Check if an invalid instruction was passed in
    if not command[0] in valid_instructions:
        errors.invalidInstructionError(command, line)
    
    print(command)
