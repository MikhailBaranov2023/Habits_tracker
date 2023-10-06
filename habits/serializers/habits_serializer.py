from rest_framework import serializers
from habits.models import Habit
from habits.validators import GoodHabitValidator, HabitLimitValidator, HabitPeriodValidator, LinkedHabitIsGoodValidator, \
    LinkedAndAwardValidator


class HabitSerializer(serializers.ModelSerializer):
    """ Base serializer class for habit with validators"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            LinkedAndAwardValidator(),
            HabitLimitValidator(limit_time='limit_time'),
            LinkedHabitIsGoodValidator(habit_link='habit_link'),
            HabitPeriodValidator(periodicity='periodicity'),
            GoodHabitValidator(habit_link='habit_link', award='award', good_habit='good_habit'),
        ]
