from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
    try:
        id = int(request.GET["id"])
        message = Message.objects.get(pk=id).content
    except:
        message = "ID not found"

    return HttpResponse(message)
		
	#content = 'Hello Web!'
	#return HttpResponse(content)
