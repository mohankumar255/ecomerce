from django.db import models
from django.utils import timezone
# Create your models here.
#create our register model here
class types(models.Model):
    product_type=models.CharField(max_length=100)
    def __str__(self):
        return self.product_type
class items(models.Model):
    product_type=models.ForeignKey(types,on_delete=models.CASCADE)
    desecription=models.CharField(max_length=100)
    item_name=models.CharField(max_length=50)
    #quantity=models.IntegerField(default=1)
    rate=models.IntegerField()
    image=models.ImageField(upload_to='pics/%y/%m/%d',null=False,blank=True)

    def __str__(self):
        return self.item_name
class save_order(models.Model):
    date=models.DateField(default=timezone.now())
    state1=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    types1=models.CharField(max_length=50)
    item_id=models.CharField(max_length=100000)
    item_name=models.CharField(max_length=50)
    quantity=models.IntegerField(default=1)
    completed = models.BooleanField(default=False)
    rate=models.IntegerField()
    #image=models.ImageField(upload_to='pics',blank=True,null=True)
    total=models.IntegerField()
    name1=models.CharField(max_length=20)
    contact1=models.CharField(max_length=10)
    contact2=models.CharField(max_length=10)
    address=models.TextField(max_length=500)
    pincode=models.IntegerField()
    def __str__(self):
        return self.name1