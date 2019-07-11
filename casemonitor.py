import random
import json

'''
intro message
'''
def displayStartMenu(selection):
	print("welcome to the case monitoring portal")

'''
displays the command help
'''
def help():
	print("help info")
	print("assign name casenumber : assigns an agent a case")
	print("list : debug function displays list of agents and cases")
	print("listcsms : lists active csms")
	print("add name maxcases isonbreakorlunch : adds a new agent")
	print("update name numbertoincrement : debug function increments the count of cases by a csm by the amount specified")
	print("autoassign casenumber : assigns a case to a random csm")
	print("activecases : lists active cases")
	print("cls or clear : clears the screen")
	print("read : reads data from the csm.txt file")
	print("write : writes data to the csm.txt file")
	print("help : displays this menu")
	print("exit : exits the program")

def printCSM(name, currentcases, maxcases, onbreak):
	#convention for CSMs
	# name | amountcurrentcases | amountmaxcases | breakstatus | shift | append case numbers here
	printstring = ""
	maxnamespace = 20
	maxcasespace = 9
	maxmaxspace = 7
	maxbreakspace = 9
	namestring = str(name)
	currentcasestring = str(currentcases)
	maxcasestring = str(maxcases)
	onbreakstring = str(onbreak)
	namespace = maxnamespace - len(namestring)
	casespace = maxcasespace - len(currentcasestring)
	maxspace = maxmaxspace - len(maxcasestring)
	onbreakspace = maxbreakspace - len(onbreakstring)
	padding = ""
	for i in range(namespace):
		padding = padding + " "
	printstring += namestring + padding
	padding = ""
	for i in range(casespace):
		padding = padding + " "
	printstring += "|" + currentcasestring + padding
	padding = ""
	for i in range(maxspace):
		padding = padding + " "
	printstring += "|" + maxcasestring + padding
	padding = ""
	for i in range(onbreakspace):
		padding = padding + " "
	printstring += "|" + onbreakstring + padding
	return printstring

'''
displays the current list of csms
will add pretty printing later
'''
def displayActive(list_of_csms):

	print("------------List of Active CSMs-----------------")
	print("--Name--------------|--Cases--|--Max--|--BR\LU--")
	for i in range(0, len(list_of_csms)):
		print(printCSM(list_of_csms[i][0], list_of_csms[i][1], list_of_csms[i][2], list_of_csms[i][3]))

def displayGameUI():
	print("----------UI debug-------------")

'''
updates the number of cases held by the given CSM
checks if the csm exists
does not check against maximum cases
'''
def updateCSMcases(name, case_increment, list_of_csms):
	print("debug updating")#debug
	for i in range(0, len(list_of_csms)):
		if str(list_of_csms[i][0]) == str(name):
			print("before")
			print(list_of_csms[i])#debug
			list_of_csms[i] = (str(name), list_of_csms[i][1] + case_increment, list_of_csms[i][2], list_of_csms[i][3])
			print("after")
			print(list_of_csms[i])#debug

'''
assigns a case and name to the list of cases
will need to check to see if the case is currently assigned, and prompt to change assignment before doing it
if the case is currently assigned to the same person you are assigning it to
if the case is being assigned to someone who doesnt exist
if the case you are assigning is being assigned to someone who is full of cases
'''
def assign(csmName, caseNumber, list_of_csms, list_of_cases):
	print("debug assigning")#debug
	csmfound = 0
	casealreadyassigned = 0
	for i in range(0, len(list_of_cases)):
		if list_of_cases[i][0] == caseNumber:
			print("case is already assigned to " + list_of_cases[i][1])
			casealreadyassigned = 1
	if casealreadyassigned == 0:
		for i in range(0, len(list_of_csms)):
			if str(list_of_csms[i][0]) == csmName:
				csmfound = 1
				print("debug csmname: " + str(list_of_csms[i][0]))
				if list_of_csms[i][1] < list_of_csms[i][2]:
					list_of_cases.append((caseNumber, csmName))
					list_of_csms[i] = (list_of_csms[i][0], list_of_csms[i][1] + 1, list_of_csms[i][2], list_of_csms[i][3])
					csmfound = 1
					print("csm found")
				else:
					print("csm at max capacity")
	if csmfound == 0:
		print("csm not found")
	print("debug csmfound: " + str(csmfound) + " csmName: " + str(csmName) + " casealreadyassigned: " + str(casealreadyassigned))

