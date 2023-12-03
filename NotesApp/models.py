from django.db import models

class Nota(models.Model):
    data_adaugare = models.DateTimeField(auto_now_add=True, blank=True)
    titlu = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.titlu} {self.text}"
