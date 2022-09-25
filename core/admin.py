from django.contrib import admin
from .models import Post, Project, Purpose, Professor, Timeline, AboutUs, Publications, ResearchArena, MembersTimeline, PictureCa, ProfTimeline, IndexResearch, PhotoVedio, tasks


class CustomPostAdmin(admin.ModelAdmin):
    list_display = list_display = [
        field.name for field in Post._meta.get_fields()]
    readonly_fields = ('short_des',)

    fieldsets = (
        ('url정보', {
            'fields': ('short_des',)
        }),
        (None, {
            'fields': ('title', 'category', 'content', 'descirption', )
        })
    )


admin.site.register(Post, CustomPostAdmin)
admin.site.register(Purpose)
admin.site.register(Professor)
admin.site.register(Timeline)
admin.site.register(AboutUs)
admin.site.register(Publications)
admin.site.register(ResearchArena)
admin.site.register(ProfTimeline)
admin.site.register(MembersTimeline)
admin.site.register(Project)
admin.site.register(PictureCa)
admin.site.register(PhotoVedio)
admin.site.register(IndexResearch)
admin.site.register(tasks)
