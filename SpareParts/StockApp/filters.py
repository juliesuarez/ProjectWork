#help us search for something from the page.
import django_filters 
from . models import SparePart, Category
class ProductFilter(django_filters.FilterSet):
    class Meta: 
        model = SparePart
        fields = [
            'part_name'
        ]

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = [
            'name'
        ]