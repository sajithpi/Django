from django.contrib import messages
from django.contrib.messages.constants import SUCCESS
from django.http import request
from django.shortcuts import  get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, FormView, DeleteView, UpdateView
from .forms import UserForm

from .models import UserDetail
from .forms import UserForm
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['user_detail'] = UserDetail.objects.all()
        return context

class DetailPageView(DetailView):
    template_name = "detail.html"
    model = UserDetail

class AddUserView(FormView):
    template_name = "adduser.html"
    form_class = UserForm
    success_url = "/"
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request,*args,**kwargs)
    def form_valid(self, form):
        # Create a new User Data
        new_object = UserDetail.objects.create(
            name = form.cleaned_data['name'],
            image = form.cleaned_data['image'],
            email = form.cleaned_data['email'],
            age = form.cleaned_data['age'],
            place = form.cleaned_data['place'],
            occupation = form.cleaned_data['occupation'],
            gender = form.cleaned_data['gender'],
         
        )
        messages.add_message(self.request ,messages.SUCCESS,'User Details Added Successfully')
        return super().form_valid(form)

class UpdateUserView(UpdateView):
    template_name = "update.html"
    model = UserDetail
    form_class = UserForm
    success_url = "/"
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        messages.add_message(self.request ,messages.SUCCESS,'User Details Updated Successfully')
        return super().form_valid(form)
        
    # fields = ['name','image','age','email','place','occupation']

class DeleteUserView(DeleteView):
    template_name = "delete.html"
    form_class = UserForm
    success_url = "/"
    model = UserDetail

    def dispatch(self, request, *args, **kwargs):
        # self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        id_ = self.kwargs.get("id")
      
        return get_object_or_404(UserDetail,id=id_)
    def post(self, request, *args, **kwargs):
          self.request = request
          messages.add_message(self.request,messages.SUCCESS,"Successfully Deleted User Details")
          return self.delete(request, *args, **kwargs)
        







 

  
