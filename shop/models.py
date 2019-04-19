from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)

    class Meta:
        ordering=['name']
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category',args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    
    #image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image = ProcessedImageField(upload_to='products/%Y/%m/%d', processors=[Thumbnail(100, 100)],
            format='JPEG', options={'quality':60}, blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    avaliable_display = models.BooleanField('Display',default = True)
    avaliable_order = models.BooleanField('Order',default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-created_at']
        index_together = [['id','slug']]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id,self.slug])
    
    