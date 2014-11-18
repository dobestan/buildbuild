from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from buildbuild.views import Home
from teams.views import MakeTeamView
from projects.views import MakeProjectView
from django.contrib.auth.decorators import login_required
from teams.views import TeamList
from projects.views import MakeProjectView

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^admin/', include(admin.site.urls)),
    
    # users' urls
    url(r'^', include('users.urls', namespace='users')),
    
    # teams' urls
    url(r'^', include('teams.urls', namespace='teams')),
    url(r'^teams/$', TeamList.as_view(), name="teamlist"),
    url(r'^teams/([0-9]+)/$', 'teams.views.team_page', name='team_page'),
    
    # projects' urls
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(
        r'^teams/([0-9]+)/projects/([0-9]+)/$', 
        'projects.views.project_page', 
        name='project_page',
    ),
    url(
        r'^teams/(?P<team_id>[0-9]+)/projects/new/$',
        login_required(MakeProjectView.as_view()),
        name="makeproject"
    ),  

    # dockerbuild's urls
    url(
        r'^builds/', 
        include('dockerbuild.urls', namespace='builds')
    ),
)
