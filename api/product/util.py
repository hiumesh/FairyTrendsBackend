from rest_framework import viewsets, serializers
from api.product import models

class MultiSerializerViewSet(viewsets.ModelViewSet):
  serializers = { 
    'default': None,
  }

  def get_serializer_class(self):
    return self.serializers.get(self.action, self.serializers['default'])

def update_category_collection_category(category, instance, category_serializer, category_collection_categories_create_serializer):
    tmp_category = {
      "CollectionId": getattr(instance, 'CollectionId'),
      "CategoryId": getattr(category['CategoryId'], 'CategoryId'),
    }
    if 'Alias' in category and category['Alias']: tmp_category['Alias'] = category['Alias']
    else: tmp_category['Alias'] = getattr(category['CategoryId'], 'CategoryName')
    if 'Tags' in category and category['Tags']:
      tags = []
      category_instance = models.Category.objects.get(CategoryId=getattr(category['CategoryId'], 'CategoryId'))
      category_serializer = category_serializer(category_instance)
      valid_tags = category_serializer.data['Tags']
      for tag in category['Tags']:
        if getattr(tag, 'TagId') not in valid_tags: raise serializers.ValidationError("Tag does not belong to the category!")
        tags.append(getattr(tag, 'TagId'))
      tmp_category['Tags'] = tags
    new_category_serializer = category_collection_categories_create_serializer(data=tmp_category)
    if (new_category_serializer.is_valid(raise_exception=True)):
      new_category_serializer.save()