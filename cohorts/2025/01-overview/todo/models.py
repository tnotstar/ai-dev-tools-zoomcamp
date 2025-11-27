from django.db import models


# Create your models here.
class Todo(models.Model):
    """
    Represents a single TODO item.
    """

    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the model, which is used in the Django admin.
        """
        return self.title
