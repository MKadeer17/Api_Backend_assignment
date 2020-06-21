from rest_framework import serializers
from .models import *


class APSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class MemberSerializer(serializers.ModelSerializer):
    activity_periods = APSerializer(many=True)

    class Meta:
        model = Members
        fields = ['id', 'real_name', 'tz', 'activity_periods']





