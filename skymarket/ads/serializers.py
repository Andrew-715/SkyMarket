from rest_framework import serializers

from ads.models import Comment, Ad


class AuthorInformationMixin(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False)
    author_id = serializers.IntegerField(required=False)

    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    def get_author_first_name(self, obj):
        author_first_name = obj.author.first_name
        return author_first_name

    def get_author_last_name(self, obj):
        author_last_name = obj.author.last_name
        return author_last_name

    def get_phone(self, obj):
        try:
            phone = obj.author.phone.as_e164
            return phone
        except:
            return None


class CommentSerializer(AuthorInformationMixin):
    ad_id = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        exclude = ['id', 'author', 'ad']


class AdSerializer(AuthorInformationMixin):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(AuthorInformationMixin):
    class Meta:
        model = Ad
        fields = '__all__'

class AdCreateSerializer(AuthorInformationMixin):
    class Meta:
        model = Ad
        exclude = ['create_at', 'id', 'author']
