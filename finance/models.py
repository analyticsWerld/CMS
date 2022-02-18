from django.db import models


class Finance(models.Model):
    type_options = [("GIVING","Giving"),("DONATION", "Donation"),("WITHDRAWAL","Withdrawal")]
    describe = models.TextField()
    date_reg = models.DateTimeField(auto_now_add=True)
    did_by = models.CharField(max_length=250)
    amount = models.FloatField(max_length=250)
    type_of = models.CharField(choices=type_options, max_length=250)
    
    def __str__(self):
        return self.describe
