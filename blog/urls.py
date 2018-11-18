from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
                  url(r'^$', views.articles, name='all_articles'),
                  url(r'^add_article$', views.add_article, name='add_articles'),
                  url(r'^(?P<article_id>\d+)/delete_article$', views.delete_article, name='delete_article'),
                  url(r'^(?P<article_id>\d+)/show$', views.show_article, name='show_article'),
                  url(r'^(?P<article_id>\d+)/edit_article$', views.edit_article, name='edit_article'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# url(r'^$', views.all_notes, name='all_notes'),
# url(r'^(?P<id>\d+)$', views.detail, name='note_detail'),
# url(r'^(?P<note_id>\d+)/edit$', views.edit, name='note_edit'),
# url(r'^add$', views.note_add, name='add_note'),
