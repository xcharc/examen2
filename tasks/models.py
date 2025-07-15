from django.db import models
class PendingTask(models.Model):
    api_id = models.IntegerField(unique=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.api_id} - {self.title}"