from django.contrib import admin
from django.core.mail import send_mail

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
    list_display = ('name', 'email_sender', 'emails_receive', 'subject', 'message', 'comment')
    actions = ['send_email']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(email_sender__user=request.user)

    def send_email(self, request, queryset):
        for obj in queryset:
            send_mail(
                obj.subject,
                obj.message,
                obj.email_sender.email_address,
                obj.get_emails_receive_list(),
                fail_silently=False,
                auth_user=obj.email_sender.email_address,
                auth_password=obj.email_sender.email_password
            )

    send_email.short_description = "Send (REAL) emails"


admin.site.register(EmailSender, EmailSenderAdmin)
admin.site.register(Statement, StatementAdmin)
