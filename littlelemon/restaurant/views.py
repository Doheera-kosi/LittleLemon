from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu
from .serializers import MenuSerializer

# Create your views here.
def index(request):
  return render(request, 'index.html', {})


# MENUITEM
class MenuItemView(ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer
  
# SingleMenuItemView
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer