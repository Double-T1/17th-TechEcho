import datetime
import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from answers.models import Answer
from chat.models import ChatGroup
from questions.models import Question


def verify(value):
    # 正則表達式：允許中文字符、英文字符和空格
    if not re.match(r"^[\u4e00-\u9fffA-Za-z\s]*$", value):
        raise ValidationError("專業能力只能包含中英文字符")


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=255, validators=[verify])
    introduce = models.TextField(
        validators=[MinLengthValidator(50), MaxLengthValidator(500)]
    )
    nickname = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    schedule = models.TimeField(default=datetime.time(0, 0))
    chat_group = models.OneToOneField(
        "chat.ChatGroup",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_teacher",
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.user.is_teacher = True
            self.user.save()
        # 如果没有 chat_group，创建一个新的 ChatGroup
        if not self.chat_group:
            chat_group = ChatGroup.objects.create(
                group_name=f"{self.nickname or self.user.username}",
            )
            self.chat_group = chat_group
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.expertise}"

    def get_questions(self):
        return Question.objects.filter(user=self.user)

    def get_answers(self):
        return Answer.objects.filter(user=self.user)
