from django.urls import path
from .views import HomePageView,ToDoAddView,ToDoEditView,ToDoDeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('todo/add/', ToDoAddView.as_view(), name='add_task'),
    path('todo/edit/<int:pk>/', ToDoEditView.as_view(), name='edit'),
    path('todo/delete/<int:pk>/', ToDoDeleteView.as_view(), name='delete')
]