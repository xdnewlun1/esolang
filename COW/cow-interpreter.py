#Cow Interpreter
#Specify a file and the running loop will begin to work through it
#It can interpret in one of three ways. [None, Space, NL]
# -None: Code is squished IE. "MooMOOOOOmooMoO"
# -Space: Code has a space between each command IE. "Moo MOO OOO moo MoO"
# -NL: Code has a New Line between each command IE. "Moo\n MOO\n moo\n"

import argparse

#debug options
debug_output = False
debug_step = False

#Preinitialize a memory list, with the first block declared.
memory = [0]

#Initialize a memory location variable, declares where to program is in memory. Start at 0
memory_iterator = 0


#Initialize the register, allows for copy paste.
register = "empty"

#moo instruction
def moo(chunk, data):
	#Connected to the MOO command. Will start executing again from the previous MOO command, if none is found do nothing
	#if prev_MOO is not the default value, then return the location in the program of the previous MOO + 1 so the previous MOO is not executed
	orig_chunk = chunk
	if chunk == 0:
		print("FATAL ERROR: moo at beginning of program")
		exit()
	else:
		chunk -= 1 #skip previous command
		level = 1
		while level > 0:
			if chunk == 0:
				break
			chunk -= 1
			if data[chunk] == "moo":
				level += 1
			elif data[chunk] == "MOO":
				level -= 1

		if level != 0:
			print(f"FATAL ERROR: moo at chunk {orig_chunk} has no corresponding MOO. Exiting")
			exit()
		if debug_output:
			print(f"moo Returning {chunk}")
		return chunk
	print("FATAL ERROR: Chunk value not returned properly")
	exit()

#mOo instruction
def mOo():
	#moves the current memory position back one block
	#cannot be < 0
	global memory_iterator
	if memory_iterator > 0:
		memory_iterator -= 1

#moO instruction
def moO():
	#moves the current memory position forward one block
	#no restriction, but need to create a new memory list item if not already created.
	global memory_iterator
	memory_iterator += 1
	while memory_iterator >= len(memory):
		memory.append(0)

#mOO instruction
def mOO(chunk):
	#executed a value dependant upon the value of memory block
	#we will read the memory block, and if it corelates to a 
	#command, execut if not, then exit program.
	command_value = memory[memory_iterator]
	#ensure its a valid command, if fails the check then exit.
	if command_value > 11 or command_value < 0 or command_value == 3:
		print(f"FATAL ERROR: mOO instruction at {chunk} caused an exit.")
		exit()
	else:
		if command_value == 0:
			chunk = moo(chunk, iterable_data)
		elif command_value == 1:
			mOo()
		elif command_value == 2:
			moO()
		elif command_value == 4:
			Moo()
		elif command_value == 5:
			MOo()
		elif command_value == 6:
			MoO()
		elif command_value == 7:
			chunk = MOO(iterable_data, chunk)
		elif command_value == 8:
			OOO()
		elif command_value == 9:
			MMM()
		elif command_value == 10:
			OOM()
		elif command_value == 11:
			oom()
	return chunk

#Moo instruction
def Moo():
	#if current memory is 0 then read in one chr from input
	if memory[memory_iterator] == 0:
		chr_input = ord(input("INPUT 1 CHAR: "))
		if len(chr_input) == 1 and chr_input.isalpha():
			memory[memory_iterator] = ord(chr_input)
		else:
			print("FATAL ERROR: Moo only accepts one char input")
			exit()
	#if current memory is not 0, then read as ASCII and print
	else:
		if debug_output:
			print(f"Pre Print Value: {memory[memory_iterator]}")
		print(chr(memory[memory_iterator]), end="")

#MOo instruction
def MOo():
	#decrement the memory value by 1
	memory[memory_iterator] -= 1

#MoO instruction
def MoO():
	#increment the memory value by 1
	memory[memory_iterator] += 1

#MOO instruction
def MOO(data, chunk):
	#if the current memory block value is 0, then skip next command and resume after the next matching moo command
	if memory[memory_iterator] == 0:
		orig_chunk = chunk
		chunk += 1
		while data[chunk] != "moo":
			if chunk == len(data):
				print(f"FATAL ERROR: Looped MOO instruction at {orig_chunk} never found matching moo. Exiting")
				exit()
			chunk += 1
		return chunk
	else:
		return chunk
	#if the current memory block value is not 0 then continue with the next command.
	#so we dont have to do anything

