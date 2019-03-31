from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photo', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' tem a idade de ' + str(self.age) + ' e ganha ' + str(self.salary)