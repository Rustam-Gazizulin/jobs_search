from django.urls import path

from companies import views

urlpatterns = [
    path("image/<int:pk>/", views.CompanyImageView.as_view()),
]
