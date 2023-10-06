from rest_framework import generics
from habits.serializers.habits_serializer import HabitSerializer
from habits.models import Habit
from rest_framework.permissions import IsAuthenticated, AllowAny
from habits.permissions.permissions import IsOwner
from habits.paginations import HabitPaginator


class HabitListAPIView(generics.ListAPIView):
    """list of my habits"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """list of public habits"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(public=True)
    permission_classes = [AllowAny]
    pagination_class = HabitPaginator


class HabitCreateAPIView(generics.CreateAPIView):
    """create habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habits = serializer.save()
        new_habits.owner = self.request.user
        new_habits.save()


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """detail info about the habits"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """removing the habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """update the habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]
