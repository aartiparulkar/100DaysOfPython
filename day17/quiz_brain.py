from question_model import Question


class QuizBrain:
    """Implements the functionality of a quiz"""
    def __init__(self, q_list:list[Question]):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0
        
    def questions_left(self):
        """Returns True if question bank still has questions left, False otherwise."""
        return self.question_no < len(self.question_list)

    def ask_question(self):
        """Asks the user a question."""
        question = self.question_list[self.question_no] 
        self.question_no += 1      
        user_answer = input(f"Q.{self.question_no}. {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)
        
    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            self.score += 1
            print("You got is right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {actual_answer}.")
        print(f"Your current score is: {self.score}/{self.question_no}\n")
        