from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from _datetime import datetime


# Create your views here.

def articles(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'all_articles.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_at = datetime.now()
            new_form.user = request.user
            new_form.save()
            return redirect('/blog/')
        else:
            print("NOT VALID")
            for e in form.errors:
                print(e)
            return redirect('/blog/add_article')
    else:
        form = ArticleForm()
        return render(request, 'add_article.html', {'form': form})


def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_at = datetime.now()
            new_form.user = request.user
            new_form.save()
            return redirect('/blog/')
        else:
            print("NOT VALID")
            for e in form.errors:
                print(e)
            return redirect('/blog/edit_article')
    else:
        form = ArticleForm(instance=article)
        return render(request, 'edit_article.html', {'form': form})


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article:
        article.delete()

    return redirect('/blog/')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    context = {
        'article': article,
        'url_primary': request.path.split('/')[1],
        'url_suffix': request.path.split('/')[-1],
    }

    print(context['url_primary'])
    print(context['url_suffix'])

    return render(request, 'single_article.html', context)
