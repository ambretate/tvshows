from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import TVshow
from .serializers import TVshowSerializer

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