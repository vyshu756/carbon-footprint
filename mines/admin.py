from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin
from .models import ActivityData, EmissionFactor

#  Add this ONLY (admin site name change)
admin.site.site_header = "Coal Mine Admin Portal"
admin.site.site_title = "Coal Mine Admin Portal"
admin.site.index_title = "Coal Mine Administration"

# Existing registrations (unchanged)
admin.site.register(ActivityData)
admin.site.register(EmissionFactor)





