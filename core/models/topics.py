from django.db import models 
from libs.models import CommonAbstract 
from django.utils.text import slugify 
from random import randint


class Topic(CommonAbstract):
    id = models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Chủ đề', unique=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True, verbose_name='Slug')


    class Meta:
        ordering = ['-created_at', 'name']
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        db_table = 'topics'
    

    def __str__(self):
        return f"{self.id} - {self.name}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "_" + f"{randint(1000, 1000000)}"
        super(Topic, self).save(*args, **kwargs)
