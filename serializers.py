from quiz.models import Quiz
from rest_framwork import serializers


class QuizListSerializer(serializers.ModelSerializer)
question_count = serialiers.SerializerMethodField()
    class Meta:
        model=QuizQuestionSerializer
        model = QuizListSerialierfields = ["id", "name", "discription", "image", "slug"]
        fields = ["id","name","description","image","slug"]
        read_only_fields = ["questions_count"]

    def get_question_count(self,obj):
        returnobj.get_question_set.all()..count()

class UserAnswerSerializer(Serializers.ModelSerializer):
    class meta:
        model =UserAnswerfield = ["id","question","label"]


class QuestionSerializer(serialiers.ModelSerializer):
    answer_set =AnswerSerializer(many=True)
    class Meta:
        model = Question
        field = "_all_"

class UserAnswerSerializer(serialiers.ModelSerializer):
    class Meta:
        model = UserAnswer
        field = "_all_"

class QuizTakerSerializer(serialiers.ModelSerializer):
    user_answer_set =UserAnswerSerializer(many=True)

    class Meta:
        model = QuizTaker
        fields = "_all_" 

class QuizDetailsSerializer(serializers.ModelSerializer):
    quiztakers_set = serializers.SerializerMethodField()
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = "_all_"

    def get_question_set(self, obj):
        try:
            quiz_taker = QuizTaker.object.get(user=self.context['request'].user,quiz=obj)
            serializer = QuizTakerSerializer(quiz_taker)
            return serializer.data
        except QuizTaker.DoesNoteExist:
            return None

