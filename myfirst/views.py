from django.shortcuts import render
from myfirst.models import Champion
from django.views.generic import ListView, DetailView




def index(request):
    champions = Champion.objects.order_by('name')[:12]

    context = {
        'champions': champions
    }

    return render(request, 'index.html', context=context)

class ChampionListView(ListView):
    model = Champion
    context_object_name = 'champions_list'
    template_name = 'champions.html'

class ChampionDetailView(DetailView):
     model = Champion
     context_object_name = 'champions_detail'
     template_name = 'detail.html'