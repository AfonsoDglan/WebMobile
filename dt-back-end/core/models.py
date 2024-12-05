from django.db import models
import uuid


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('outcome', 'Outcome'),
    )

    id = models.CharField(max_length=10, primary_key=True, editable=False)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Gera um ID curto se for uma nova transação
            self.id = str(uuid.uuid4())[:4]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.price}"
