from django.db import models


# Create your models here.

class TrainRecord(models.Model):
    def __str__(self):
        return ';'.join((str(self.dt), self.user_name, self.picture_name, self.permutation))

    dt = models.DateTimeField('date inserted')
    user_name = models.CharField(max_length=100)
    picture_name = models.CharField(max_length=100)
    permutation = models.CharField(max_length=100)
    initial_permutation = models.CharField(max_length=100)
