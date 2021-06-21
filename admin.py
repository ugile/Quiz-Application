from django.contrib import admin
import nested_admin
from.models import Quiz, Question, Answer, QuizTaker, UserAnswer
# Register your models here.


class AnswerInline(nested_admin.NestedTabularInline):
      model=Answer
      extra=4
      max_num=4

class QuestionInline(nested_admin.NestedTabularInline):
      model=Question
      inlines=[AnswerInline,]
      extra=5

class QuizAdmin(nested_admin.NestedModelAdmin):
      inlines=[QuestionInline,]

class UsersAnswerInline(nested_admin.NestedTabularInline):
    model=UserAnswer

class QuizTakerAdmin(nested_admin.NestedTabularInline):
    inlines=[UsersAnswerInline,]


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizTaker)
admin.site.register(UserAnswer)

