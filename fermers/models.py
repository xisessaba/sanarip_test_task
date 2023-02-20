# from django.db import models
from django.contrib.gis.db import models

class Fermer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Fermers"
        verbose_name = "Fermer"


class Culture(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cultures"
        verbose_name = "Culture"

class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Seasons"
        verbose_name = "Season"

class Plot(models.Model):
    contour = models.PointField(srid=4326, blank=True)
    fermer = models.ForeignKey(Fermer, on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.fermer.name

    class Meta:
        verbose_name_plural = "Plots"
        verbose_name = "Plot"





	
