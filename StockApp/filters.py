#help us search for something from the page.
import django_filters 
from . models import SparePart, Category
#this class handles the queryset of products using partname.
class ProductFilter(django_filters.FilterSet):
    class Meta: 
        model = SparePart
        fields = [
            'part_name'
        ]

#this class handles the queryset for the categories.
class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = [
            'name'
        ]