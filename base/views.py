from django.http import JsonResponse


def check_health(request):
    return JsonResponse(
        data="Reached",
        safe=False
    )
