from django.contrib import admin
from .models import Article,Person,TeacherInfo
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = ('tec_title',)



admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(TeacherInfo,TeacherInfoAdmin)