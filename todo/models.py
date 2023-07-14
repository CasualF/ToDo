from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ToDo(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_todos', blank=True, null=True)
    responsible_for_task = models.ForeignKey('auth.User', on_delete=models.SET_NULL, related_name='todos', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='todos', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        now = timezone.now()
        return f'{self.category} | {self.title} {"✅" if self.is_done else ""} ' \
               f'{(self.deadline - now) if self.deadline and self.deadline>now else "Time is up" if self.deadline else ""}'

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo\'s'
