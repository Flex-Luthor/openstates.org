from django.conf.urls.defaults import patterns, include
from django.conf import settings


urlpatterns = patterns('',
    (r'^api/locksmith/', include('locksmith.mongoauth.urls')),
    (r'^api/', include('billy.web.api.urls')),
    (r'^admin/', include('billy.web.admin.urls')),
    (r'^', include('billy.web.public.urls')),

    # flat pages
    #(r'^$', 'django.views.generic.simple.direct_to_template',
    #{'template':'index.html'}),
    (r'^contributing/$', 'django.views.generic.simple.direct_to_template',
     {'template':'contributing.html'}),
    (r'^thanks/$', 'django.views.generic.simple.direct_to_template',
     {'template':'thankyou.html'}),
    (r'^categorization/$', 'django.views.generic.simple.direct_to_template',
     {'template':'categorization.html'}),
    (r'^status/$', 'django.views.generic.simple.direct_to_template',
     {'template':'status.html'}),
    (r'^csv_downloads/$', 'django.views.generic.simple.direct_to_template',
     {'template':'csv_downloads.html'}),

    # api docs
    (r'^api/$', 'django.views.generic.simple.direct_to_template',
     {'template':'api.html'}),
    (r'^api/metadata/$', 'django.views.generic.simple.direct_to_template',
     {'template':'api_metadata.html'}),
    (r'^api/bills/$', 'django.views.generic.simple.direct_to_template',
     {'template':'api_bills.html'}),
    (r'^api/committees/$', 'django.views.generic.simple.direct_to_template',
     {'template':'api_committees.html'}),
    (r'^api/legislators/$', 'django.views.generic.simple.direct_to_template',
     {'template':'api_legislators.html'}),
    (r'^api/events/$', 'django.views.generic.simple.direct_to_template',
     {'template':'api_events.html'}),
    (r'^api/districts/$', 'django.views.generic.simple.direct_to_template',
     {'template':'api_districts.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT,
          'show_indexes': True}))
