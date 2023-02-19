from django.contrib import admin

# Register your models here.
from .models import ProjectPost,ProjectPostSection
# Register your models here.
admin.site.register(ProjectPost)

admin.site.register(ProjectPostSection)

