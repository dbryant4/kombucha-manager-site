from django.db import models
from datetime import datetime

class Source(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

class TeaType(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

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
        return "%s %s %s" % (", ".join(sources),
                            self.name,
                            ", ".join(tea_types))

class Batch(models.Model):
    tea = models.ManyToManyField(Tea, related_name='batches')
    tea_volume = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    sugar_volume = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    brew_volume = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    scoby_count = models.IntegerField(default=1)
    brew_date = models.DateField('date of first fermentation', default=datetime.now().today)
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "Batch #%s - %s" % (self.id, self.brew_date)

class Flavor(models.Model):
    name = models.CharField(max_length=200)
    source = models.ManyToManyField(Source, related_name='flavors')
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Bottle(models.Model):
    batch = models.ForeignKey(Batch, related_name='bottles')
    flavors = models.ManyToManyField(Flavor, related_name='bottles')
    bottle_date = models.DateField('date bottled', default=datetime.now().today)
    comments = models.TextField(null=True, blank=True)

    def __unicode__(self):
        flavors = (flavor.name for flavor in self.flavors.all())
        return "Bottle #%s (%s) - %s" % (self.id, ", ".join(flavors), self.bottle_date)
