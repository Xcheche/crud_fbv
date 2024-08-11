from django.db import models


# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    test_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.first_name
