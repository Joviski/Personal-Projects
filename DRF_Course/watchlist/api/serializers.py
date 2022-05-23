from rest_framework import serializers
from ..models import *

class ReviewSerializer(serializers.ModelSerializer):
    review_user= serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        #fields = "__all__"
        exclude= ['watchlist']

class WatchListSerializer(serializers.ModelSerializer):
    length_title = serializers.SerializerMethodField()
    reviews= ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

    def get_length_title(self, object):
        return len(object.title)

    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError("Title & Storyline should differ")
        return data


    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title is too short!")
        return value

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)
    #watchlist = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    #watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name="movie-detail")

    class Meta:
        model = StreamPlatform
        fields= "__all__"

# def name_len(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name= serializers.CharField(validators=[name_len])
#     description= serializers.CharField()
#     active= serializers.BooleanField()
#
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name & Description should differ")
#         return data
#
#
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     return value