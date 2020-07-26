from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid

# Create your models here.

class cabana(models.Model):
    ubicacion = models.CharField(max_length=100)
    texto = models.TextField(max_length=500)
    slug = models.SlugField(null=False, unique=True, blank=False)
    fecha = models.DateField()
    image_main = models.ImageField(upload_to='cabanas/', null=False, blank=False, verbose_name="Imagen principal (Primera a ver)")
    image_1 = models.ImageField(upload_to='cabanas/', verbose_name="Imagen 1", null=True, blank=True)
    image_2 = models.ImageField(upload_to='cabanas/', verbose_name="Imagen 2", null=True, blank=True)
    image_3 = models.ImageField(upload_to='cabanas/', verbose_name="Imagen 3", null=True, blank=True)
    image_4 = models.ImageField(upload_to='cabanas/', verbose_name="Imagen 4", null=True, blank=True)
    image_5 = models.ImageField(upload_to='cabanas/', verbose_name="Imagen 5 (La foto más grande)", null=True, blank=True)
    


def set_slug(sender, instance, *args, **kwargs): 

    if instance.ubicacion and not instance.slug:
        slug = slugify(instance.ubicacion)

        while cabana.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.ubicacion, str(uuid.uuid4())[:4])
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=cabana)


class plano(models.Model):
    ubicacion = models.CharField(max_length=100)
    texto = models.TextField(max_length=500)
    slug = models.SlugField(null=False, unique=True, blank=False)
    image_main = models.ImageField(upload_to='planos/', null=False, blank=False, verbose_name="Imagen principal (Primera a ver)")
    image_1 = models.ImageField(upload_to='planos/', verbose_name="Imagen 1", null=True, blank=True)
    image_2 = models.ImageField(upload_to='planos/', verbose_name="Imagen 2", null=True, blank=True)
    image_3 = models.ImageField(upload_to='planos/', verbose_name="Imagen 3", null=True, blank=True)
    image_4 = models.ImageField(upload_to='planos/', verbose_name="Imagen 4", null=True, blank=True)
    image_5 = models.ImageField(upload_to='planos/', verbose_name="Imagen 5 (La foto más grande)", null=True, blank=True)

def set_slug_plano(sender, instance, *args, **kwargs): 

    if instance.ubicacion and not instance.slug:
        slug = slugify(instance.ubicacion)

        while plano.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.ubicacion, str(uuid.uuid4())[:4])
            )

        instance.slug = slug

pre_save.connect(set_slug_plano, sender=plano)