'''
adds a csm to the list of csms
needs to check if the csm is already in the list
'''
def addCSM(csmName, maxCases, onBreak, list_of_csms):
	print("debug adding") # debug
	csmexists = 0
	for i in range(0, len(list_of_csms)):
		if csmName == list_of_csms[i][0]:
			csmexists = 1
	if csmexists == 0:
		list_of_csms.append((csmName, 0, int(maxCases), onBreak))
		print("added ", csmName)

'''
writes the current list of csms to a file which can be shared or restored from
'''
def writeCSMs(list_of_csms):
	#f = open('csms.txt', 'w')
	data = {}
	data['csm'] = []
	data['csm'].append({
		'name': 'Alice',
		'currentcases': '0',
		'maxcases': '4',
		'onbreak': 'False'
	})
	print("write completed")
	print(data)

def parsedata(rawdata):
	csmname = ""
	currentcases = ""
	maxcases = ""
	onbreak = ""

	return (csmname, currentcases, maxcases, onbreak)

def readCSMs():
	f = open('csms.txt', 'r')
	raw_data = ""
	for line in f:
		print(line)
		raw_data = parsedata(line)
		print(raw_data)
		raw_data = ""
	f.close()

def main():
	#main loop
	done = False
	clicked = 0
	selection = 0
	state = "starting"
	list_of_csms = []
	#list_of_csms = [("larry", 0, 4, True), ("bob", 0, 4, False), ("joe", 2, 4, True), ("mark", 1, 5, False), ("mary", 0, 3, False), ("jules", 3, 4, False), ("alice", 2, 4, False), ]#debug
	list_of_cases = []
	#list_of_cases = [('00000000', 'joe'), ('9999999', 'joe'), ('9898898', 'mark'), ('87878787', 'jules'), ('83838383', 'jules'), ('858585858', 'jules'), ('45444554', 'alice'), ('333344445', 'alice')]#debug
	#displayActive(list_of_csms)
	
	while not done:
		#wipe screen
		#handlestates
		if state == "closing":
			done = True
			print("closing")
		elif state == "starting":
			displayStartMenu(selection)
			args = input("> ")
			argu = args.split(" ")
			print(argu)
			if argu[0] == "run":
				state = "running"
			elif argu[0] == "exit":
				state = "closing"
			elif argu[0] == "help":
				print("enter run to start or exit to exit")
			else:
				pass #invalid input
		elif state == "running":
			#displayActive(list_of_csms)
			rawinput = input(">")
			args = rawinput.split(" ")
			#print(args)#debug
			if args[0] == "exit":
				state = "closing"
			if args[0] == "update":
				if len(args) == 3:
					updatename = str(args[1])
					updateCSMcases(updatename, int(args[2]), list_of_csms)
				else:
					print("invalid args")
			if args[0] == "list":
				displayActive(list_of_csms)
				#print(str(len(list_of_csms)))
				#print(list_of_cases)
			if args[0] == "add":
				if len(args) == 4:
					if args[3] == "True":
						onbreak = True
					else:
						onbreak = False
					addCSM(args[1], args[2], onbreak, list_of_csms)
				else:
					print("invalid number of args")
			if args[0] == "assign":
				if len(args) == 3:
					assign(str(args[1]), str(args[2]), list_of_csms, list_of_cases)
				else:
					print("invalid number of arguments")
			if args[0] == "autoassign":
				if len(args) == 2:
					luckycsm = random.randint(0, (len(list_of_csms) - 1))
					print("lucky csm is: " + str(luckycsm))
					assign(list_of_csms[luckycsm][0], args[1], list_of_csms, list_of_cases)	
			if args[0] == "activecases":
				padding = ""
				maxpad = 23
				print("       active cases")
				print("#################################")
				print("SR#                    Name")
				for i in range(0, len(list_of_cases)):
					#print("test")#debug
					numberstring = str(list_of_cases[i][0])
					namestring = str(list_of_cases[i][1])
					topad = maxpad - len(str(list_of_cases[i][0]))
					if topad < 0:
						topad = 1
					for i in range(topad):
						padding = padding + " "
					print(numberstring + padding + namestring)
					padding = ""
			if args[0] == "listcsms":
				for i in range(0, len(list_of_csms)):
					print(list_of_csms[i][0])
			if args[0] == "help":
				help()
			if args[0] == "cls" or args[0] == "clear":
				for i in range (0, 25):
					print("\r\n")
			if args[0] == "write":
				writeCSMs(list_of_csms)
			if args[0] == "read":
				readCSMs()
		else:
			pass # invalid state

main()
exit()