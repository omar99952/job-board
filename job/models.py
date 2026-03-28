from django.db import models
from django.utils.text import slugify
# Create your models here.

Job_Type = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def save_photo(instance,file_name):
    phota_name,extension = file_name.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class job(models.Model):
    # Properties
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices = Job_Type)
    description = models.TextField(max_length = 50)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=save_photo)
    slug = models.SlugField(blank=True , null=True)
    # category --> Foriegn Key
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    #  Methods
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args,**kwargs)

# *******************************************************************************

class Category(models.Model):
    category = models.CharField(max_length=15)
    
    def __str__(self):
        return self.category
    


class Applications(models.Model):
    job = models.ForeignKey("job", verbose_name=("jobTable"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField(max_length=50)
    cv = models.FileField(upload_to="apply/")
    coverletter = models.TextField(max_length=200)

    def __str__(self):
        return self.name