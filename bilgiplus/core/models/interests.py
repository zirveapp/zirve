from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'interests'
        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'

    def __str__(self):
        return self.name