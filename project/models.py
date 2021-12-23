from django.db import models



# Create your models here.
class Project(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=4048)
    duration_in_days = models.IntegerField()
    avatar = models.ImageField(upload_to='project_avatar')

    def __str__(self):return self.name

    class Meta:
        verbose_name_plural = 'Project'

class Task(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    assigned_to = models.ForeignKey(Project,on_delete=models.CASCADE,default=None,null=True)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=4048)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):return self.name
    class Meta:
        verbose_name_plural = 'Tasks'
