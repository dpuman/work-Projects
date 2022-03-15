from ensurepip import version
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache


@receiver(user_logged_in, sender=User)
def signedInSignal(sender, request, user, **kwargs):
    ct = cache.get('count', 0, version=user.pk)
    new_count = ct+1
    cache.set('count', new_count, version=user.pk)
