# No shebang in modules

def name_input(prompt):
	while True:
		answer = raw_input(prompt)
		return answer

def int_input(prompt):
	while True:
		answer = raw_input(prompt)
		try:
			answer = int(answer)
			return answer
		except ValueError:
			print("That is not a number. Please try again.")
			
def float_input(prompt):
	while True:
		answer = raw_input(prompt)
		try:
			answer = float(answer)
			return answer
		except ValueError:
			print("That is not a real number. Please try again.")