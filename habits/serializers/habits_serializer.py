from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ Base serializer class for habit"""

    class Meta:
        model = Habit
        fields = "__all__"
