import uuid
from django.db import models

class BaseModel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)

	def __str__(self):
        	object_name = self.__class__.__name__
        	if hasattr(self, 'name'):
            		object_name = self.name
        	object_name += ' ({})'.format(self.pk)
        	return object_name

	class Meta:
		abstract = True

class BaseExtensionModel(models.Model):
    # For models where we use primary keys other than UUID
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        object_name = self.__class__.__name__
        if hasattr(self, 'name'):
            object_name = self.name
        object_name += ' ({})'.format(self.pk)
        return object_name

    class Meta:
        abstract = True