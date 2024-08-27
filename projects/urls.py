
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.ProjectList.as_view(),name='project_list'),
    path('project/create',views.CreateProjectView.as_view(),name='create_project'),
    path('project/edit/<int:pk>',views.UpdateProjectView.as_view(),name='update_project'),
    path('task/create',views.CreateTaskView.as_view(),name='create_task'),
    path('task/edit/<int:pk>',views.UpdateTaskView.as_view(),name='update_task'),
    path('task/delete/<int:pk>',views.DeleteTaskView.as_view(),name='delete_task'),
]
