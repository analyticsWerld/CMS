from django.utils import timezone
from django.db import models
from membership.models import Member

Status = [("PRESENT","Present"),("ABSENT","Absent")]


class Attendance(models.Model):
    
    describe = models.TextField(blank=True,null=True)
    time_reg = models.DateTimeField(blank=True,null=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    status = models.CharField(choices=Status,max_length=10)
    
    def __str__(self):
        return self.describe
