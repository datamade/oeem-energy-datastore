from django.conf.urls import url
from datastore import views

urlpatterns = [
    url(r'^consumption/$', views.ConsumptionMetadataList.as_view()),
    url(r'^consumption/(?P<pk>[0-9]+)/$', views.ConsumptionMetadataDetail.as_view()),
    url(r'^project/$', views.ProjectList.as_view()),
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
]
