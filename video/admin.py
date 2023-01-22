from django.contrib import admin
from .models import Video,VideoChapter,VideoLesson
# Register your models here.
class VideolessonInlineAdmin(admin.TabularInline):
    model= VideoLesson
    extra = 2

class VideoChapterInlineAdmin(admin.TabularInline):
    model= VideoChapter


class VideoAdmin(admin.ModelAdmin):
    list_display=['name','price','published','category','category_sub']
    list_filter = ['published']
    search_fields =['name']
    prepopulated_fields = {'slug':['name']}
    inlines=[VideolessonInlineAdmin,VideoChapterInlineAdmin]

admin.site.register(Video,VideoAdmin)
