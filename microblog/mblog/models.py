# /usr/bin/python
#! coding = 'utf-8'

from django.db import models

# Create your models here.

class MBlog(models.Model) : 
    content = models.TextField(default = u'没有内容', verbose_name = u'内容')
    time = models.DateTimeField(auto_now = True, verbose_name = u'时间')

    def __unicode__(self) : 
        return self.content[0:5] + '...'
