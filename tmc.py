import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
  left = random.randint(MIN_OPERAND, MAX_OPERAND)
  right = random.randint(MIN_OPERAND, MAX_OPERAND)
  operator = random.choice(OPERATORS)
  expr = str(left) + " " + operator + " " + str(right)
  answer = eval(expr)
  return expr, answer

wrong = 0
input("Press Enter to start the test...")
print("---------------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
  problem, solution = generate_problem()
  while True:
    guess = input(f"Problem {i + 1}: {problem} = ")
    if guess == str(solution):
      break
    wrong += 1

end_time = time.time()
elapsed_time = round(end_time - start_time, 2)

print("---------------------------------")
print("Nice Work! You have completed the test in ", elapsed_time, "seconds.")