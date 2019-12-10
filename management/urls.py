from django.urls import path

from . import views

urlpatterns = [
    path('management/feedback', views.AjaxFeedbackCreateView.as_view(), name='feedback'),
]
