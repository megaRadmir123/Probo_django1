from django.db import models

# Create your models here.
class Zametka(models.Model):
    text = models.CharField(max_length=150)
    td = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Название заметок"
    def __str__(self):
        return self.text
class Podrobnee(models.Model):
    zametka = models.ForeignKey(Zametka,on_delete=models.PROTECT)
    text = models.TextField()
    td = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "подробности"
    def __str__(self):
        return self.text[:31]+"..."