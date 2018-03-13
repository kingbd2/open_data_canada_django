from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Inventory

from profile_data_script import profile

def inventory_explorer(request):
    titles = Inventory.objects.exclude(date_published__isnull=True).order_by('-date_published')[:1000]
    context = {'titles': titles}
    return render(request, 'inventory_explorer/index.html', context)

def item_detail(request, inventory_id):
    title = get_object_or_404(Inventory, pk=inventory_id)
    return render(request, 'inventory_explorer/item_detail.html', {'title': title})

def results(request, inventory_id):
    response = "You're looking at the results of poll %s."
    return HttpResponse(response % inventory_id)

def vote(request, inventory_id):
    return HttpResponse("You're voting on item %s." % inventory_id)

def get_data(request):
    response = HttpResponse(Inventory, content_type='text/plain')
    response_a = profile(response)
    return response_a

#name__contains='Smith'
