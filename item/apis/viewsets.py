from urllib import request
from rest_framework import viewsets, status
from item.apis.permissions import ItemPermission
from item.models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response


class ItemViewset(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (ItemPermission, )

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        user = request.user.uuid
        data['user'] = user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
