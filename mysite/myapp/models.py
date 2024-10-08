from django.db import models

class Link(models.Model):
    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        # Ensure a string is returned, even if name is None or empty
        return self.name if self.name else "Unnamed Link"
