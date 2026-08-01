def delete_instance_image(instance):
    file = instance.image
    print(f"Removing {file}")
    file.delete()
    return instance
