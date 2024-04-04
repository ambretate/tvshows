from django.urls import path
from .views import Home,TVshowList, TVshowDetail, ViewingListCreate, ViewingDetail, CastListCreate, CastDetail, AddCastToShow, RemoveCastFromShow

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tvshows/', TVshowList.as_view(), name='tvshow-list'),
    path('tvshows/<int:id>/', TVshowDetail.as_view(), name='tvshow-detail'),
    path('tvshows/<int:show_id>/viewings/', ViewingListCreate.as_view(), name='viewing-list-create'),
    path('tvshows/<int:show_id>/viewings/<int:id>/', ViewingDetail.as_view(), name='viewing-detail'),
    path('cast/', CastListCreate.as_view(), name='cast-list-create'),
    path('cast/<int:cast_id>/', CastDetail.as_view(), name='cast-detail'),
    path('tvshows/<int:show_id>/add_cast/<int:cast_id>/', AddCastToShow.as_view(), name='add-cast-to-show'),
    path('tvshows/<int:show_id>/remove_cast/<int:cast_id>/', RemoveCastFromShow.as_view(), name='remove-cast-from-show')
]