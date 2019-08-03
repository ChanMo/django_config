from django.db import models
from django.utils.translation import gettext_lazy as _

class ConfigManager(models.Manager):
    def get_value(self, code):
        """
        获取配置值, 如果不存在, 返回None
        """
        try:
            value = self.get(code = code)
            return value.value
        except:
            return None


class Config(models.Model):
    code = models.CharField(_('code'), max_length=100, unique=True)
    value = models.CharField(_('value'), max_length=200, blank=True, null=True)
    description = models.TextField(_('description'), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ConfigManager()

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['-created']
        verbose_name = _('config')
        verbose_name_plural = _('config')
