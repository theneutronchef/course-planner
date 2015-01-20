import json

courses_taken = []
json_file = open('courses.json', 'r')
course_data_file = open('course_data.json', 'r')

data = json.load(json_file)
course_data = json.load(course_data_file)

def add(course):
	# course = major + " " + course_number
	in_major = False
	for courses in data["Prerequisites"]:
		if course in courses.split('/'):
			data["Prerequisites"][courses] = True
			in_major = True
	for requirement in data["Upper Div Requirements"]:
		if course in course_data[requirement]:
			data["Upper Div Requirements"][requirement] = True
			data["Upper Division Units"] = data["Upper Division Units"] + 4
			data["Upper Division Classes"] = data["Upper Division Classes"] + 1
			in_major = True
	if in_major:
		courses_taken.append(course)
	else:
		print("Class not in CogSci syllabus")


def check():
	for courses in data["Prerequisites"]:
		if data["Prerequisites"][courses] == False:
			return False
	for requirement in data["Upper Div Requirements"]:
		if data["Upper Div Requirements"][requirement] == False:
			return False
	if data["Upper Division Units"] < 30 or data["Upper Division Classes"] < 9:
		return False
	return True

def pretty_print(l):
	for elem in l:
		print(elem)

def run():
	running = True
	while running:
		func = input("Prompt (type 'help' for more information): ")
		if func == "exit":
			running = False
		elif func == "help":
			print("add 'Department' 'Course Number': add class and updates checklist")
			print("check: print out list of requirements fulfilled")
			print("classes: print out list of classes taken")
			print("list 'Requirement': list classes that can fulfil the given requirement")
			print("exit: leave the program")
		elif func == "check":
			print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
			if check():
				print("You are done with all requirements!")
			else:
				print("You are not done with all requirements")
		elif func == "classes":
			pretty_print(courses_taken)
		else:
			func_split = func.partition(" ")
			if func_split[0] == "add":
				add(func_split[2])
				# print("Please use the correct format: add 'Department' 'Course Number'")
			elif func_split[0] == "list":
				if func_split[2] in course_data:
					pretty_print(course_data[func_split[2]])
				else:
					print("Please use the correct format: list 'Requirement'")
			else:
				print("Invalid input")

run()
