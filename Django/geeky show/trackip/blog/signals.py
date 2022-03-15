from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def signedInSignal(sender, request, user, **kwargs):
    print('-'*50)
    ip = request.META.get('REMOTE_ADDR')
    print('IP: ', ip)
    request.session['ip'] = ip
