from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post) #add Post model to admin site to edit + make changes thru admin dashboard instead of writing a ton of code
