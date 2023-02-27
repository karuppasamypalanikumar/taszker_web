from django.urls import path
from . import views

urlpatterns = [
    path(
        route='create/',
        view=views.CreateTaskView.as_view(),
        name='create'
    ),
    path(
        route='delete/',
        view=views.DeleteTaskView.as_view(),
        name='delete'
    ),
    path(
        route='update/',
        view=views.UpdateTaskView.as_view(),
        name='update'
    ),
    path(
        route='view_all/',
        view=views.ViewAllTaskView.as_view(),
        name='view_all'
    ),
    path(
        route='view_all_users/',
        view=views.AvailableUserView.as_view(),
        name='view_all_users'
    ),
    path(
        route='view_all_status/',
        view=views.ViewAllStatusView.as_view(),
        name='view_all_status'
    ),
    path(
        route='view_all_projects/',
        view=views.ViewAllProjectView.as_view(),
        name='view_all_projects'
    )
]
