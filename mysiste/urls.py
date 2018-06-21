
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [ 
url(r'', include('polls.urls', namespace="polls")),
url(r'^blog/', include('blog.urls')),
url(r'^admin/', admin.site.urls), ]

