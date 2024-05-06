from rest_framework import serializers

from Quote_api.models import Quotes  # Assuming Quotes is defined in another file within the app



class quoteSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quotes
        fields="__all__"