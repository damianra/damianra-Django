from btcdata.models import BtcData
from rest_framework import serializers

class BtcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BtcData
        fields = ['date', 'price', 'var']