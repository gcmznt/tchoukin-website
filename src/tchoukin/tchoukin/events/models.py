from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError


class Event(models.Model):
    name = models.CharField(verbose_name=_(u'Name of the event'), max_length=150, unique=True)
    website = models.URLField(verbose_name=_(u'Website'), max_length=255, blank=True)
    email = models.EmailField(verbose_name=_(u'Email'), max_length=255)
    from_date = models.DateField(verbose_name=_(u'From date'))
    to_date = models.DateField(verbose_name=_(u'To date'))

    address_address = models.CharField(verbose_name=_(u'Address'), max_length=2000)
    address_lat = models.FloatField(verbose_name=_(u'Latitude'))
    address_lon = models.FloatField(verbose_name=_(u'Longitude'))
    address_country = models.CharField(verbose_name=_(u'Country'), max_length=255, blank=True)
    address_locality = models.CharField(verbose_name=_(u'Locality'), max_length=255, blank=True)
    address_province = models.CharField(verbose_name=_(u'State'), max_length=255, blank=True)
    address_postal_code = models.CharField(verbose_name=_(u'Postal code'), max_length=255, blank=True)
    address_address_without_number = models.CharField(verbose_name=_(u'Route'), max_length=255, blank=True)
    address_address_number = models.CharField(verbose_name=_(u'Street number'), max_length=255, blank=True)

    status = models.CharField(verbose_name=_(u'Status'), max_length=255, blank=True)
    confirmation_code = models.CharField(verbose_name=_(u'Confirmation code'), max_length=255, blank=True)
    ip_address = models.IPAddressField(verbose_name=_(u'IP address'))
    insert_date = models.DateField(verbose_name=_(u'Insert date'), auto_now_add=True)

    def __unicode__(self):
        return self.name

    def clean(self):
        if self.from_date > self.to_date:
            raise ValidationError(_(u'Date error'))

    class Meta:
        verbose_name = _(u'Event')
        verbose_name_plural = _(u'Events')
