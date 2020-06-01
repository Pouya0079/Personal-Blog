from django.conf.urls import url
from .views import (
    IndexPage, 
    AboutPage, 
    contact_page, 
    AllArticleAPIView, 
    SingleArticleAPIView,
    SearchArticleAPIView,
    SubmitArticleAPIView,
    UpdateArticleCoverAPIView,
    DeleteArticleAPIView,
)

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index'),
    url(r'^about/$', AboutPage.as_view(), name='about'),
    url(r'^contact/$', contact_page, name='contact'),

    url(r'^article/all/$', AllArticleAPIView.as_view(), name='all_articles'),
    url(r'^article/$', SingleArticleAPIView.as_view(), name='single_articles'),
    url(r'^article/search/$', SearchArticleAPIView.as_view(), name='search_article'),
    url(r'^article/submit/$', SubmitArticleAPIView.as_view(), name='submit_article'),
    url(r'^article/update-cover/$', UpdateArticleCoverAPIView.as_view(), name='update_article_cover'),
    url(r'^article/delete/$', DeleteArticleAPIView.as_view(), name='delete_article'),
    
]