from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from agricom.settings import MEDIA_ROOT

class Incidence(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return self.name

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class gpxFile(models.Model):
    title = models.CharField("Title", max_length=100)
    gpx_file = models.FileField(upload_to='gpx_files')

    def __unicode__(self):
        return self.title

class GPXPoint(models.Model):
    name = models.CharField("Name", max_length=50, blank=True)
    description = models.CharField("Description", max_length=250, blank=True)
    gpx_file = models.ForeignKey(gpxFile, on_delete=models.CASCADE)
    point = models.PointField()
    objects = GeoManager()

    def __unicode__(self):
        return unicode(self.name)

class GPXTrack(models.Model):
    track = models.MultiLineStringField()
    gpx_file = models.ForeignKey(gpxFile, on_delete=models.CASCADE)
    objects = GeoManager()

