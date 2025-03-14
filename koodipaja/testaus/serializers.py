# from django.http import JsonResponse
# from .models import QuestionAnswerPair

# def get_questions(request):
#     questions = list(QuestionAnswerPair.objects.values())
#     return JsonResponse(questions, safe=False)

from rest_framework import serializers
from .models import QuestionAnswerPair

class QuestionAnswerPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswerPair
        fields = '__all__'
