from django.db import models



class Announcement(models.Model):
    describe = models.TextField()
    date_reg = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    
    def __str__(self):
        return self.describe
