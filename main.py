import random
from js import document

question_div = document.querySelector("#question")
feedback_div = document.querySelector("#feedback")
results_div = document.querySelector("#results")
submit_btn = document.querySelector("#submit")
answer_input = document.querySelector("#answer")

score = 0
total = 3
current = 0
x = y = correct_answer = None

def new_question():
    global x, y, correct_answer, current
    if current >= total:
        results_div.innerText = f"Game over! You got {score}/{total} correct."
        question_div.innerText = ""
        submit_btn.disabled = True
        return

    x = random.randint(1, 10)
    y = random.randint(1, 10)
    correct_answer = x * y
    current += 1
    question_div.innerText = f"Question {current}: What is {x} × {y}?"
    feedback_div.innerText = ""
    answer_input.value = ""

def check_answer(event):
    global score
    try:
        user_answer = int(answer_input.value)
    except ValueError:
        feedback_div.innerText = "Please enter a number."
        return

    if user_answer == correct_answer:
        feedback_div.innerText = "✅ Correct!"
        score += 1
    else:
        feedback_div.innerText = f"❌ Wrong. The correct answer was {correct_answer}."
    new_question()

submit_btn.addEventListener("click", check_answer)
new_question()
