
def ask_question(q_num, question_data):
    print(f"\nQuestion {q_num}: {question_data['question']}")
    for option in ['a', 'b', 'c', 'd']:
        print(f"{option}) {question_data['options'][option]}")
    answer = input("Your answer (a/b/c/d): ").lower()
    
    if answer == question_data['answer']:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer is '{question_data['answer']}'")
        return False

def run_quiz(questions):
    print("🧪 Welcome to the Python Quiz Game!")
    score = 0
    for i, q in enumerate(questions, 1):
        if ask_question(i, q):
            score += 1
    print(f"\n🎯 Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You're a Python Pro!")
    elif score >= len(questions) * 0.7:
        print("🎉 Great job!")
    elif score >= len(questions) * 0.5:
        print("👍 Good effort! Keep learning.")
    else:
        print("📘 Keep practicing. You'll get better!")

# 20 Python Interview Questions
quiz_questions = [
    {
        'question': "A while loop must always have what to avoid an infinite loop ?",
        'options': {
            'a': "A print statement",
            'b': "A way to update the condition",
            'c': "A return statement",
            'd': "No specific requirement"
        },
        'answer': 'b'
    },
    {
        'question': "In a nested loop, what happens when a break is executed in the inner loop?",
        'options': {
            'a': "Both loops terminate",
            'b': "Only the inner loop terminates",
            'c': "The outer loop skips an iteration",
            'd': "The program crashes"
        },
        'answer': 'b'
    },
    {
        'question': "What will the output be? x = [1, 2, 3] y = [1, 2, 3] print(x is y)",
        'options': {
            'a': "True",
            'b': "False",
            'c': "None",
            'd': "Error"
        },
        'answer': 'b'
    },
    {
        'question': "What is the output of bool(0)?",
        'options': {
            'a': "True",
            'b': "False",
            'c': "0",
            'd': "Error"
        },
        'answer': 'b'
    },
    {
        'question': "Which operator is used to concatenate strings?",
        'options': {
            'a': "+",
            'b': "*",
            'c': "&",
            'd': "."
        },
        'answer': 'a'
    },
    {
        'question': "Find the result of 12 | 5 ?",
        'options': {
            'a': "7",
            'b': "15",
            'c': "13",
            'd': "5"
        },
        'answer': 'c'
    },
    {
        'question': "what is output of the given code: print(bool(0.0)) ?",
        'options': {
            'a': "True",
            'b': "Error",
            'c': "NOne",
            'd': "Flase"
        },
        'answer': 'd'
    },
    {
        'question': "Which of the following updates a variable using exponentiation?",
        'options': {
            'a': "^=",
            'b': "*=",
            'c': "**=",
            'd': "=="
        },
        'answer': 'c'
    },
    {
        'question': "Which of the following functions is used to transform all elements in an iterable?",
        'options': {
            'a': "map()",
            'b': "filter()",
            'c': "sum()",
            'd': "count()"
        },
        'answer': 'a'
    },
    {
        'question': "Recursive function must always move towards?",
        'options': {
            'a': "Infinite loop",
            'b': "Input validation",
            'c': "Function cal",
            'd': "Base case"
        },
        'answer': 'd'
    },
    {
        'question': "Is tuple passed by reference?",
        'options': {
            'a': "Yes",
            'b': "No",
            'c': "Depends on size",
            'd': "Depends on value"
        },
        'answer': 'a'
    },
    {
        'question': "Which function should be used to selectively keep items in a sequence?",
        'options': {
            'a': "map()",
            'b': "filter()",
            'c': "reduce()",
            'd': "all()"
        },
        'answer': 'b'
    },
    {
        'question': "Pass by reference helps in ?",
        'options': {
            'a': "Creating new variable",
            'b': "Importing module",
            'c': "Modifying original data",
            'd': "Calling class"
        },
        'answer': 'c'
    },
    {
        'question': "What will `lambda x: x * 2` return when called with `3`?",
        'options': {
            'a': "3",
            'b': "6",
            'c': "9",
            'd': "None"
        },
        'answer': 'b'
    },
    {
        'question': "What is the result of `lambda x: x.upper()` when called with `'hello'`?",
        'options': {
            'a': "hELLO",
            'b': "HELLO",
            'c': "HELLO",
            'd': "helloupper"
        },
        'answer': 'c'
    },
    {
        'question': "What does `lambda x=3: x*2` return when called without arguments?",
        'options': {
            'a': "6",
            'b': "Error",
            'c': "None",
            'd': "3"
        },
        'answer': 'a'
    },
    {
        'question': "Which function returns only the elements that satisfy a condition?",
        'options': {
            'a': "map()",
            'b': "reduce()",
            'c': "zip()",
            'd': "filter()"
        },
        'answer': 'd'
    },
    {
        'question': "In a nested loop, what happens when a break is executed in the inner loop?",
        'options': {
            'a': "Both loops terminate",
            'b': "Only the inner loop terminates",
            'c': "The outer loop skips an iteration",
            'd': "The program crashes"
        },
        'answer': 'b'
    },
    {
        'question': "What is the minimum number of times a while loop executes?",
        'options': {
            'a': "0",
            'b': "1",
            'c': "Depends on input",
            'd': "Infinite"
        },
        'answer': 'a'
    },
    {
        'question': "When is a break statement typically used?",
        'options': {
            'a': "To repeat a loop",
            'b': " To skip an iteration",
            'c': "To exit a loop when a condition is met",
            'd': "o pause execution"
        },
        'answer': 'c'
    }
]

