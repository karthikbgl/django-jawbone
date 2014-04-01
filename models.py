from django.db import models
from django.conf import settings

auth_user = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class UserJawbone(models.Model):

    user = models.ForeignKey(auth_user)
    token_type = models.CharField(max_length=512)
    access_token = models.CharField(max_length=512)
    refresh_token = models.CharFieldField(max_length=512)
    expires_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"{0}".format(self.user)
