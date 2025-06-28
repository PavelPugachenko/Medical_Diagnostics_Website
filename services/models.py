from django.db import models


class Service(models.Model):
    title = models.CharField("Название услуги", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="services/", null=True, blank=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"

    def __str__(self):
        return f"Сообщение от {self.name}"