# Run the game
if __name__ == "__main__":
    run_quiz(quiz_questions)

'''
Question 1: A while loop must always have what to avoid an infinite loop ?
a) A print statement
b) A way to update the condition
c) A return statement
d) No specific requirement
Your answer (a/b/c/d): b
✅ Correct!

Question 2: In a nested loop, what happens when a break is executed in the inner loop?
a) Both loops terminate
b) Only the inner loop terminates
c) The outer loop skips an iteration
d) The program crashes
Your answer (a/b/c/d): c
❌ Wrong! The correct answer is 'b'

Question 3: What will the output be? x = [1, 2, 3] y = [1, 2, 3] print(x is y)
a) True
b) False
c) None
d) Error
Your answer (a/b/c/d): b
✅ Correct!

Question 4: What is the output of bool(0)?
a) True
b) False
c) 0
d) Error
Your answer (a/b/c/d): b
✅ Correct!

Question 5: Which operator is used to concatenate strings?
a) +
b) *
c) &
d) .
Your answer (a/b/c/d): a
✅ Correct!

Question 6: Find the result of 12 | 5 ?
a) 7
b) 15
c) 13
d) 5
Your answer (a/b/c/d): b
❌ Wrong! The correct answer is 'c'

Question 7: what is output of the given code: print(bool(0.0)) ?
a) True
b) Error
c) NOne
d) Flase
Your answer (a/b/c/d): d
✅ Correct!

Question 8: Which of the following updates a variable using exponentiation?
a) ^=
b) *=
c) **=
d) ==
Your answer (a/b/c/d): c
✅ Correct!

Question 9: Which of the following functions is used to transform all elements in an iterable?
a) map()
b) filter()
c) sum()
d) count()
Your answer (a/b/c/d): a
✅ Correct!

Question 10: Recursive function must always move towards?
a) Infinite loop
b) Input validation
c) Function cal
d) Base case
Your answer (a/b/c/d): d
✅ Correct!

Question 11: Is tuple passed by reference?
a) Yes
b) No
c) Depends on size
d) Depends on value
Your answer (a/b/c/d): a
✅ Correct!

Question 12: Which function should be used to selectively keep items in a sequence?
a) map()
b) filter()
c) reduce()
d) all()
Your answer (a/b/c/d): b
✅ Correct!

Question 13: Pass by reference helps in ?
a) Creating new variable
b) Importing module
c) Modifying original data
d) Calling class
Your answer (a/b/c/d): c
✅ Correct!

Question 14: What will `lambda x: x * 2` return when called with `3`?
a) 3
b) 6
c) 9
d) None
Your answer (a/b/c/d): b
✅ Correct!

Question 15: What is the result of `lambda x: x.upper()` when called with `'hello'`?
a) hELLO
b) HELLO
c) HELLO
d) helloupper
Your answer (a/b/c/d): c
✅ Correct!

Question 16: What does `lambda x=3: x*2` return when called without arguments?
a) 6
b) Error
c) None
d) 3
Your answer (a/b/c/d): a
✅ Correct!

Question 17: Which function returns only the elements that satisfy a condition?
a) map()
b) reduce()
c) zip()
d) filter()
Your answer (a/b/c/d): d
✅ Correct!

Question 18: In a nested loop, what happens when a break is executed in the inner loop?
a) Both loops terminate
b) Only the inner loop terminates
c) The outer loop skips an iteration
d) The program crashes
Your answer (a/b/c/d): b
✅ Correct!

Question 19: What is the minimum number of times a while loop executes?
a) 0
b) 1
c) Depends on input
d) Infinite
Your answer (a/b/c/d): c
❌ Wrong! The correct answer is 'a'

Question 20: When is a break statement typically used?
a) To repeat a loop
b)  To skip an iteration
c) To exit a loop when a condition is met
d) o pause execution
Your answer (a/b/c/d): c
✅ Correct!

🎯 Your Final Score: 17/20
🎉 Great job!'''