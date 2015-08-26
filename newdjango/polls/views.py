from django.http import Http404, HttpResponse
from polls.models import Poll


def index(request):
    if request.method == 'GET':
        polls = Poll.objects.all()
        return HttpResponse(polls.to_json(), content_type='application/json')
    else:
        return Http404('invalid request type')
