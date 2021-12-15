from django.db import models

# Класс, для хранения url адреса ngrok
class NgrokUrl(models.Model):
    NgrokUrl = models.CharField(max_length=300)

    def __str__(self):
        return self.NgrokUrl
