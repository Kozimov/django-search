from django.db import models

class Works(models.Model):
    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Ishchilar"

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    job = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)