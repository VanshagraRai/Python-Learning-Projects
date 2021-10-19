from question import Questions
question_prompts = [
    "Which is the tallest tower in the world?\n(a) Eiffel Tower\n(b) UN\n(c) Burj Khalifa\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "Who is the first Prime Minister of India?\n(a) Pt. Nehru\n(b) MK Gandhi\n(c) Narendra Modi\n\n"
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "a")
]


def prompting(questions_given):
    score = 0
    for question in questions_given:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your score is out of " + str(len(questions)) + " = " + str(score))


prompting(questions)
