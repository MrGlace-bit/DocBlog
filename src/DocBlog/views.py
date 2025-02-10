from datetime import datetime

from django.shortcuts import render


def index(request):
    date = datetime.today()
    return render(request, 'templates/DocBlog/index.html', context=dict(date=date, prenom="Patrick"))

