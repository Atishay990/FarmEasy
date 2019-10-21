from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from.models import Grain,farmer

# Create your views here.
def index (request):
    return render(request,'farmeasy/index.html')


def grains(request):
    latest_release = Grain.objects.order_by('grain_date')
    context = {'latest_release': latest_release}
    return render(request, 'farmeasy/market.html', context)

def farm(request):
    if request.method == 'POST':
        if request.POST.get('GrainName'):


            post=farmer()
            post.GrainName=request.POST.get('GrainName')
            post.GrainType=request.POST.get('GrainType')
            post.GrainPrice=request.POST.get('GrainPrice')
            post.GrainImage=request.POST.get('GrainImage')
            post.save()
            return render(request,'farmeasy/index.html')
        else:
            return render(request,'farmeasy/index.html')

    return render(request,'farmeasy/market2.html')

def posting(request):
    all_grains = farmer.objects.all()
    context = {'all_grains':all_grains}
    return render(request,'farmeasy/market.html',context)
