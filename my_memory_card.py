from PyQt5.QtCore import Qt
from random import shuffle,randint
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,QButtonGroup, QRadioButton, QPushButton, QLabel)
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
Button = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответа')
main_win.resize(800,600)
class Question():
    def __init__(self,quest,right_answer,wrong1,wrong2,wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
main_win.score = 0
main_win.total = 0
question_list = []
question_list.append(Question("Какого цвета нет на Российском флаге?","Чёрного","Синего","Красного","Белого"))
question_list.append(Question("Какого цвета нет на Германском флаге?","Синего","Жёлтого","Красного","Чёрного"))
question_list.append(Question("Какого цвета нет на Великобретанском флаге?","Жёлтого","Синего","Красного","Белого"))
# Варианты ответов
question_1 = QRadioButton('Энцы')
question_2 = QRadioButton('Смурфы')
question_3 = QRadioButton('Чулымцы')
question_4 = QRadioButton('Алеуты')
# Линии верт и гориз
layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

# Приклепление к группе
layout_2.addWidget(question_1)
layout_2.addWidget(question_2)
layout_3.addWidget(question_3)
layout_3.addWidget(question_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RadioGroupBox.setLayout(layout_1)
# Создание группы ответов

RadioGroupBox2 = QGroupBox('Результат ответа:')

layout_otv1 = QVBoxLayout()
 
otvet = QLabel('Правильный/Неправильный')

otvet_my1 = QLabel('Правильно')
# Привязка ответов
layout_otv1.addWidget(otvet, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_otv1.addWidget(otvet_my1,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

RadioGroupBox2.setLayout(layout_otv1)


# Главные линии
layout_glav = QVBoxLayout()
layout_1glv = QHBoxLayout()
layout_2glv = QHBoxLayout()
layout_3glv = QHBoxLayout()

# Приклепление к линиям

layout_1glv.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_2glv.addWidget(RadioGroupBox)
layout_2glv.addWidget(RadioGroupBox2)

layout_3glv.addStretch(1)
layout_3glv.addWidget(Button,stretch = 2)
layout_3glv.addStretch(1)
layout_glav.setSpacing(100)
# Приклепление к главной верт
layout_glav.addLayout(layout_1glv)
layout_glav.addLayout(layout_2glv)
layout_glav.addLayout(layout_3glv)
main_win.setLayout(layout_glav)
RadioGroupBox.show()
RadioGroupBox2.hide()
# Группа кнопок
RadioGroup = QButtonGroup()
RadioGroup.addButton(question_1)
RadioGroup.addButton(question_2)
RadioGroup.addButton(question_3)
RadioGroup.addButton(question_4)


#Функции
def show_question():
    RadioGroupBox.show()
    RadioGroupBox2.hide()
    Button.setText('Ответить')

def show_result():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    Button.setText('Следующий вопрос')
    RadioGroup.setExclusive(False)
    question_1.setChecked(False)
    question_2.setChecked(False)
    question_3.setChecked(False)
    question_4.setChecked(False)
    RadioGroup.setExclusive(True)
def click_Ok():
    if Button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
answers = [question_1,question_2,question_3,question_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.quest)
    otvet_my1.setText(q.right_answer)
    show_question()
def show_correct(res):
    otvet.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')
    print('Статистика')
    print('Всего вопросов - ',main_win.total)
    print('Правильных ответов', main_win.score)
    print('Рейтинг - ',int(main_win.score/main_win.total*100),'%')
    print()
def next_question():
    main_win.total += 1
    cur_question = randint(0 ,len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)






Button.clicked.connect(click_Ok)
next_question()
# Вывод

main_win.show()
app.exec_()