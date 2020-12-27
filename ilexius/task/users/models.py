from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

alphanumeric = RegexValidator(r'^[a-zA-Z0-9]*$', 'alphanumeric characters')

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, blank=True, unique=True, validators=[alphanumeric])
    login_count = models.PositiveIntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_employee(sender, instance, **kwargs):
    instance.employee.save()

def login_user(request, user, **kwars):
    user.employee.login_count = user.employee.login_count + 1
    user.employee.save()

user_logged_in.connect(login_user)
