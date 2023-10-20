from django.urls import path

from . import views

app_name = 'enquetes'

urlpatterns = [
  # /enquetes/
  path('', views.listar, name='listar'),

  # /enquetes/2/
  path('<int:question_id>/', views.detalhar, name='detalhar'),

  # /enquetes/2/resultados/
  path('<int:question_id>/resultados/', views.resultados, name='resultados'),

  # /enquetes/2/votar/
  path('<int:question_id>/votar/', views.votar, name='votar'),
]