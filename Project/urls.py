from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from core import views


urlpatterns = [
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^$', views.home, name='home'),
    url(r'^upload/$', views.simple_upload, name='simple_upload'),
    url(r'^record/$', views.record, name='record'),
    url(r'^karaoke/$' , views.karaoke_success ,name='karaoke'),
    url(r'^admin/', admin.site.urls),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

