from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import TVshow, Viewing
from .serializers import TVshowSerializer, ViewingSerializer

# Create your views here.
class Home(APIView):
    def get(self, request):
        content = {'message: Welcome to the TV Shows API home route'}
        return Response(content)
    
class TVshowList(generics.ListCreateAPIView):
    queryset = TVshow.objects.all()
    serializer_class = TVshowSerializer

class TVshowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TVshow.objects.all()
    serializer_class = TVshowSerializer
    lookup_field = 'id'

class ViewingListCreate(generics.ListCreateAPIView):
    serializer_class = ViewingSerializer

    def get_queryset(self):
        show_id = self.kwargs['show_id']
        return Viewing.objects.filter(show_id=show_id)
    
    def perform_create(self, serializer):
        show_id = self.kwargs['show_id']
        show = TVshow.objects.get(id=show_id)
        serializer.save(show=show)

class ViewingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ViewingSerializer
    lookup_field = 'id'

    def get_queryset(self):
        show_id = self.kwargs['show_id']
        return Viewing.objects.filter(show_id=show_id)