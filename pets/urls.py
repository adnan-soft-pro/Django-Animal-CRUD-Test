from pets import views
from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', views.ApiHome.as_view()),
    url(r'^list/$', views.PetListView.as_view()),
    url(r'^create/$', views.PetCreateView.as_view()),
    url(r'^edit/(?P<pk>.+)/$', views.PetRetrieveUpdateDestroyView.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
