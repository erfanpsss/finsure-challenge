from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Lender
from io import StringIO
import csv

class LenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lender
        fields = "__all__"

class LenderBulkSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        csv_data = csv.DictReader(StringIO(value.read().decode('utf-8')))
        return csv_data

    def create(self, validated_data):
        report = {
            "created_count": 0,
            "failed_count": 0,
            "failed_items": []
        }
        for lender in validated_data.get("file"):
            try:
                Lender.objects.create(
                    name=lender.get("name"),
                    code=lender.get("code"),
                    upfront_commission_rate=lender.get("upfront_commission_rate"),
                    trial_commission_rate=lender.get("trial_commission_rate"),
                    active=True if lender.get("active", "").lower() == "true" else False
                )
                report["created_count"] += 1
            except Exception as error:
                report["failed_count"] += 1
                report["failed_items"].append(f'{", ".join(lender)}, error: {str(error)}')
        return report