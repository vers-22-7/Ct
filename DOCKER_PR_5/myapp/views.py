from django.http import JsonResponse

def profile(request):
    return JsonResponse({'name': 'Ваше Імʼя Прізвище'})
