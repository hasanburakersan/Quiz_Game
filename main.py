from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
q_bank=[]
for questions in question_data:
    q_bank.append(
        Questions(questions["text"],questions["answer"])
    )

quiz_brain= QuizBrain(q_bank)
for q in range(len(question_data)):
    quiz_brain.next_question()