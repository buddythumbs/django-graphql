from django.contrib import admin

# Register your models here.
from .models import Task, Engineer, Category, Shift, Tool, ToolOwner, ActionPlan, ServiceNotification, Competency

admin.site.register(Task)
admin.site.register(Engineer)
admin.site.register(Category)
admin.site.register(Shift)
admin.site.register(Tool)
admin.site.register(ToolOwner)
admin.site.register(ActionPlan)
admin.site.register(ServiceNotification)
admin.site.register(Competency)