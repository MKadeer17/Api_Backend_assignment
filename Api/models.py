from django.db import models


# Create your models here.
class Members(models.Model):
    # For Timezone
    import pytz
    real_name = models.CharField(max_length=100)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    tz = models.CharField(max_length=50, choices=TIMEZONES)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):

    members = models.ForeignKey(Members, null=True, on_delete=models.CASCADE, related_name='activity_periods')

    start_time = models.DateTimeField(auto_now=False, null=True)
    end_time = models.DateTimeField(auto_now=False, null=True)

