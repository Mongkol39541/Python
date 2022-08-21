class Controller:
    def __init__(self, data):
        self.question_list = data
        self.question_number = 0
        self.score = 0
        self.current = None

    # ไปยังข้อถัดไป
    def nextQuestion(self):
        self.current = self.question_list[self.question_number]
        self.question_number += 1
        return f"{self.question_number} ) {self.current.text}"

    def hasQuestion(self):
        return self.question_number < len(self.question_list)

    def checkAnswer(self, userInput):
        currect_answer = self.current.answer
        if userInput.lower() == currect_answer.lower():
            # ได้รับคะแนน
            self.score += 1
            return True
        else:
            return False
