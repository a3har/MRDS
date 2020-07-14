from django.conf.urls import url
from . import views

app_name= 'first'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^hospital_user/$', views.hospital_user, name='hospital_user'),
    url(r'^view/$', views.view, name='view'),
    #url(r'^record/$', views.record, name='record'),
    url(r'^index/record/(?P<user_id>(\d+))/(?P<document_id>(\d+))/$', views.record, name='record'),
    url(r'^search/', views.search, name='search'),
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<document_id>[0-9]+)/[A-Z]+$', views.ind_record, name='ind_record'),
    url(r'^index/(?P<user_id>[0-9]+)/record/(?P<document_id>[0-9]+)/$', views.record, name='record'),
    url(r'^(?P<user_id>[0-9]+)/record/$', views.record, name='record'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    #url(r'^document/add/$', views.DocumentCreate.as_view(), name='document-add'),
    url(r'^create/$', views.CreateDocument.as_view(), name='create'),
    url(r'^delete/$', views.DocumentDelete.as_view(), name='document-delete'),
    url(r'^(?P<user_id>[0-9]+)/delete_document/(?P<document_id>[0-9]+)/$', views.delete_document, name='delete_document'),
    #url(r'^create/$', views.create, name='create'),


    url(r'^python/$', views.python, name='python'),
    #url(r'^(?P<user_id>[0-9]+)/python/(?P<document_id>[0-9]+)/$', views.python,name='python'),

    #url(r'^index/python/(?P<user_id>[0-9]+)/$', views.python, name='python'),
    url(r'^index/(?P<user_id>[0-9]+)/python/$', views.python, name='python'),
    #url(r'^(?P<user_id>[0-9]+)/(?P<document_id>[0-9]+)/python/$', views.python, name='python'),
    #url(r'^(?P<user_id>[0-9]+)/python/(?P<document_id>[0-9]+)/$', views.python, name='python'),
    #url(r'^python/(?P<user_id>(\d+))/(?P<document_id>(\d+))/$', views.python, name='python'),
    #url(r'^index/python/(?P<user_id>[0-9]+)/(?P<document_id>[0-9]+)/$', views.python, name='python'),


    #url(r'^first/login/$', views.LoginFormView.as_view, name='login'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^document/(?P<user_id>[0-9]+)/delete/$', views.DocumentDelete.as_view(), name='document-delete'),
]
