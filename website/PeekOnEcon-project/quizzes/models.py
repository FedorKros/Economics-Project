from django.db import models
from django.contrib import admin


# class Quiz(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=300)
    
#     created = models.DateTimeField(auto_now_add=True)
#     url = models.URLField(blank=True)



#     def __str__(self):
#         return self.title

# quiz/models.py



class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

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
