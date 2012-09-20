from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.news.views.feed'),
    # admin site
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^login$', 'app.auth.views.signin'),
    url(r'^logout$', 'app.auth.views.signout'),
    url(r'^news/', include('app.news.urls')),
    
    #account
    url(r'^account/', include('app.account.urls')),

    # Static pages
    url(r'^about/(?P<about_slug>[a-z-]+)/$', 'app.website.views.about'),
    url(r'^teams/(?P<team_slug>[A-Za-z-]+)/$', 'app.website.views.teams'),
    url(r'^fun/(?P<fun_slug>[a-z-]+)/$', 'app.website.views.fun'),
    url(r'^sponsors$', 'app.website.views.sponsors'),
    
    #finance(invoice, paypal)
    url(r'^finance/', include('app.finance.urls')),
                       
    # urls for music
    (r'^music/vote/$', 'app.music.views.music_vote'),
    (r'^music/$', 'app.music.views.music_submit_song'),

    # miscellaneous
    url(r'^(?P<path>.*)/$', 'app.website.views.slug'),
                       
                       

    # admin site
    #(r'^admin/', include(backends.site.urls)),

    # login
    #(r'accounts/login/$', 'csesoc.auth.backends.cse_login'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

# Serve the static folder if in development
#from django.conf import settings
#if settings.DEBUG:
#    urlpatterns += patterns('django.contrib.staticfiles.views',
#        url(r'^assets/(?P<path>.*)$', 'serve'),
#    )