from django.conf.urls import include, url
from django.contrib import admin
from home_test.views import signin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',signin, name='signin'),
    url(r'^home_test/', include('home_test.urls', namespace='home')),

]