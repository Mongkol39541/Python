# รันโปรแกรทม
from question import Question
from data import question_data
from controller import Controller
from ui import UserInterface

all_question = []

# กำหนดโจทย์ปัญหา
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = Question(text, answer)
    all_question.append(question )

# สร้างแผนควบคุม
controller = Controller(all_question)
userInterface = UserInterface(controller)
