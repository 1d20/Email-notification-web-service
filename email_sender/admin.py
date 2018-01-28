from django.contrib import admin

from .models import EmailSender, Statement


class EmailSenderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('email_address', 'email_password',),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(user=request.user)


class StatementAdmin(admin.ModelAdmin):
    list_display = ('email_sender', 'emails_receive', 'text', 'comment')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(email_sender__user=request.user)


admin.site.register(EmailSender, EmailSenderAdmin)
admin.site.register(Statement, StatementAdmin)
