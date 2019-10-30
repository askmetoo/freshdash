from django.shortcuts import render
from django.http import Http404, JsonResponse
from dashboard.models import Client

def index(request):
    sort_by = {
        'name' : 'name',
        'time' : 'hours_remaining',
        'status' : 'status'
    }

    query = request.GET.dict()
    clients = Client.objects.all()

    # for key, value in sort_by.items():
    #     if query and query['sort'] == key:
            # clients.sort(key=lambda x: getattr(x, value)())

    context = {'clients': clients}

    return render(request, 'dashboard/index.html', context)

def response(items, failure_message="404 Not found"):
    if items is False:
        raise Http404(failure_message)
    else:
        return JsonResponse(items, safe=False)
