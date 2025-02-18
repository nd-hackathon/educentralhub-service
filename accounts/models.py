from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    STUDENT = 1
    HEADMASTER = 2
    TEACHER = 3
    
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (HEADMASTER, 'headmaster'),
        (TEACHER, 'teacher'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    school_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    roles = models.ManyToManyField(Role, related_name="users", blank=True)

    @property
    def is_student(self):
        return self.roles.filter(id=Role.STUDENT).exists()

    @property
    def is_headmaster(self):
        return self.roles.filter(id=Role.HEADMASTER).exists()

    @property
    def is_teacher(self):
        return self.roles.filter(id=Role.TEACHER).exists()
