from http.client import HTTPResponse
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,DetailView,ListView,FormView,CreateView,UpdateView,DeleteView

from .forms import CommentForm, LessonForm, ReplyForm
from app_curriculum.models import Standard
from .models import Standard, Course, Lesson
from django.contrib.auth.mixins import AccessMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



class StandardListView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('user_login',current_app='app_users')
    redirect_field_name = 'redirect_to'
    template_name = 'app_curriculum/standard_list_view.html'
    context_object_name = 'standards'
    model = Standard


class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'app_curriculum/subject_list_view.html'

class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Course
    template_name = 'app_curriculum/lesson_list_view.html'

class LessonDetailView(DetailView,FormView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'app_curriculum/lesson_detail_list_view.html'
    form_class = CommentForm
    second_form_class = ReplyForm

    #handle each reply and comment form as per need
    def get_context_data(self, **kwargs):
        context = super(LessonDetailView,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()

        return context
    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.Standard
        subject = self.object.Course
        return reverse_lazy('app_curriculum:lesson_detail',kwargs={'standard':standard.slug,'subject':subject.slug,'slug':self.object.slug})

    def form_valid(self,form):
        self.object = self.get_object()
        fm = form.save(commit = False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self,form):
        self.object = self.get_object()
        fm = form.save(commit = False)
        fm.author = self.request.user
        fm.comm_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())




    def post(self,request,*args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.form_class
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)

        if form_name == 'form' and form.is_valid():
            print('comment form is returned'
            )
            return self.form_valid(form)
        elif form_name == 'form2' and form.is_valid():
            print("reply form is returned")
            return self.form2_valid(form)
    
class LessonCreateView(UserPassesTestMixin,CreateView):
    form_class = LessonForm
    context_object_name = 'subject'
    model = Course
    template_name = 'app_curriculum/lesson_create.html'
    permission_denied_message = 'Only staff can create lessons'
  
    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('app_curriculum:lesson_list',kwargs={'standard':standard.slug,'slug':self.object.slug})

    def form_valid(self,form,*args,**kwargs):
        self.object = self.get_object()
        my_form = form.save(commit=False)
        my_form.created_by = self.request.user
        my_form.Standard = self.object.standard
        my_form.Course = self.object
        my_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def test_func(self):
        return self.request.user.is_staff



class LessonUpdateView(UserPassesTestMixin,UpdateView):
    fields = ('name','position','video','ppt','Notes')
    model = Lesson
    template_name = 'app_curriculum/lesson_update.html'
    context_object_name = 'lessons'
    def test_func(self):
        return self.request.user.is_staff


class LessonDeleteView(UserPassesTestMixin,DeleteView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'app_curriculum/lesson_delete.html'
    def test_func(self):
        return self.request.user.is_staff
    def get_success_url(self):
        standard = self.object.Standard
        Course = self.object.Course
        return reverse_lazy('app_curriculum:lesson_list',kwargs={'standard':standard.slug,'slug':Course.slug})