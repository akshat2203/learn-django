import datetime
from django.db.models import signals
from django.dispatch import receiver

from historical_data.models import Post, Author


@receiver(signals.post_save, sender=Post)
def create_post(sender, instance, created, **kwargs):
    print("Save method is called")


@receiver(signals.pre_save, sender=Post)
def check_post_content(sender, instance, **kwargs):
    if not instance.content:
        instance.content = 'This is Default content for post'


@receiver(signals.post_save, sender=Author)
def create_post(sender, instance, created, **kwargs):
    print("Save method is called")


@receiver(signals.pre_save, sender=Author)
def check_post_content(sender, instance, **kwargs):
    if not instance.date_of_birth:
        instance.date_of_birth = datetime.date.today()