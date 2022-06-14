from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from . forms import StudentForm
from . models import Student

from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Create your views here.


class HomeView(TemplateView):
    template_name = 'enroll/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fr = StudentForm()
        st = Student.objects.all()
        context = {
            'form': fr, 'st': st
        }
        return context

    def post(self, request):
        fr = StudentForm(request.POST)
        if fr.is_valid():
            name = fr.cleaned_data['name']
            email = fr.cleaned_data['email']
            password = fr.cleaned_data['password']
            reg = Student(name=name, email=email, password=password)
            reg.save()

            return redirect('home')


class DeleteStudent(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Student.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class UpdateStudent(View):
    def get(self, request, id):
        st = Student.objects.get(pk=id)
        fr = StudentForm(instance=st)
        return render(request, 'enroll/update.html', {'form': fr})

    def post(self, request, id):
        st = Student.objects.get(pk=id)
        fr = StudentForm(request.POST, instance=st)
        if fr.is_valid():
            fr.save()
        return redirect('home')
