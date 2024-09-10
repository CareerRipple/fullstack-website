from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as DjangoUser


class Project(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField()
    description = models.TextField()
    category = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    posted_date = models.DateField()
    start_date = models.DateField()
    deadline = models.DateField()
    lead = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    meeting_time = models.DateTimeField()
    meeting_platform = models.CharField(max_length=100)
    project_length = models.DurationField()
    phase = models.IntegerField()
    availability_per_week = models.DurationField()

    def __str__(self):
        return f"{self.title}, {self.category}"

class Role(models.Model):
    title = models.CharField(max_length=255)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    class MentorshipStatus(models.TextChoices):
        MENTOR = 'mentor', 'Mentor'
        MENTEE = 'mentee', 'Mentee'
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    location = models.CharField(max_length=100)
    mentorship = models.CharField(max_length=6, choices=MentorshipStatus.choices, default=MentorshipStatus.MENTEE)
    timezone = models.DateTimeField(default=timezone.now)
    headline = models.CharField(max_length=250)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    biography = models.TextField()
    occupation = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    linkedin_link = models.URLField()
    portfolio_link = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name}, {self.user.last_name}: {self.role}"


class Education(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=150)
    enter_year = models.DateField()
    graduation_year = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.institution
    

class Experience(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company = models.CharField(max_length=150)
    start_year = models.DateField()
    end_year = models.DateField(null=True, blank=True)
    accomplishment = models.TextField()

    def __str__(self):
        return self.company


class Skill(models.Model):
    user = models.ManyToManyField(UserProfile)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title