import logging

logger = logging.getLogger(__name__)


def delete_instance_image(instance):
    file = instance.image
    if file:
        msg = f"{file.url} Deleted"
        logger.info(msg)
        file.delete()
    return instance
