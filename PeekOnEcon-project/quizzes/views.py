from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import path
from django.contrib.auth.models import User
from .models import Quiz, Question, Choice

def all_list(request):
    # quizzes = Quiz.objects.all().order_by('-created')
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/all_list.html', {'quizzes': quizzes})

def view_quiz(request, quiz_id):
    try: 
        quiz = Quiz.objects.get( id = quiz_id )
        questions = quiz.questions.all().prefetch_related('choices')
        time_limit = quiz.time_limit
    except: 
        raise Http404('Not found')
    return render(request, 'quizzes/view_quiz.html', {'quiz':quiz, 'questions': questions, 'time_limit': time_limit})

def quiz_submit(request, quiz_id):
    
    quiz = Quiz.objects.get( id = quiz_id )
    score = 0
    total_questions = quiz.questions.count()

    for question in quiz.questions.all():
        selected_choice = request.POST.get(f'question_{question.id}')

        if selected_choice: 
            choice = Choice.objects.get(id = selected_choice)
            if choice.is_correct:
                score += 1
    
    return render(request, 'quizzes/quiz_results.html', {'quiz':    quiz, 'score': score, 'total_questions': total_questions})