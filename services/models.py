from django.db import models

class Service(models.Model):
    title = models.CharField("Название услуги", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.title