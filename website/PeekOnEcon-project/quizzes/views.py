from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import path
from django.contrib.auth.models import User
from .models import Quiz

def all_list(request):
    # quizzes = Quiz.objects.all().order_by('-created')
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/all_list.html', {'quizzes': quizzes})

def view_quiz(request, quiz_id):
    try: 
        quiz = Quiz.objects.get( id = quiz_id )
        questions = quiz.questions.all().prefetch_related('choices')
    except: 
        raise Http404('Not found')
    return render(request, 'quizzes/view_quiz.html', {'quiz':quiz, 'questions': questions})
