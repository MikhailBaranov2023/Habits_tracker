from rest_framework import generics
from habits.serializers.habits_serializer import HabitSerializer
from habits.models import Habit


class HabitListAPIView(generics.ListAPIView):
    """list of all habits"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitCreateAPIView(generics.CreateAPIView):
    """create habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """detail info about the habits"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDeleteAPIView(generics.DestroyAPIView):
    """removing the habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """update the habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
