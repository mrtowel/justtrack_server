from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from social_auth.db.django_models import UserSocialAuth
from tastypie.models import ApiKey

URL_TYPES = (
    (1, 'nav'),
    (2, 'other'),
)


class Url(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    subvalue = models.ForeignKey('self', null=True)
    url_type = models.IntegerField(choices=URL_TYPES)


class Location(models.Model):
    lon = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ('-time', )

    def __unicode__(self):
        return '%s [%s, %s] %s' % (self.user, self.lon, self.lat, self.time)


class JustTrackUser(models.Model):
    def get_user_upload_path(self):
        return '%s_%s' % (self.user.id, self.user.username)

    user = models.OneToOneField(User)
    color = models.CharField(max_length=6, default='eeeeee')
    avatar = models.FileField(upload_to='%s/%s' % ('user_photos', get_user_upload_path), blank=True, null=True)

    def __unicode__(self):
        return self.user.username


def connect_user(sender, instance, created, **kwargs):
    pass


def create_just_track_user(sender, instance, created, **kwargs):
    if created:
        profile, just_track_created = JustTrackUser.objects.get_or_create(user=instance)
        apikey, apikey_created = ApiKey.objects.get_or_create(user=instance)

        if just_track_created:
            profile.save()
        if apikey_created:
            apikey.save()


post_save.connect(create_just_track_user, User)
post_save.connect(connect_user, UserSocialAuth)