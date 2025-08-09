# from django.conf import settings
# from django.db import models
# from django.contrib.auth.models import User
#
#
# class AdvertisementStatusChoices(models.TextChoices):
#     """Статусы объявления."""
#
#     OPEN = "OPEN", "Открыто"
#     CLOSED = "CLOSED", "Закрыто"
#     DRAFT = "DRAFT", 'Черновик'
#
#     STATUS_CHOICES = [
#         (OPEN, 'Открыто'),
#         (CLOSED, 'Закрыто'),
#         (DRAFT, 'Черновик'),  # Для дополнительного задания
#     ]
#
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=OPEN)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Advertisement(models.Model):
#     """Объявление."""
#
#     title = models.TextField()
#     description = models.TextField(default='')
#     status = models.TextField(
#         choices=AdvertisementStatusChoices.choices,
#         default=AdvertisementStatusChoices.OPEN
#     )
#     creator = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True
#     )


from django.db import models
from django.contrib.auth.models import User


class Advertisement(models.Model):
    class AdvertisementStatusChoices(models.TextChoices):
        OPEN = 'OPEN', 'Открыто'
        CLOSED = 'CLOSED', 'Закрыто'
        DRAFT = 'DRAFT', 'Черновик'  # Для дополнительного задания

    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title