from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'is_scheduled', 'scheduled_time', 'created_at', 'updated_at')
    list_filter = ('is_published', 'is_scheduled')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'video', 'file', 'is_paid_content')
        }),
        ('Publication', {
            'fields': ('is_published', 'is_scheduled', 'scheduled_time'),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj or not obj.is_scheduled:
            form.base_fields['scheduled_time'].disabled = True
        return form

    class Media:
        js = ('admin/js/post_admin.js',)

admin.site.register(Post, PostAdmin)
