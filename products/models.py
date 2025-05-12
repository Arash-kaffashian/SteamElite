from django.db import models
from django.utils.translation import gettext_lazy as _

from .API import turkey_price, brazil_price, global_price


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(_('title'), max_length=70)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    product_id = models.PositiveIntegerField(_('product id'), blank=True, null=True)

    price_tr = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    price_br = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    price_global = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    def update_prices(self):
        self.price_tr = turkey_price(self.product_id)
        self.price_br = brazil_price(self.product_id)
        self.price_global = global_price(self.product_id)
        self.save()

    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('category', verbose_name='categories', blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_IMAGE = 4
    FILE_TYPES = (
        (FILE_AUDIO, _('audio')),
        (FILE_VIDEO, _('video')),
        (FILE_PDF, _('pdf')),
        (FILE_IMAGE, _('image'))
    )

    product = models.ForeignKey(Product, verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file_type = models.PositiveSmallIntegerField(_('file type'), choices=FILE_TYPES, default=1)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/%file_type')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.title
