from users.models import Messages
from django.contrib import admin
from .models import Project, Tag, Review

# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Messages)
admin.site.register(Review)