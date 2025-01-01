from django.db import models 
from libs.models import CommonAbstract 
from django.contrib.auth.models import User 
from core.models.research_document import ResearchDocument 


class Review(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    document = models.ForeignKey(ResearchDocument, on_delete=models.CASCADE, verbose_name='Document')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Account')
    content = models.TextField(verbose_name='Review Content')


    class Meta:
        ordering = ['-created_at', 'document', 'user']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        db_table = 'reviews'
