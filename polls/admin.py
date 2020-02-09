from django.contrib import admin
from .models import Choice
from .models import Pool
from .models import Vote
# Register your models here.


@admin.register(Choice)
class Custom_Choice(admin.ModelAdmin):
    list_display=('poll','choice_text')

admin.site.register(Pool)
admin.site.register(Vote)