import json
from .tools import model_instance_diff
from .models import DataLogEntry


def log_create(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a log entry when a model instance is first saved to the database.
    Direct use is discouraged, connect your model through :py:func:`compliance.registry.register` instead.
    """
    if created:
        changes = model_instance_diff(None, instance)

        log_entry = DataLogEntry.objects.log_create(
            instance,
            action='created',
            changes=json.dumps(changes),
        )


def log_update(sender, instance, **kwargs):
    """
    Signal receiver that creates a log entry when a model instance is changed and saved to the database.
    Direct use is discouraged, connect your model through :py:func:`compliance.registry.register` instead.
    """
    if instance.pk is not None:
        try:
            old = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            pass
        else:
            new = instance

            changes = model_instance_diff(old, new)

            # Log an entry only if there are changes
            if changes:
                log_entry = DataLogEntry.objects.log_create(
                    instance,
                    action='updated',
                    changes=json.dumps(changes),
                )


def log_delete(sender, instance, **kwargs):
    """
    Signal receiver that creates a log entry when a model instance is deleted from the database.
    Direct use is discouraged, connect your model through :py:func:`compliance.registry.register` instead.
    """
    if instance.pk is not None:
        changes = model_instance_diff(instance, None)

        log_entry = DataLogEntry.objects.log_create(
            instance,
            action='deleted',
            changes=json.dumps(changes),
        )