import json

courses_taken = []
json_file = open('courses.json', 'r')
course_data_file = open('course_data.json', 'r')

data = json.load(json_file)
course_data = json.load(course_data_file)

def add(major, course_number):
	course = major + " " + course_number
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
	# do something
	print("")

def run():
	running = True
	while running:
		func = input("Prompt (type 'help' for more information): ")
		if func == "exit":
			running = False
		elif func == "help":
			print("add 'Department' 'Course Number': add class and updates checklist")
			print("check: print out list of classes taken")
			print("exit: leave the program")
		elif func == "check":
			print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
		elif func == "list":
			print(courses_taken)
		else:
			func_split = func.split()
			if func_split[0] == "add":
				if len(func_split) == 3:
					add(func_split[1], func_split[2])
				else:
					print("Please use the correct format: add 'Department' 'Course Number'")

			else:
				print("Invalid input")

run()
