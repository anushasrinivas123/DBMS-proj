from django.db import models

# Create your models here.
class Customer1(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

class RoomType(models.Model):
    roomtypeid=models.AutoField(db_column='RoomTypeID', primary_key=True)
    roomtype=models.CharField(db_column='RoomType', max_length=20)
    def __str__(self):
        return self.roomtype
    class Meta:
        managed=True
        db_table = 'RoomType'