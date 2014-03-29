from django.contrib import admin
from stories.models import Story, Name, KnownFor


admin.site.register(Story)


class KnownForInline(admin.TabularInline):
    model = KnownFor
    extra = 0


class NameAdmin(admin.ModelAdmin):
    inlines = [KnownForInline]


admin.site.register(Name, NameAdmin)
