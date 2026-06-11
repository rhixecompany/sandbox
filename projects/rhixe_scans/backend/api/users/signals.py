from django.db.models.signals import pre_delete

from api.users.models import User
from api.users.signals_helpers import delete_instance_image


def user_image_pre_delete(sender, instance, *args, **kwargs):
    if instance.image:
        delete_instance_image(instance)


pre_delete.connect(
    user_image_pre_delete,
    sender=User,
    dispatch_uid="user_image_pre_delete",
)
