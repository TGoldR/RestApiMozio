from datetime import datetime
from rest_framework_json_api import serializers, relations
from example.models import Polygon, Provider, AuthorBio

class EntrySerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # to make testing more concise we'll only output the
        # `featured` field when it's requested via `include`
        request = kwargs.get('context', {}).get('request')
        if request and 'featured' not in request.query_params.get('include', []):
            self.fields.pop('featured')
        super(EntrySerializer, self).__init__(*args, **kwargs)

    included_serializers = {
        'authors': 'example.serializers.AuthorSerializer',
        'featured': 'example.serializers.EntrySerializer',
    }

    #body_format = serializers.SerializerMethodField()
    # many related from model
    #comments = relations.ResourceRelatedField(
    #        source='comment_set', many=True, read_only=True)
    # many related from serializer
    suggested = relations.SerializerMethodResourceRelatedField(
            source='get_suggested', model=Polygon, many=True, read_only=True)
    # single related from serializer
    featured = relations.SerializerMethodResourceRelatedField(
            source='get_featured', model=Polygon, read_only=True)

    def get_suggested(self, obj):
        return Polygon.objects.exclude(pk=obj.pk)

    def get_featured(self, obj):
        return Polygon.objects.exclude(pk=obj.pk).first()

    #def get_body_format(self, obj):
    #    return 'text'

    class Meta:
        model = Polygon
        fields = ('name', 'price', 'latitude', 'longitude', 'pub_date', 'mod_date',
                  'authors', 'featured', 'suggested',)
        #meta_fields = ('body_format',)


class AuthorBioSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorBio
        fields = ('author', 'body',)


class AuthorSerializer(serializers.ModelSerializer):
    #included_serializers = {
    #    'bio': AuthorBioSerializer
    #}

    class Meta:
        model = Provider
        fields = ('name', 'email', 'phonenum', 'language', 'currency')
