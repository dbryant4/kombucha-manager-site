from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name="user_profile")
    organization = models.ForeignKey(Organization, related_name="user_profiles")

    def __unicode__(self):
        return self.user.username

class Vessel(models.Model):
    organization = models.ForeignKey(Organization, related_name="vessels")
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "{0!s} - {1!s}".format(self.organization, self.name)

class Source(models.Model):
    name = models.CharField(max_length=200)
    source_url = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

class TeaType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Tea(models.Model):
    name = models.CharField(max_length=200)
    comments = models.TextField(null=True, blank=True)
    sources = models.ManyToManyField(Source, related_name='teas')
    tea_types = models.ManyToManyField(TeaType, related_name='teas')

    def __unicode__(self):
        sources = (source.name for source in self.sources.all())
        tea_types = (tea_type.name for tea_type in self.tea_types.all())
        return "{0!s} {1!s} {2!s}".format(", ".join(sources),
                            self.name,
                            ", ".join(tea_types))

class Batch(models.Model):
    vessel = models.ForeignKey(Vessel, related_name='batches')
    tea = models.ManyToManyField(Tea, related_name='batches')
    tea_volume = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    sugar_volume = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    brew_volume = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    scoby_count = models.IntegerField(default=1)
    brew_date = models.DateField('date of first fermentation', default=datetime.now().today)
    comments = models.TextField(null=True, blank=True)
    discarded = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "batches"

    def __unicode__(self):
        return "Batch #{0!s} ({1!s}) - {2!s}".format(self.id, None, self.brew_date)

class Flavor(models.Model):
    name = models.CharField(max_length=200)
    source = models.ManyToManyField(Source, related_name='flavors')
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class BottleSize(models.Model):
    size = models.IntegerField(default=1)

    def __unicode__(self):
        return "{0!s} fl oz".format(self.size)

class Bottle(models.Model):
    batch = models.ForeignKey(Batch, related_name='bottles')
    size = models.ForeignKey(BottleSize, related_name='bottles')
    flavors = models.ManyToManyField(Flavor, related_name='bottles')
    bottle_date = models.DateField('date bottled', default=datetime.now().today)
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        # flavors = (flavor.name for flavor in self.flavors.all())
        flavors = ['no']
        return "Bottle #{0!s} {1!s} fl oz ({2!s}) - {3!s}".format(self.id, self.size.size, ", ".join(flavors), self.bottle_date)
