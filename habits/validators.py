from rest_framework.validators import ValidationError
from habits.models import Habit


class LinkedAndAwardValidator:

    def __call__(self, value):
        habit_link_val = dict(value).get('habit_link')
        award_val = dict(value).get('award')

        if habit_link_val and award_val:
            raise ValidationError('You cannot select a related habit and reward at the same time.')


class HabitLimitValidator:
    def __init__(self, limit_time):
        self.limit_time = limit_time

    def __call__(self, value):
        limit_time_val = dict(value).get(self.limit_time)
        if isinstance(limit_time_val, int) and limit_time_val > 120:
            raise ValidationError("The execution time should be no more than 120 seconds.")


class HabitPeriodValidator:
    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, value):
        periodicity_val = dict(value).get(self.periodicity)
        if isinstance(periodicity_val, int) and periodicity_val < 7:
            raise ValidationError("You cannot perform the habit less than once every 7 days.")


class LinkedHabitIsGoodValidator:
    def __init__(self, habit_link):
        self.habit_link = habit_link

    def __call__(self, value):
        habit_link_val = dict(value).get(self.habit_link)
        if habit_link_val:
            habit = Habit.objects.get(pk=habit_link_val.id)
            if not habit.good_habit:
                raise ValidationError("In a bound habit can only be a good habit")


class GoodHabitValidator:
    def __init__(self, good_habit, habit_link, award):
        self.good_habit = good_habit
        self.habit_link = habit_link
        self.award = award

    def __call__(self, value):
        good_habit_val = dict(value).get(self.good_habit)
        habit_link_val = dict(value).get(self.habit_link)
        award_val = dict(value).get(self.award)

        if good_habit_val and habit_link_val or good_habit_val and award_val:
            raise ValidationError("A good habit cannot have a award and an habit link.")
