from django.db import models


class Todo(models.Model):
    class Meta(object):
        db_table = "todo"

    title = models.CharField(blank=False, null=False, max_length=50, db_index=True)
    description = models.TextField()
    is_completed = models.BooleanField(blank=False, null=False, default=False)
    created_at = models.DateTimeField("Created Datetime", blank=True, auto_now_add=True)
    updated_at = models.DateTimeField("Updated Datetime", blank=True, auto_now=True)

    def __str__(self) -> str:
        return self.title
