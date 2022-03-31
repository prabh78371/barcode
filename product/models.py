from django.db import models
import barcode

from io import BytesIO
from barcode.writer import ImageWriter

from django.core.files import File

class BC(models.Model):
    name = models.CharField(max_length=100)
    bcode = models.ImageField(upload_to='images',blank=True)

    def save(self,*args,**kwargs):
        pr=barcode.get_barcode_class('EAN13')
        Ean = pr('1234567892345',writer = ImageWriter())
        buffer = BytesIO()
        Ean.write(buffer)
        self.bcode.save('barcode.png',File(buffer),save=False)
        return super().save(*args,**kwargs)