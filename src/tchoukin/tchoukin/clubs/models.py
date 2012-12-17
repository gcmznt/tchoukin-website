import uuid
from django.db import models
from django.core.mail import send_mail
from django.utils.translation import ugettext as _


class Club(models.Model):
    name = models.CharField(verbose_name=_(u'Name'), max_length=150, unique=True)
    website = models.URLField(verbose_name=_(u'Website'), max_length=255, blank=True)
    email = models.EmailField(verbose_name=_(u'Email'), max_length=255)

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

    class Meta:
        verbose_name = _(u'Club')
        verbose_name_plural = _(u'Clubs')

    def save(self, *args, **kwargs):
        if self.id is None:
            self.status = 'pending'
            self.ip_address = '127.0.0.1'  # TODO ip
            self.confirmation_code = uuid.uuid1().hex

        # TODO email
        # print self.confirmation_code
        # send_mail('Confirm your place', 'To confirm your place go to this URL:', 'from@example.com', ['to@example.com'], fail_silently=False)

        super(Club, self).save(*args, **kwargs)
