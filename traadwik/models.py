from django.db import models

class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=5000)
    slug=models.CharField(max_length=5000,unique=True)
    publish_date=models.DateField(auto_now_add =True)
    def __str__(self):
        return (f"{self.name}  Update at -({self.publish_date})")

class ProductCategory(models.Model):
    id=models.AutoField(primary_key=True)
    brand_name=models.CharField(max_length=5000)
    name=models.CharField(max_length=5000)
    slug=models.CharField(max_length=5000,unique=True)
    description=models.CharField(max_length=5000)
    img=models.ImageField( upload_to='priceList/img', height_field=None, width_field=None, default='/noProductImage.png')
    publish_date=models.DateField(auto_now_add =True)
    def __str__(self):
        return (f"{self.name}  Update at -({self.publish_date})")

class PriceList(models.Model):
    id=models.AutoField(primary_key=True)
    brand_name=models.CharField(max_length=5000)
    img=models.ImageField( upload_to='priceList/img', height_field=None, width_field=None, default='/noProductImage.png')
    pdf=models.FileField(upload_to='priceList/documents')
    slug=models.CharField(max_length=5000,unique=True)
    publish_date=models.DateField(auto_now_add =True)
    def __str__(self):
        return (f"{self.brand_name}  Update at -({self.publish_date})")

class Jobs(models.Model):
    id=models.AutoField(primary_key=True)
    role=models.CharField(max_length=150)
    slug=models.CharField(max_length=150)
    location=models.CharField(max_length=1000)
    description_1=models.CharField(max_length=5000)
    description_2=models.CharField(max_length=5000,blank=True, null=True)
    description_3=models.CharField(max_length=5000,blank=True, null=True)
    description_4=models.CharField(max_length=5000,blank=True, null=True)
    description_5=models.CharField(max_length=5000,blank=True, null=True)
    publish_date=models.DateField(auto_now_add =True)
    contact_email=models.EmailField(default='careers@traadwik.com')
   
    def __str__(self):
        return (f"{self.role}-({self.publish_date})") 

class product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=5000)
    slug=models.CharField(max_length=5000,unique=True)
    short_description=models.CharField(max_length=10000)
    categoryChoice = (
               ('schneider','Schneider'),
               ('legrand','Legrand')
               )
    brand=models.CharField(max_length=8000,choices=categoryChoice,default='schneider')
    subcategory=models.CharField(max_length=8000,default='Schneider')
    img1=models.ImageField( upload_to='productImg/', height_field=None, width_field=None, default='/noProductImage.png')
    Feature_1_title=models.CharField(max_length=5000)
    Feature_1_description=models.CharField(max_length=10000)
    priceList=models.FileField(upload_to='priceList/documents')
    priceList_2=models.FileField(upload_to='priceList/documents',blank=True, null=True)
    priceList_3=models.FileField(upload_to='priceList/documents',blank=True, null=True)
    p_warranty=models.CharField(max_length=5000,blank=True, null=True)
    Feature_2_title=models.CharField(max_length=5000,blank=True, null=True)
    Feature_2_description=models.CharField(max_length=10000,blank=True, null=True)
    Feature_3_title=models.CharField(max_length=5000,blank=True, null=True)
    Feature_3_description=models.CharField(max_length=10000,blank=True, null=True)
    Feature_4_title=models.CharField(max_length=5000,blank=True, null=True)
    Feature_4_description=models.CharField(max_length=10000,blank=True, null=True)
    Feature_5_title=models.CharField(max_length=5000,blank=True, null=True)
    Feature_5_description=models.CharField(max_length=10000,blank=True, null=True)
    Full_1_description=models.CharField(max_length=10000,blank=True, null=True)
    Full_2_description=models.CharField(max_length=10000,blank=True, null=True)
    Full_3_description=models.CharField(max_length=10000,blank=True, null=True)
    Full_4_description=models.CharField(max_length=10000,blank=True, null=True)
    publish_date=models.DateField(auto_now_add =True)
    img2=models.ImageField( upload_to='productImg/', height_field=None, width_field=None,blank=True, null=True )
    img3=models.ImageField( upload_to='productImg/', height_field=None, width_field=None,blank=True, null=True )
    img4=models.ImageField( upload_to='productImg/', height_field=None, width_field=None,blank=True, null=True )
    img5=models.ImageField( upload_to='productImg/', height_field=None, width_field=None,blank=True, null=True )
    img6=models.ImageField( upload_to='productImg/', height_field=None, width_field=None,blank=True, null=True )
    img7=models.ImageField( upload_to='productImg/', height_field=None, width_field=None,blank=True, null=True )
    img8=models.ImageField( upload_to='productImg/', height_field=None, width_field=None,blank=True, null=True )

    def __str__(self):
        return (f"{self.name}-{self.subcategory}-{self.brand}-({self.publish_date})") 
