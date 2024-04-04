from django.urls import path
from .views import Home,TVshowList, TVshowDetail, ViewingListCreate, ViewingDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tvshows/', TVshowList.as_view(), name='tvshow-list'),
    path('tvshows/<int:id>/', TVshowDetail.as_view(), name='tvshow-detail'),
    path('tvshows/<int:show_id>/viewings/', ViewingListCreate.as_view(), name='viewing-list-create'),
    path('tvshows/<int:show_id>/viewings/<int:id>/', ViewingDetail.as_view(), name='viewing-detail')
]