from django.db import models 
from libs.models import CommonAbstract, SEOAbstract 
from libs.enum import DOCUMENT_STATUS
from django.utils.text import slugify 
from random import randint 
from django.contrib.auth.models import User 
from core.models.topics import Topic 


class ResearchDocument(CommonAbstract, SEOAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Account')
    title = models.CharField(max_length=255, verbose_name='Title')
    author = models.CharField(max_length=255, verbose_name='Author')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, verbose_name='Research Topic')
    summary = models.TextField(null=True, blank=True, verbose_name='Summary')
    pdf_docs = models.FileField(upload_to='documents/', null=True, blank=True, verbose_name='Document Upload')
    pdf_docs_img = models.ImageField(upload_to='docs_img/', null=True, blank=True, verbose_name='Doc Preview Image')
    thumb_img = models.ImageField(upload_to='thumb_img/', null=True, blank=True, verbose_name='Thumbnail Image')
    # detail = models.HTMLField()
    views_count = models.PositiveIntegerField(default=0, verbose_name='Views Count')
    downloads_count = models.PositiveIntegerField(default=0, verbose_name='Downloads Count')
    status = models.SmallIntegerField(default=0, choices=DOCUMENT_STATUS, verbose_name='Trạng thái tài liệu')
    slug = models.SlugField(max_length=300, verbose_name='Slug', null=True, blank=True)


    class Meta:
        ordering = ['-updated_at', '-created_at', 'topic', 'title', 'author', '-downloads_count', '-views_count',]
        verbose_name = 'Research Document'
        verbose_name_plural = 'Research Documents'
        db_table = 'documents'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + "_" + f"{randint(1000, 1000000)}.html"
        super(ResearchDocument, self).save(*args, **kwargs)


