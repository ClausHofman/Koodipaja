from django.http import JsonResponse
from .models import QuestionAnswerPair

def get_questions(request):
    questions = list(QuestionAnswerPair.objects.values())
    return JsonResponse(questions, safe=False)
