from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import path
from django.contrib.auth.models import User
from .models import Quiz, Question, Choice
from random import shuffle
from django.db.models import Prefetch


def all_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/all_list.html', {'quizzes': quizzes})

def view_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all().prefetch_related(Prefetch('choices', queryset=Choice.objects.order_by('?')))
    time_limit = quiz.time_limit

    print(questions)
    return render(request, 'quizzes/view_quiz.html', {'quiz':quiz, 'questions': questions, 'time_limit': time_limit})


def quiz_submit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    score = 0
    total_questions = quiz.questions.count()
    # information about each question
    results = []  

    for question in quiz.questions.all():
        selected_choice_id = request.POST.get(f'question_{question.id}')
        selected_choice = Choice.objects.get(id=selected_choice_id) if selected_choice_id else None

        is_correct = selected_choice.is_correct if selected_choice else False
        for choice in question.choices.all():
            if choice.is_correct:
                correct_choice = choice
        
        question_info = {
            'question': question,
            'selected_choice': selected_choice,
            'is_correct': is_correct,
            'correct_choice': correct_choice
        }

        results.append(question_info)
        if is_correct:
            score += 1

    return render(request, 'quizzes/quiz_results.html', {'quiz': quiz, 'score': score, 'total_questions': total_questions, 'results': results})