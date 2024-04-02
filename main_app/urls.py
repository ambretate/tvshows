from django.urls import path
from .views import Home,TVshowList, TVshowDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tvshows/', TVshowList.as_view(), name='tvshow-list'),
    path('tvshows/<int:id>/', TVshowDetail.as_view(), name='tvshow-detail'),
]