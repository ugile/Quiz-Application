from django.urls import path,re_path
from quiz.api import QuizlistAPI,QuizDetailAPi



urlpatterns = [
    
    path ("quizzes/", QuizListAPI.as_view()),
    path ("quizzes/?<slug>[\w\-]+)/$", QuizListAPI.as_view()),

    
]