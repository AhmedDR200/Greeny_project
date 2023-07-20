from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

FLAG_OPTION=(
     ('New','New'),
     ('Feature','Feature'),
     ('Sale','Sale'),

)



class Products (models.Model):
    name = models.CharField(max_length=100 , verbose_name=_("Name"))
    subtitle = models.CharField(_("Subtitle"),max_length=500)
    sku = models.IntegerField(_("SKU"))
    desc = models.TextField(_('Description'), max_length=10000)
    price = models.models.FloatField(_("Price"))
    flag = models.CharField(_("Flag"), max_length=10 , choices=FLAG_OPTION)
    quantity = models.IntegerField(_("Quantity"))
    brand =''
    category = ''



class ProducstImages(models.Model):
    pass



class Brand(models.Model):
    pass


class Category(models.Model):
    pass



class ProductReview(models.Model):
    pass