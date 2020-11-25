from django.contrib import admin
from .models import shape_piza, size_piza, piza_type, choice

admin.site.register(shape_piza)
admin.site.register(choice)
admin.site.register(size_piza)
admin.site.register(piza_type)