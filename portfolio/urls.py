from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.entry_page_view),
    path('index', views.entry_page_view, name='index'),
    path('home', views.home_page_view, name='home'),
    path('login-submit', views.submit_login, name='login-submit'),
    path('disciplinas', views.disciplinas_page_view, name='disciplinas'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('blog', views.blog_page_view, name='blog'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('logout', views.logout_user, name='logout'),
]