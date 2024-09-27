from django.http import JsonResponse
from subjects.models import Subjects

def filter_subjects(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'GET':
        category_id = request.GET.get('category_id')

        # Fetch subjects related to the category
        subjects = Subjects.objects.filter(category_id=category_id).values('id', 'subject_name')
        subjects_list = list(subjects)

        return JsonResponse(subjects_list, safe=False)
    return JsonResponse([], safe=False)
