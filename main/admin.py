from django.contrib import admin
from . models import Contact
from embed_video.admin import AdminVideoMixin
from .models import Video

admin.site.site_header = 'Welcome, to Admin Dashboard'


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, MyModelAdmin)
admin.site.register(Contact)
