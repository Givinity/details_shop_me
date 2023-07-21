import io

from rest_framework import serializers

from details_shop_me.apps.detailapp.models import Details


class DetailsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.
                                   CurrentUserDefault())

    class Meta:
        model = Details
        fields = '__all__'
