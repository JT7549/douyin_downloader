from django.contrib import admin
from.models import DouyinVideo
admin.site.register(DouyinVideo)

# Register your models here.
class DouyinVideoAdmin(admin.ModelAdmin):
    list_display = ('video_url', 'is_downloaded')  # 设置列表页显示的字段
    list_editable = ('is_downloaded',)  # 设置可在列表页直接编辑的字段
    search_fields = ('video_url',)  # 设置搜索字段

admin.site.register(DouyinVideo, DouyinVideoAdmin)