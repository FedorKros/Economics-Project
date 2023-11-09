from django.contrib import admin

# Register your models here.
from .models import Quiz

# class ToDoAdmin(admin.ModelAdmin):
#     readonly_fields = ('created',)

# admin.site.register(Quiz, ToDoAdmin)

from .models import Quiz, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # This allows you to add 3 wrong and 1 correct answer by default

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1  # Number of blank questions
    show_change_link = True  # If you want to edit the question in a separate page
    inlines = [ChoiceInline,]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline,]

admin.site.register(Question)
admin.site.register(Choice)