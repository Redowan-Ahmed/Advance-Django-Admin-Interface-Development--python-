from django.contrib import admin
from .models import *
from django.utils.html import format_html
 


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    fields= ('title','descripstion',  'preview', 'image','schedule', 'status','author' )
    readonly_fields= ('preview',)
    list_display = ( 'Thumbnail', 'title', 'status', 'is_completed', 'editbutton')
    list_display_links = ('title', 'status',)
    list_filter = ('created_at','status', 'is_completed',)
    save_on_top = False
    search_fields = ('title',)
    actions_on_bottom = True;
    list_per_page= 2
    def Thumbnail(self, obj):
        return format_html(f'<a href="/admin/admininterface/todo/{obj.id}/change/"> <img width="90px" src="/media/{obj.image}" > </a>') 
    def preview(self, obj):
        return format_html(f'<img width="90px" src="/media/{obj.image}" >') 
    def editbutton(self, obj):
        return format_html(f'<a style="padding: 10px 20px;background: #68d4fa;color: #121212;font-weight: 600;border-radius: 50px;text-align: center;display: inline-block;" href="/admin/admininterface/todo/{obj.id}/change/"> Edit </a>') 
    


admin.site.register(Todo, TodoAdmin)
