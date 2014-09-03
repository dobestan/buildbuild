from django.conf.urls import patterns, include, url

from django.contrib import admin
from users import views
from django.contrib.auth.decorators import login_required
admin.autodiscover()

from users.views import Login
from users.views import Logout
from users.views import AccountView

from buildbuild.views import Home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buildbuild.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^login/', Login.as_view(), name="login"),
    url(r'^logout/', Logout.as_view(), name="logout"),
    url(r'^account/', login_required(AccountView.as_view(),login_url='/login'), name="account"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls',namespace='users')),
)
