from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Article
from .forms import ContactForm

class IndexPage(TemplateView):
    
    def get(self, request, **kwargs):
        article_data = []
        articles = Article.objects.all()
        for article in articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'content': article.content,
                'created_at': article.created_at.date(),
            })
        
        promote_data = []
        all_promote_articles = Article.objects.filter(promote=True)
        for promote_article in all_promote_articles:
            promote_data.append({
                'category': promote_article.category.title,
                'title': promote_article.title,
                'author': promote_article.author.user.first_name + ' ' + promote_article.author.user.last_name,
                'avatar': promote_article.author.avatar.url if promote_article.author.avatar else None,
                'cover': promote_article.cover.url if promote_article.cover else None,
                'created_at': promote_article.created_at.date(),
            })

        context = {
            'article_data': article_data,
            'promote_article_data': promote_data,
        }

        return render(request, 'index.html', context)


class AboutPage(TemplateView):
    template_name = 'about.html'


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to the Contact Page.',
        'form': contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact.html', context)