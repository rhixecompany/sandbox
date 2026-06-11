def delete_instance_image(instance):
    file = instance.image
    print(f"Removing {file}")  # noqa: T201
    file.delete()
    return instance
