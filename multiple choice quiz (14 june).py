from questions import question

question_prompt = [
    "what color are apple  \n (a) Red/Green \n (b) purple \n (c) orange \n",
    "what color are banana \n (a) Red/Green \n (b) yellow \n (c) orange \n",
    "what color are orange \n (a) Red/Green \n (b) purple \n (c) orange \n"
]

questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "b"),
    question(question_prompt[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"you got ", score, "/", len(questions), " correct")


run_test(questions)