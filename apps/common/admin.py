from django.contrib import admin
from django.utils.safestring import mark_safe  # this is to render html text


admin.site.site_header = mark_safe(
    "<strong style='font-weight:bold;'>C.S ADMIN</strong>"
)
