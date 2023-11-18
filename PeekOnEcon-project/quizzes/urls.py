from django.urls import path
from . import views


urlpatterns = [
    path("all_list/", views.all_list, name = "all_list"), 
    path("view_quiz/<int:quiz_id>/", views.view_quiz, name = "view_quiz"),
    path("quiz_submit/<int:quiz_id>/", views.quiz_submit, name = "quiz_submit"),
]