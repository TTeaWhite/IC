from django.db import models

# Create your models here.
class inventory_list(models.Model):
    inv_no = models.CharField(max_length=10)
    loc = models.CharField(max_length=10)
    user = models.CharField(max_length=20)
    des = models.TextField()
    brand = models.CharField(max_length=20)
    price = models.IntegerField()
    date_purchase = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'inventories'

    def __str__(self):
        return 'Inventory #{}'.format(self.id)