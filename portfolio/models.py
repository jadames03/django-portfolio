from django.db import models

# Create your models here.
PROJECT_TYPE = (
    ('DEV','Development'),
    ('UI/UX','UI/UX Design'),
    ('CV','Computer Vision'),
)

class Project(models.Model):
    title = models.CharField(max_length=100)
    project_type =  models.CharField(max_length=10, choices=PROJECT_TYPE, default='DEV')
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title