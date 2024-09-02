from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from projects.models import Project,Task
from projects.forms import ProjectCreateForm,ProjectUpdateForm
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect

class ProjectList(ListView):
    model = Project
    template_name = 'projects/list.html'
    paginate_by = 3


class CreateProjectView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('project_list')

class DeleteProjectView(DeleteView):

    model = Project
    http_method_names=["POST"]

    def get_success_url(self):
        return reverse('project_list')

class UpdateProjectView(UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'projects/update.html'

    
    def get_success_url(self):
        return reverse('update_project',args=[self.object.id])

class CreateTaskView(CreateView):
    model = Task
    fields = ['description','project']
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('update_project',args=[self.object.project.id])

class UpdateTaskView(UpdateView):
    model = Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('update_project',args=[self.object.project.id])

class DeleteTaskView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('update_project',args=[self.object.project.id])

