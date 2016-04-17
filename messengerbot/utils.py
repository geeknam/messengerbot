

def django_verification(request, validation_token):
    from django.http import HttpResponse

    if request.GET['hub.verify_token'] == validation_token:
        return HttpResponse(
            request.GET['hub.challenge']
        )
    return HttpResponse('Error, wrong validation token')
