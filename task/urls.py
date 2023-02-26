from django.urls import path
from . import views

urlpatterns = [
    path(
        route='create/',
        view=views.CreateView.as_view(),
        name='create'
    ),
    path(
        route='delete/',
        view=views.DeleteView.as_view(),
        name='delete'
    ),
    path(
        route='assign/',
        view=views.AssignView.as_view(),
        name='assign'
    ),
    path(
        route='view_all/',
        view=views.ViewAllView.as_view(),
        name='view_all'
    )
]
