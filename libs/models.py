from django.db import models 
from django.utils import timezone 


class CommonAbstract(models.Model):
    created_at = models.DateTimeField(editable=False, null=True, blank=True, verbose_name='Thời điểm tạo')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')


    class Meta:
        ordering = ['-created_at',]
        abstract = True 

    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super(CommonAbstract, self).save(*args, **kwargs)


class SEOAbstract(models.Model):
    meta_title = models.TextField(verbose_name='SEO Title', null=True, blank=True)
    meta_desc = models.TextField(verbose_name='SEO Description', null=True, blank=True)
    meta_keywords = models.TextField(verbose_name='SEO Keywords', null=True, blank=True)


    class Meta:
        abstract = True 
