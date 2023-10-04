from django.urls import path
from habits.apps import HabitsConfig
from habits.views.habits_views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveApiView, HabitDeleteAPIView, \
    HabitUpdateAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('view/<int:pk>/', HabitRetrieveApiView.as_view(), name='habit_view'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit_delete'),
]
