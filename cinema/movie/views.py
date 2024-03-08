from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from movie.models import movie

from movie.form import movieform

#function based
# def home(request):
    # return HttpResponse("wia")
    # v = movie.objects.all()
    # return render(request,'home.html',{'m':v})


# class based
class Movie(ListView):    #ListView Displays all objects/records retrieving from a model
    model=movie
    template_name="home.html"
    context_object_name="m"



# function based details

# def view(request):
#     # return HttpResponse("hi")
#     v = movie.objects.all()
#     return render(request, 'view.html', {'m': v})


# class based details

class MovieDetail(DetailView):    #DetailView displays a perticular object retrieving from a model.
    model=movie
    template_name="movie_detail.html"
    context_object_name="v"



# function based

# def add(request):
#     if (request.method=="POST"):
#         n=request.POST['n']
#         d=request.POST['d']
#         y=request.POST['y']
#         i=request.FILES['i']
#         m=movie.objects.create(name=n, desc=d, year=y, image=i)
#         m.save()
#         return home(request)
#     # return HttpResponse('koi')
#     return render(request,'add.html')
#

# class based

class Movieadd(CreateView):    #CreateView displays a form for adding new object and handles form submission
    model=movie
    template_name = "add.html"
    fields = "__all__"
    success_url = reverse_lazy("movie:home")



#function based

# def edit(request,s):
#     m = movie.objects.get(id=s)
#     if (request.method == "POST"):
#         form = movieform(request.POST, request.FILES, instance=m)
#         if form.is_valid():
#             form.save()
#             return view(request)
#
#     form = movieform(instance=m)
#     return render(request, 'edit.html', {'form': form})


#class based

class Movieupdate(UpdateView):
    model = movie
    template_name = "edit.html"
    fields = "__all__"
    success_url = reverse_lazy("movie:home")





# def delete(request,s):
#     m=movie.objects.get(id=s)
#     m.delete()
#     return view(request)

class MovieDelete(DeleteView):
    model = movie
    success_url = reverse_lazy('movie:home')
    template_name = "delete.html"