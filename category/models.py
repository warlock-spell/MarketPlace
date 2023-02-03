from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=False)

    # override the default get_absolute_url method
    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"slug": self.slug})

    # override the default save method
    def save(self, *args, **kwargs):
        # if the slug is not present, then generate it
        if not self.slug:
            self.slug = slugify(self.name)
        # super() to make sure that the save method of the parent class is also called
        # it is important to call the save method of the parent class, because it will save the object in the database
        # note that we are forwarding the arguments to the save method of the parent class
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name',)

    def __str__(self):
        return self.name
