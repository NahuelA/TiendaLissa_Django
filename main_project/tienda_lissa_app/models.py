from django.db import models

# Create your models here.

class TiendaLissa(models.Model):

    id = models.BigAutoField(db_column="id",
                            primary_key=True,
                            unique=True)
    date_creation = models.DateTimeField(verbose_name="date_creation",
                                        auto_now_add=True)
    name = models.CharField(verbose_name="name_of_client",
                            max_length=35)
    description = models.CharField(verbose_name="description_product",
                                    max_length=300)
    count = models.PositiveIntegerField(verbose_name="count")
    price = models.FloatField(verbose_name="price",default=0.00)
    paid_out = models.BooleanField(verbose_name="paid_out",default=True)
    total = models.FloatField(verbose_name="total",default=0.00)

    class Meta:
        db_table = "tienda_lissa_table"