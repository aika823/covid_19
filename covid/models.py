from django.db import models


class User(models.Model):
    gender = models.CharField(max_length=1, null=False)
    age = models.CharField(max_length=10, null=False)
    underlying = models.CharField(max_length=10, null=False)
    class Meta:
        db_table = 'user'

class Vaccination(models.Model):
    user = models.ForeignKey(to=User, db_column='user', null=False, on_delete=models.CASCADE)
    vaccine_times = models.IntegerField(null=False)
    vaccine_name = models.CharField(max_length=20, null=False)
    class Meta:
        db_table = 'vaccination'

class SideEffect(models.Model):
    side_effect_code = models.CharField(max_length=1)
    side_effect_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'side_effect'

class VaccinationSideEffect(models.Model):
    vaccination = models.ForeignKey(to=Vaccination, db_column='vaccination', null=False, on_delete=models.CASCADE)
    side_effect = models.ForeignKey(to=SideEffect, db_column='side_effect', null=True, on_delete=models.CASCADE)
    side_effect_etc = models.CharField(max_length=200, null=True, default=None)
    class Meta:
        db_table = 'vaccination_side_effect'
