from django.db import models
from django.contrib import admin


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(help_text="Add a description to your quiz.")
    time_limit = models.PositiveIntegerField(help_text="Time limit in minutes.", default=5)
    # created = models.DateTimeField(default=)  
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
