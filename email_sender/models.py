from django.contrib.auth import get_user_model
from django.db import models


class EmailSender(models.Model):
    email_address = models.EmailField()
    email_password = models.CharField(max_length=254)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return self.email_address


class Statement(models.Model):
    email_sender = models.ForeignKey(EmailSender, on_delete=models.PROTECT)
    emails_receive = models.TextField()
    text = models.TextField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.comment
