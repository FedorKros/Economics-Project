import os
import telebot
import sqlite3
import os.path
from pathlib import Path
from functools import partial


BOT_API_TOKEN = "6975446452:AAHPV043uCf6aBPzYvD70btuTyYjon5EYaw"

DJANGO_APP_NAME = 'quizzes'
BASE_DIR = Path(__file__).resolve().parent.parent
db_path = os.path.join(BASE_DIR, "db.sqlite3")
CORRECT = True
INCORRECT = False

bot = telebot.TeleBot(BOT_API_TOKEN)
teacher_ids = [556272797]

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Hi! This is my bot")


@bot.message_handler(commands=['add_quiz'])
def addQuiz(message):
    if message.from_user.id in teacher_ids:
        try:
            quiz = bot.reply_to(message,
                                "Please enter quiz title, description and time limit for the new quiz. Separate them with an empty line")
            bot.register_next_step_handler(quiz, addQuestionAndAnswer)
        except Exception as e:
            print(f"An error occured: {e}")
            bot.send_message("Ooops! Something went wrong. Please try again.")
    else:
        bot.send_message(message.chat.id, "You are not an admin. Back off!")


def addQuestionAndAnswer(message):
    quiz_info = message.text.split("\n\n")
    print(quiz_info)

    db_path = os.path.join(BASE_DIR, "db.sqlite3")
    quizPrimaryKey = ""
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        sql_query = """INSERT INTO quizzes_quiz (title, description, time_limit) VALUES (?, ?, ?);"""
        cursor.execute(sql_query, [quiz_info[0], quiz_info[1], int(quiz_info[2])])
        quizPrimaryKey = cursor.lastrowid

    question = bot.reply_to(message, "Please enter the question to add:")
    parametrized_handler = partial(questionInput, quizId=quizPrimaryKey)
    bot.register_next_step_handler(question, parametrized_handler)


def questionInput(message, quizId):
    question = message.text
    questionPrimaryKey = ""
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        sql_query = """INSERT INTO quizzes_question (quiz_id, text) VALUES (?, ?);"""
        cursor.execute(sql_query, [quizId, question])
        questionPrimaryKey = cursor.lastrowid

    correctAnswer = bot.reply_to(message, "Please enter the correct answer:")
    parametrized_handler_question = partial(correctAnswerInput, questionId=questionPrimaryKey, quizId=quizId)
    bot.register_next_step_handler(correctAnswer, parametrized_handler_question)


def correctAnswerInput(message, questionId, quizId):
    correctAnswer = message.text
    print(correctAnswer)
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        sql_query = """INSERT INTO quizzes_choice (text, is_correct, question_id) VALUES (?, ?, ?);"""
        cursor.execute(sql_query, [correctAnswer, CORRECT, questionId])
    incorrectAnswers = bot.reply_to(message, "Please enter incorrect answers, separate them with an empty line:")
    parametrized_handler_correct_answer = partial(incorrectAnswersInput, questionId=questionId, quizId=quizId)
    bot.register_next_step_handler(incorrectAnswers, parametrized_handler_correct_answer)


def incorrectAnswersInput(message, questionId, quizId):
    incorrectAnswersList = message.text.split("\n\n")
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        sql_query = """INSERT INTO quizzes_choice (text, is_correct, question_id) VALUES (?, ?, ?);"""
        for incorrectAnswer in incorrectAnswersList:
            cursor.execute(sql_query, [incorrectAnswer, INCORRECT, questionId])
    parametrized_handler_incorrect_answer = partial(chooseNextStep, quizId=quizId)
    nextStep = bot.reply_to(message,
                            'Question successfully added! Write 1 to creat another question or 2 to finish the quiz creation.')
    bot.register_next_step_handler(nextStep, parametrized_handler_incorrect_answer)


def chooseNextStep(message, quizId):
    nextStep = message.text
    if nextStep == '1':
        question = bot.reply_to(message, "Please enter the next question")
        parametrized_handler_next_quiz = partial(questionInput, quizId=quizId)
        bot.register_next_step_handler(question, parametrized_handler_next_quiz)
    else:
        bot.send_message(message.chat.id, "Quiz successfully created :)")


bot.polling(none_stop=True)