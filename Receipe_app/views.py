from django.shortcuts import render,redirect
from Receipe_app.models import *
from django.http import HttpResponse

# Create your views here.

def receipe(request):
    if request.method== "POST":
        data = request.POST
        
        Receipe_name = data.get('reciepe_name')
        Receipe_des = data.get('reciepe_des')
        Receipe_image = request.FILES.get('reciepe_image')
        
        Reciepe.objects.create(
            reciepe_name = Receipe_name,
            reciepe_des = Receipe_des,
            reciepe_image = Receipe_image,)
        
        return redirect("/receipe/")
    
    queryset = Reciepe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(reciepe_name__icontains = request.GET.get('search'))
        
    context = {'receipes' : queryset}
    return render(request, 'reciepe.html' , context)




def delete_receipe(request,id):
    queryset = Reciepe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipe/")


def update_receipe(request, id):
    queryset = Reciepe.objects.get(id=id)
    
    if request.method == 'POST':
        data = request.POST

        Receipe_name = data.get('reciepe_name')
        Receipe_des = data.get('reciepe_des')
        Receipe_image = request.FILES.get('reciepe_image')
        
        queryset.Receipe_name = Receipe_name
        queryset.Receipe_des = Receipe_des

        if Receipe_image:
            queryset.Receipe_image = Receipe_image
        
        queryset.save()
        return redirect('/receipe/')
    
    context = {'receipes' : queryset}
    return render(request, "update_reciepe.html", context)

    