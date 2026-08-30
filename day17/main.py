from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    text = item["question"]
    answer = item["correct_answer"]
    question_bank.append(Question(text, answer))
    
quiz = QuizBrain(question_bank)
quiz.ask_question()

while quiz.questions_left():
    quiz.ask_question()

print("You completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
