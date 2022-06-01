from rest_framework import serializers
from account.models import User
from item.models import Item

class ItemSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='uuid')
    url = serializers.HyperlinkedIdentityField(
        view_name="items-detail", lookup_field="uuid")
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='uuid',
        required=True
    )

    class Meta:
        model = Item
        fields = ('id', 'url', 'user', 'name', 'scheduled_at', 'status')
