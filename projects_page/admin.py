from django.contrib import admin

# Register your models here.
from .models import PROJECT_TABLE, REVIEW_TABLE, TAG_TABLE

admin.site.register(PROJECT_TABLE)
admin.site.register(REVIEW_TABLE)
admin.site.register(TAG_TABLE)

