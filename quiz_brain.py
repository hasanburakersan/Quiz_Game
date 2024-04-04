class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.questions = q_list
        self.correct_counter = 0


    def next_question(self):
        user_ans= input("Q."+str(self.q_number+1)+" "+self.questions[self.q_number].text+"( True/False? ) ")
        if user_ans.lower()==self.questions[self.q_number].answer.lower():
            self.correct_counter+=1
            print(f"Correct! Your current score is: {self.correct_counter}/{self.q_number+1}\n")
        else:
            print(f"Incorrect! Your current score is: {self.correct_counter}/{self.q_number+1}\n")
        self.q_number +=1

        if self.q_number == len(self.questions):
            print(f"\n\nGame Over. Your final score is {self.correct_counter}/{self.q_number}")