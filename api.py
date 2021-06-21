from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from quiz.models import Quiz,QuizTakers
from quiz.serializers import QuizListSerializer,QuizDetailSerizer


# Create your views here.
class QuizListAPI(generics.ListAPIView):
    

    def get_queryset(self,*args,**kwargs):
        queryset = Quiz.objects.filter(roll_out=True).exclude(quiztaker)_user=self.request.user)
        query = self.request.GET.get("q")

        if query:
            queryset = querset.filter(
                Q(name_icontains=query)|
                Q(description_icontains=query)

            ).distinct()

        return queryset

class QuizDetailAPI(generics.RetrieveAPIView):
    serializer_class = QuizListSerializer


    def get(self,*args, **kwargs):
        slug = self.kwargs["slug"]
        quiz = get_object_or_404(Quiz,slug=slug)
        last_question = None
        obj, create = QuizTakers.objects.get_or_create(user=self.request.user,quiz=quiz)
        if created:
            for question in Question.objects.filter(quiz=quiz):
                UserAnswer.objects.create(quiz_taker=obj,question=questio)
        else:
            last_question = UserAnswer.object.filter(quiz_taker=obj,answer_isnull=False)
            if last_question.count() > 0:
                last_question =last_question.last().question.id
            else:
                last_question = None
        returnResponse('quiz':self.get_serializer(quiz,context={'request': self.request}).data,'last_question_id':last_question})