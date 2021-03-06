from django.conf.urls import patterns, url

urlpatterns = patterns('softwarecollections.scls.views',
    url(r'^$',                                  'list_all',     name='list_all'),
    url(r'^user/$',                             'list_my',      name='list_my'),
    url(r'^user/(?P<username>.*)/$',            'list_user',    name='list_user'),
    url(r'^tag/(?P<name>.*)/$',                 'list_tag',     name='list_tag'),
    url(r'^new/$',                              'new',          name='new'),
    url(r'^coprnames/(?P<copr_username>[^/]+)/$',
                                                'coprnames',    name='coprnames'),
    url(r'^(?P<slug>[^/]+/[^/]+)/$',            'detail',       name='detail'),
    url(r'^(?P<slug>[^/]+/[^/]+)/edit/$',       'edit',         name='edit'),
    url(r'^(?P<slug>[^/]+/[^/]+)/acl/$',        'acl',          name='acl'),
    url(r'^(?P<slug>[^/]+/[^/]+)/coprs/$',      'coprs',        name='coprs'),
    url(r'^(?P<slug>[^/]+/[^/]+)/repos/$',      'repos',        name='repos'),
    url(r'^(?P<slug>[^/]+/[^/]+)/delete/$',     'delete',       name='delete'),
    url(r'^(?P<slug>[^/]+/[^/]+)/rate/$',       'rate',         name='rate'),
    url(r'^(?P<slug>[^/]+/[^/]+)/review_req/$', 'review_req',   name='review_req'),
    url(r'^(?P<slug>[^/]+/[^/]+)/sync_req/$',   'sync_req',     name='sync_req'),
    url(r'^(?P<slug>[^/]+/[^/]+)/complain/$',   'complain',     name='complain'),
    url(r'^(?P<slug>[^/]+/[^/]+/[^/]+)/download/(.*\.rpm)?$',
                                                'download',     name='download'),
)
urls = (urlpatterns, 'scls', 'scls')
