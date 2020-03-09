
from question import Question

question_prompts = [
    "what color are apples?\n (a) Red/Green\n (b) Purple\n (c) orange \n\n",
    "what color are bananas? \n (a) Teal\n (b) Magenta \n (c) Yellow \n\n",
    "what color are strawberries? \n (a) Yellow\n(b) red\n (c) blue\n\n "


]
questions =[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)