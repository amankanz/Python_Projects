# Python Quiz Game

questions = (
    "What is Python?: ",
    "How do you print text in Python?: ",
    "How do you declare a variable in Python?: ",
    "What is the difference between a list and a tuple in Python?: ",
    "What is the output of 3**2 in Python?: ",
    "How do you write a conditional statement in Python?: ",
    "How can you create a function in Python?: ",
    "What is a dictionary in Python, and how do you create one?: ",
    "How do you handle exceptions in Python?: ",
    "What is a Python module, and how do you import one?: ",
)

options = (
    ("A. high-level, interpreted programming language", "B. type of snake", "C. database system", "D. web server"),
    ("A. Use the echo() function", "B. Use the print() function", "C. Use the display() function", "D. Use the text() function"),
    ("A. By assigning a value to a name, e.g., x = 10", "B. Using a declaration keyword like var", "C. Using a data type keyword, e.g., int x = 10", "D. Variables are predefined in Python"),
    ("A. Lists are mutable; tuples are immutable", "B. Lists are immutable; tuples are mutable", "C. Lists and tuples are both mutable", "D. Lists and tuples are the same in Python"),
    ("A. 6", "B. 9", "C. 8", "D. 3"),
    ("A. Using a while loop", "B. Using if, elif, and else", "C. Using only if", "D. Using switch-case"),
    ("A. Use the define keyword", "B. Use the def keyword to define a function", "C. Declare a function as func()", "D. Functions do not exist in Python"),
    ("A. A collection of key-value pairs, e.g., {'key': 'value'}", "B. A list of values", "C. A tuple of keys", "D. A library of modules"),
    ("A. Using a for loop", "B. Using try, except, and finally blocks", "C. Using a conditional statement", "D. Errors cannot be handled in Python"),
    ("A. A folder containing images", "B. A file containing Python code; use import to include it", "C. A Python interpreter", "D. A type of variable"),
)



# all_options = [
#     [
#         "A high-level, interpreted programming language",
#         "A type of snake",
#         "A database system",
#         "A web server",
#     ],
#     [
#         "Use the echo() function",
#         "Use the print() function",
#         "Use the display() function",
#         "Use the text() function",
#     ],
#     [
#         "By assigning a value to a name, e.g., x = 10",
#         "Using a declaration keyword like var",
#         "Using a data type keyword, e.g., int x = 10",
#         "Variables are predefined in Python",
#     ],
#     [
#         "Lists are mutable; tuples are immutable",
#         "Lists are immutable; tuples are mutable",
#         "Lists and tuples are both mutable",
#         "Lists and tuples are the same in Python",
#     ],
#     [
#         "6",
#         "9",
#         "8",
#         "3",
#     ],
#     [
#         "Using a while loop",
#         "Using if, elif, and else",
#         "Using only if",
#         "Using switch-case",
#     ],
#     [
#         "Use the define keyword",
#         "Use the def keyword to define a function",
#         "Declare a function as func()",
#         "Functions do not exist in Python",
#     ],
#     [
#         "A collection of key-value pairs, e.g., {'key': 'value'}",
#         "A list of values",
#         "A tuple of keys",
#         "A library of modules",
#     ],
#     [
#         "Using a for loop",
#         "Using try, except, and finally blocks",
#         "Using a conditional statement",
#         "Errors cannot be handled in Python",
#     ],
#     [
#         "A folder containing images",
#         "A file containing Python code; use import to include it",
#         "A Python interpreter",
#         "A type of variable",
#     ],
# ]


correct_answers = (
    "A. high-level, interpreted programming language 🆗",
    "B. Use the print() function 🆗",
    "A. By assigning a value to a name, e.g., x = 10 💯",
    "A. Lists are mutable; tuples are immutable 💯",
    "B. 9",
    "B. Using if, elif, and else 🆗",
    "B. Use the def keyword to define a function 👍",
    "A. A collection of key-value pairs, e.g., {'key': 'value'} 💯",
    "B. Using try, except, and finally blocks 👍",
    "B. A file containing Python code; use import to include it 👍",
)

guesses = [ ]

score = 0
question_num = 0


for question in questions:
    print(f"--------- {questions.index(question) + 1} -------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess in correct_answers[question_num][0]:
        score += 1
        print("CORRECT! 💯")
    else:
        print("INCORRECT 😐❌")
        print(f"{correct_answers[question_num]} is the correct answer!")
    question_num += 1

# for answer in correct_answers:
#     guess = input("Enter a guess (A, B, C, D): ").upper()

#     if guess in correct_answers[0][0]:
#         print(f"{guess} is present! 👍")
#     else:
#         print("NOPE!")
#         print(guess)
#         print(correct_answers[0][0])
#         break


print("------------------------")
print("------  🎉 RESULT 🎉  ------")
print("------------------------")

print("Correct Answers:", end="")
for answer in correct_answers:
    print(answer, end=" ")
print()

print("Guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"YOUR POINTS {score} / {len(questions)}")
print(f"YOUR SCORE IS: {int((score / len(questions))*100)}%")