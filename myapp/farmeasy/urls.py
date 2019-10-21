from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings

urlpatterns= [
path('',(views.index), name='index'),
path('market.html',(views.posting),name='market'),
path('market2.html',(views.farm),name='market2')
]
urlpatterns += static((settings.STATIC_URL), document_root=(settings.STATIC_ROOT))
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static((settings.MEDIA_URL), document_root=(settings.MEDIA_ROOT))
