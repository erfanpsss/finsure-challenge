from rest_framework import serializers
from .models import Lender


class LenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lender
        fields = "__all__"



