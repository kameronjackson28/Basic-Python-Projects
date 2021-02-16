from django.db import models


# creates class and columns for user input
class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=100, default="", blank=False)
    duration = models.FloatField()

    # gives a model manager
    classes = models.Manager()

    # assigns a proper description of the object on Admin page
    def __str__(self):
        return self.title
