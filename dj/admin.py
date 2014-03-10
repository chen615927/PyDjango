from django.contrib import admin
from dj.models import Publisher

class PublisherAdmin(admin.ModelAdmin):
  list_display = ('name', 'address', 'city', 'telphone')
  list_filter = ('name', 'city')
  search_fields = ('name', 'gmt_create')
  # ordering = ('-publication_date',)**

admin.site.register(Publisher, PublisherAdmin)
