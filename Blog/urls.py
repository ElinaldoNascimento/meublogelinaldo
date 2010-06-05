from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo


urlpatterns = patterns('',
    

#(r'^artigo/ (?P<artigo_id>\d+)/$', 'blog.views.artigo'),
    
(r'^$','django.views.generic.date_based.archive_index',{'queryset': Artigo.objects.all(),'date_field': 'publicacao'}),
   # (r'^admin/(.*)', admin.site.root),
(r'^admin/', include(admin.site.urls)),


   
)
#

