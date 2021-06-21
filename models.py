from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from quiz.mode


# Create your models here.

class Quiz(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=70)
    image=models.ImageField()
    slug=models.SlugField(blank=True)
    roll_out=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)


class Meta:
    ordering=['timestamp',]
    verbose_name_plural="quizzes"

    def __str__(self):
       return self.name


class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    label=models.CharField(max_length=100)
    order=models.IntegerField(default=0)


    def __str__(self):
       return self.label

class Answer(models.Model):
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    label=models.CharField(max_length=100)
    is_correct= models.BooleanField(default=False)


    def __str__(self):
       return self.label


class QuizTaker(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)
    completed=models.BooleanField(default=False)
    data_finished=models.DateTimeField()
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.email


class UserAnswer(models.Model):
    quiz_taker=models.ForeignKey(QuizTaker,on_delete=models.CASCADE)
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    Answer=models.ForeignKey(Answer,on_delete=models.CASCADE)

    def __str__(self):
    return self.questions.label



@receiver(pre_save,sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug=slugify(instance.name)