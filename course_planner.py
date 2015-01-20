import json

courses_taken = []
json_file = open('courses.json', 'r')
course_data_file = open('course_data.json', 'r')

data = json.load(json_file)
course_data = json.load(course_data_file)

def add(course):
	courses_taken.append(course)
	for courses in data["Prerequisites"]:
		if course in courses.split('/'):
			data["Prerequisites"][courses] = True

def check(course):
	# do something
	print("")

def run():
	running = True
	while running:
		func = input("Prompt (type 'help' for more information): ")
		if func == "exit":
			running = False
		elif func == "help":
			print("add ABC: add ABC to list of classes taken")
			print("check: print out list of classes taken")
			print("exit: leave the program")
		elif func == "check":
			print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
		else:
			func_split = func.split()
			if func_split[0] == "add":
				add(func_split[1] + " " + func_split[2])
			else:
				print("Invalid input")

run()
