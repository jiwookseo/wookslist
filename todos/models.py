from django.db import models
from django.contrib.auth import get_user_model


class List(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='lists')

    def __str__(self):
        return f"{self.user.username}'s {self.title} List"


class Todo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default="", blank=True)
    check = models.BooleanField(default=False)
    due_date = models.DateField(blank=True, null=True)
    important = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="todos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.list.user.username}'s Todo : {self.title}"

    class Meta:
        ordering = ['-id']
