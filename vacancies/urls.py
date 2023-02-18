from django.urls import path

from vacancies import views

urlpatterns = [

    path("", views.VacancyListView.as_view()),
    path("<int:pk>/", views.VacancyDetailView.as_view()),
    path("update/<int:pk>/", views.VacancyUpdateView.as_view()),
    path("create/", views.VacancyCreateView.as_view()),
    path("delete/<int:pk>/", views.VacancyDeleteView.as_view()),
]
