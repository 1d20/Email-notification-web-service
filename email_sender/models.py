from django.contrib.auth import get_user_model
from django.db import models


class EmailSender(models.Model):
    email_address = models.EmailField()
    email_password = models.CharField(max_length=254)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return self.email_address


class Statement(models.Model):
    name = models.CharField(max_length=254)
    email_sender = models.ForeignKey(EmailSender, on_delete=models.PROTECT)
    emails_receive = models.TextField()
    subject = models.TextField()
    message = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def get_emails_receive_list(self):
        emails = self.emails_receive.split()
        emails = [e.replace('\r', '') for e in emails]
        emails += [self.email_sender.email_address]
        return emails

    def __str__(self):
        return self.name
