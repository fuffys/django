from django.shortcuts import render
from myfirst.models import Champion
from django.views.generic import ListView




class ChampionListView(ListView):
    model = Champion

    context_object_name = 'champions_list'

    template_name = 'champions.html'

def get_queryset(self):
 if 'champion_name' in self.kwargs:
    return Champion.objects.filter(champions__name=self.kwargs['champion_name']).all()
 else:
    return Champion.objects.all()



def index(request):
    champions = Champion.objects.order_by('name')[:12]

    context = {
        'champions': champions
    }

    return render(request, 'index.html', context=context)
