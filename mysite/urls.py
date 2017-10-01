from django.conf.urls import include, url
from django.contrib import admin
from home_test.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view()),
    url(r'^home_test/', include('home_test.urls', namespace='home')),

]