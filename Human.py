class Human:
    def __init__(self, name):
        self.name = name
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю. nhevgfgegfgev блин че такое')
    
class Student(Human):
    def ask_question(self, someone, question):
        
        print(f'{someone.name}, {question}')
        someone.answer_question(question) # если сюда добавить return, то будет работать как функция 
                                          #и перейдет на функцию другого класса без исполнения print()
        print()
          
class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
             super().answer_question(question)
        
class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)

class CodeReviewer(Human):
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)
   
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
