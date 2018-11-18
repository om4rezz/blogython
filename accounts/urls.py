from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
                  url('signup/', views.SignUp.as_view(), name='signup'),
                  url('all/', views.all_users, name='all_users'),
                  url(r'^(?P<user_id>\d+)/edit/', views.edit_user, name='edit_user'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# url(r'^$', views.all_notes, name='all_notes'),
# url(r'^(?P<id>\d+)$', views.detail, name='note_detail'),
# url(r'^(?P<note_id>\d+)/edit$', views.edit, name='note_edit'),
# url(r'^add$', views.note_add, name='add_note'),