#OOO instruction
def OOO():
	#Set the current memory block to 0
	memory[memory_iterator] = 0

#MMM instruction
def MMM():
	global register
	#If no value in register (IE "empty") then copy current memory value into register
	#If there is a value (IE not "empty") then paste into the current memory block and clear register
	if register == "empty":
		register = memory[memory_iterator]
	else:
		memory[memory_iterator] = register
		register = "empty"

#OOM instruction
def OOM():
	#print the value of the current memory block to STDOUT as an integer
	print(memory[memory_iterator])

#oom instruction
def oom():
	input_value = input("INTEGER INPUT: ")
	if isinstance(input_value,int):
		memory[memory_iterator] = input_value
	else:
		print("FATAL ERROR: oom Input only accepts integers")
		exit()

def main_loop(data):

	#Checks to ensure good COW
	#If data is not divisible by 3 the syntax is bad
	if len(data) % 3 != 0:
		print("FATAL ERROR: Bad Cow Code; File length not divisible by 3, missing or extra characters found!")
		exit()

	
	#Initialize last 
	#Break code into chunks of 3 characters
	iterable_data = []
	iterable_data = [data[i:i+3] for i in range(0, len(data), 3)]

	#Loop through data, and begin to interpret
	chunk = 0
	while chunk < len(iterable_data):
		#Print debug output if selected by options
		if debug_output:
			print(f"---Instruction: {iterable_data[chunk]} - Chunk #: {chunk}---")
			print(f"--Memory Address: {memory_iterator}--")
			print(f"--Memory: {memory}--")
			print(f"")
		#Based on the programs given function, follow that instruction
		if iterable_data[chunk] == "moo":
			chunk = moo(chunk, iterable_data)
			chunk -= 1
		elif iterable_data[chunk] == "mOo":
			mOo()
		elif iterable_data[chunk] == "moO":
			moO()
		elif iterable_data[chunk] == "mOO":
			chunk = mOO(chunk)
		elif iterable_data[chunk] == "Moo":
			Moo()
		elif iterable_data[chunk] == "MOo":
			MOo()
		elif iterable_data[chunk] == "MoO":
			MoO()
		elif iterable_data[chunk] == "MOO":
			chunk = MOO(iterable_data, chunk)
		elif iterable_data[chunk] == "OOO":
			OOO()
		elif iterable_data[chunk] == "MMM":
			MMM()
		elif iterable_data[chunk] == "OOM":
			OOM()
		elif iterable_data[chunk] == "oom":
			oom()

		#Print output if debug_output enabled
		if debug_output:
			print(f"Next Chunk: {chunk+1}")

		chunk += 1
	
#If a file is passed with no seperator then process to interpret properly
def none_file(file):
	data = ""
	with open(file, 'r') as file:
		data = file.read()

	main_loop(data)

#If a file is passed with space seperator process to interpret properly
def space_file(file):
	data = ""
	with open(file, 'r') as file:
		data = file.read()

	data = data.strip()
	data = data.replace(" ", "")
	
	main_loop(data)

#If a file is passed with new line seperator process to interpret properly
def nl_file(file):
	data = ""
	with open(file, 'r') as file:
		for line in file:
			data = data + line.strip()

	main_loop(data)

#Main function, runs the argument parsing and starts the processing of the .cow file
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Cow Interpreter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("-f", "--file", action="store", help=".cow file to interpret", required=True)
	parser.add_argument("-s", "--seperator", action="store", help="How the code is seperated. Options: None, Space, NewLine", required=True)
	parser.add_argument("-d", "--debug", action="store_true", help="Enable Debug Output; Adds command, and memory output for every instruction.")
	parser.add_argument("-ds", "--stepper", action="store_true", help="Enable stepping mode, requires user to press enter between every instruction.")
	args = parser.parse_args()

	#Set debug options
	debug_output = args.debug
	debug_step = args.stepper

	#Check to make sure .cow file was passed
	if ".cow" not in args.file:
		print("FATAL ERROR: Please specify a .cow file")
		exit()

	#Determine the seperator and start the program
	if args.seperator.lower() == "none":
		none_file(args.file)
	elif args.seperator.lower() == "space":
		space_file(args.file)
	elif args.seperator.lower() == "newline":
		nl_file(args.file)