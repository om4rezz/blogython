from django.conf.urls import url
from . import views

app_name = 'permissions'

urlpatterns = [
    url(r'^$', views.all_permissions, name='all_permissions'),
    url(r'^(?P<id>\d+)/edit$', views.edit_permission, name='edit_permission'),
    url(r'^(?P<id>\d+)/delete$', views.delete_permission, name='delete_permission'),
]
# url(r'^$', views.all_notes, name='all_notes'),
# url(r'^(?P<id>\d+)$', views.detail, name='note_detail'),
# url(r'^(?P<note_id>\d+)/edit$', views.edit, name='note_edit'),
# url(r'^add$', views.note_add, name='add_note'),
