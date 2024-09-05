from django.db.models.query import QuerySet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from projects.models import Project,Task
from projects.forms import ProjectCreateForm,ProjectUpdateForm
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
class ProjectList(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'projects/list.html'
    paginate_by = 3

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id':self.request.user}

        q = self.request.GET.get('q',None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class CreateProjectView(LoginRequiredMixin,CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('project_list')

    def  form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class DeleteProjectView(LoginRequiredMixin,DeleteView):

    model = Project
    http_method_names=["post"]

    def get_success_url(self):
        return reverse('project_list')

class UpdateProjectView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'projects/update.html'

    def test_func(self):
        return self.get_object().user_id == self.request.user.id
    
    def get_success_url(self):
        return reverse('update_project',args=[self.object.id])

class CreateTaskView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Task
    fields = ['description','project']
    http_method_names = ['post']

    def test_func(self):
        project_id = self.request.POST.get('project','')
        return Project.objects.get(pk=project_id).user_id == self.request.user.id
    
    def get_success_url(self):
        return reverse('update_project',args=[self.object.project.id])

class UpdateTaskView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['is_completed']
    http_method_names = ['post']

    def test_func(self):
        project_id = self.request.POST.get('project','')
        return Project.objects.get(pk=project_id).user_id == self.request.user.id

    def get_success_url(self):
        return reverse('update_project',args=[self.object.project.id])

class DeleteTaskView(LoginRequiredMixin,DeleteView):
    model = Task

    def test_func(self):
        project_id = self.request.POST.get('project','')
        return Project.objects.get(pk=project_id).user_id == self.request.user.id
        
    def get_success_url(self):
        return reverse('update_project',args=[self.object.project.id])

