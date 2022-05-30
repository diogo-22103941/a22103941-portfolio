import imp
from logging.config import IDENTIFIER

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from matplotlib import pyplot as plt

# Create your views here.

def disciplinas_page_view(request):
    context = {'cadeiras': Cadeira.objects.all().order_by('semestre')}

    return render(request, 'portfolio/disciplinas.html', context)

def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}

    return render(request, 'portfolio/projetos.html', context)

def entry_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'minutos': agora.minute,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/index.html', context)

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Utilizador ou senha inválida, tente novamente')
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'minutos': agora.minute,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html', context)

def blog_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            form.save()
            return HttpResponseRedirect(reverse('portfolio:blog'))
        else:
            messages.error(request, 'Tem de efetuar login para submeter um post.')

    context = {'form': form, 'posts': Post.objects.all().order_by('data').reverse}
    return render(request, 'portfolio/blog.html', context)

def pontuacao_quizz(request):
    pontos = 0

    if request.POST['pergunta_1'] == 'r2':
        pontos += 25
    if request.POST['pergunta_2'] == 'r3':
        pontos += 25
    if request.POST['pergunta_3'] == 'r2':
        pontos += 25
    if request.POST['pergunta_4'] == 'r3':
        pontos += 25

    return pontos

def grafico_pontuacao():
    sorted_bd = sorted(PontuacaoQuizz.objects.all(), key=lambda objecto: objecto.pontos, reverse=True)
    nomes = [objecto.nome for objecto in sorted_bd]
    pontuacoes = [objecto.pontos for objecto in sorted_bd]
    plt.barh(nomes,pontuacoes)
    plt.savefig('portfolio/static/portfolio/images/grafico_resultados.png', bbox_inches='tight')
    plt.close()

def quizz_page_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        
        PontuacaoQuizz.objects.update_or_create(nome=n, defaults={'pontos':p})

        grafico_pontuacao()

    return render(request,"portfolio/quizz.html")

