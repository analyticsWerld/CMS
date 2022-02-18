from django.db import models
from membership.models import Member
type_options = [("GIVING","Giving"),("DONATION", "Donation"),("WITHDRAWAL","Withdrawal")]
status = [("PRESENT","Present"),("ABSENT","Absent")]
time_slots = (
    ('7:00 - 8:00', '7:00 - 8:00'),
    ('6:30 - 7:30', '6:30 - 7:30'),
    ('8:30 - 10:30', '8:30 - 10:30'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

worship_days = (
    ('Monday', 'Monday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


class Attendance(models.Model):
    
    describe = models.TextField()
    time_reg = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    present = models.BooleanField(choices=status)
    
    def __str__(self):
        return self.describe
