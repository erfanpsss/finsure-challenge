from django.db import models

class Lender(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    upfront_commission_rate = models.FloatField()
    trial_commission_rate = models.FloatField()
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Lender"
        verbose_name_plural = "Lenders"


    def __str__(self):
        return self.name
    

