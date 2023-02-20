from rest_framework import serializers
from .models import Fermer, Culture, Season, Plot

class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class PlotSerializer(serializers.ModelSerializer):
    culture = CultureSerializer(read_only=True)
    season = SeasonSerializer(read_only=True)

    class Meta:
        model = Plot
        fields = '__all__'

class FermerSerializer(serializers.ModelSerializer):
    plots = PlotSerializer(many=True, read_only=True)

    class Meta:
        model = Fermer
        fields = '__all__'