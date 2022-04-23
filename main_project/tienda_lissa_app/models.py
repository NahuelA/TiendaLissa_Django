from django.db import models

# Create your models here.

class ModelSales(models.Model):

    id = models.BigAutoField(db_column="ID",
                            primary_key=True,
                            unique=True,
                            db_index=True)
    date_creation = models.DateTimeField(verbose_name="Fecha de creación",
                                        auto_now_add=True)
    name = models.CharField(verbose_name="Nombre del cliente",
                            max_length=35,
                            db_index=True)
    description = models.CharField(verbose_name="Descripción del producto",
                                    max_length=300,
                                    db_index=True)
    count = models.PositiveIntegerField(verbose_name="Cantidad",db_index=True)
    price = models.DecimalField(verbose_name="Precio",
                                default=0.00,
                                max_digits=10,
                                decimal_places=2,
                                db_index=True,)

    paid_out = models.BooleanField(verbose_name="Pagado",default="Pagado", db_index=True)
    total = models.FloatField(verbose_name="Total",default=0.00, db_index=True)

    class Meta:
        db_table = "tienda_lissa_table"