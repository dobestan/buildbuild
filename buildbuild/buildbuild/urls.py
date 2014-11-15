from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from buildbuild.views import Home
from teams.views import MakeTeamView
from projects.views import MakeProjectView
from django.contrib.auth.decorators import login_required
from teams import views
from users.views import Login, Logout, \
    SignUp


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buildbuild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^teams/', include('teams.urls', namespace='teams')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^dockerbuild/', include('dockerbuild.urls', namespace='dockerbuild')),
    url(r'^login/', Login.as_view(), name="login"),
    url(r'^logout/', Logout.as_view(), name="logout"),
    url(r'^signup/', SignUp.as_view(), name="signup"),

)
