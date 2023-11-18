# from models import Quiz
from django.conf import settings
from django.db import models
from django.contrib import admin
import telebot
import django
import os
import sqlite3

connection = sqlite3.connect('db.sqlite3', check_same_thread=False)

cursor = connection.cursor()


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quizzes.settings")
# settings.configure()
# django.setup()




BOT_API_TOKEN = "6975446452:AAHPV043uCf6aBPzYvD70btuTyYjon5EYaw"

DJANGO_APP_NAME = 'quizzes'



bot = telebot.TeleBot(BOT_API_TOKEN)
quiz = ''


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Hi! This is my bot")


@bot.message_handler(commands=['add_quiz'])
def addQuiz(message):
    if message.from_user.id == 556272797:
        try:
            quiz = bot.reply_to(message, "Please enter quiz title, description and time limit for the new quiz. Separate them with an empty line")
            bot.register_next_step_handler(quiz, addQuestionAndAnswer)


        except Exception as e:
            print(f"An error occured: {e}")
            bot.send_message("Ooops! Something went wrong. Please try again.")

    else:
        bot.send_message("You are not an admin. Back off!")
    

    # Quiz.objects.create(title=title)

    


# def addQuestionAndAnswer(message):
#     quiz_info = message.text.split("\n\n")
#     print(quiz_info)

#     q = Quiz.objects.create(title=quiz_info[0], description=quiz_info[1], time_limit=int(quiz_info[2]))
#     # q = Quiz(title=quiz_info[0], description=quiz_info[1], time_limit=int(quiz_info[2]))
#     q.save()
#     # Add the db the quiz
#     # And save quiz to the global file variable 
    
#     question = bot.reply_to(message, "Please enter the question to add:")
#     bot.register_next_step_handler(question, questionInput)
#     # Question.objects.create(quiz=)

def addQuestionAndAnswer(message):
    quiz_info = message.text.split("\n\n")
    print(quiz_info)
    title = quiz_info[0]
    description = quiz_info[1]
    time_limit = int(quiz_info[2])
    # quiz = Quiz.objects.create(title=quiz_info[0], description=quiz_info[1], time_limit=int(quiz_info[2])) 
    # with connection.cursor() as cursor:
    # print(cursor.execute(".tables").fetchAll())
    # sql_query = """
    #         INSERT INTO quizzes_quiz (title, description, time_limit)
    #         VALUES (%s, %s, %s)
    #     """
    # cursor.execute("INSERT INTO quizzes_quiz VALUES (?, ?, ?)", ('title', 'description', 2))
    # cursor.execute(sql_query, [quiz_info[0], quiz_info[1], int(quiz_info[2])])
    # sql_query = """
    #         INSERT INTO quizzes_quiz (title, description, time_limit)
    #         VALUES ({title}, {description}, {times})
    #     """.format(title=quiz_info[0], description=quiz_info[1], times=int(quiz_info[2]))
    sql_query = """
            INSERT INTO quizzes_quiz (title, description, time_limit)
            VALUES ('a', 's', 1)
        """
    # sql_query = """
    #         INSERT INTO quizzes_quiz VALUES a, b, 2
    #     """
    cursor.execute(sql_query)
    question = bot.reply_to(message, "Please enter the question to add:")
    bot.register_next_step_handler(question, questionInput)
    # Question.objects.create(quiz=)



def questionInput(message):
    question = message.text
    print(question)
    correctAnswer = bot.reply_to(message, "Please enter the correct answer:")
    bot.register_next_step_handler(correctAnswer, correctAnswerInput)


def correctAnswerInput(message):
    correctAnswer = message.text
    print(correctAnswer)
    incorrectAnswers = bot.reply_to(message, "Please enter incorrect answers, separate them with an empty line:")
    bot.register_next_step_handler(incorrectAnswers, incorrectAnswersInput)
    


def incorrectAnswersInput(message):
    incorrectAnswers = message.text
    incorrectAnswersList = incorrectAnswers.split("\n\n")
    nextStep = bot.reply_to(message, 'Question successfully added! Write 1 to creat another question or 2 to finish the quiz creation.')
    bot.register_next_step_handler(nextStep, chooseNextStep)

def chooseNextStep(message):
    nextStep = message.text
    if nextStep == '1':
        question = bot.reply_to(message, "Please enter the next question")
        bot.register_next_step_handler(question, questionInput)
    else:
        bot.send_message(message.chat.id, "Quiz successfully created :)")

    # bot.send_message(message.chat.id, "Quiz creation complete! :)")
        
        
bot.polling(none_stop=True)
















# import telebot
# from models import Quiz, Question, Choice

# BOT_API_TOKEN = "6975446452:AAHPV043uCf6aBPzYvD70btuTyYjon5EYaw"

# bot = telebot.TeleBot(BOT_API_TOKEN)

# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, "Hi! This is my bot")


# @bot.message_handler(commands=['add_quiz'])
# def addQuiz(message):
#     if message.from_user.id == 556272797:
#         question = bot.reply_to(message, "Add a question or finish creating the quiz.")
#         bot.register_next_step_handler(question, addQuestionAndAnswer)
#         # title = bot.send_message(message.chat.id, "Enter the quiz title.")
#         # description = bot.reply_to(message, "Add a description")
#         # print(title)
#         # print(description)
#         # Quiz.objects.create(title=title)
#     else:
#         print("ТЫ НЕ ПРОЙДЕШЬ!!!")



# def addQuestionAndAnswer(message):
#     question = bot.reply_to(message, "Please enter the question to add:")
#     bot.register_next_step_handler(question, questionInput)
#     # Question.objects.create(quiz=)
    


# def questionInput(message):
#     question = message.text
#     print(question)
#     correctAnswer = bot.reply_to(message, "Please enter the correct answer:")
#     bot.register_next_step_handler(correctAnswer, correctAnswerInput)
    


# def correctAnswerInput(message):
#     correctAnswer = message.text
#     print(correctAnswer)
#     incorrectAnswers = bot.reply_to(message, "Please enter incorrect answers, separate them with an empty line:")
#     bot.register_next_step_handler(incorrectAnswers, incorrectAnswersInput)


# def incorrectAnswersInput(message):
#     incorrectAnswers = message.text
#     incorrectAnswersList = incorrectAnswers.split("\n\n")
#     print(incorrectAnswersList)

# bot.polling(none_stop=True)