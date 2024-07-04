from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError('The User ID must be set')
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_approved', 99)  # is_approved 필드를 99로 설정
        return self.create_user(user_id, password, **extra_fields)

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=200, unique=True)
    name = models.CharField("이름", max_length=50)
    password = models.CharField(verbose_name="비밀번호", max_length=255)
    is_approved = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def save(self, *args, **kwargs):
        if self.is_approved in [1, 2, 99]:  # is_approved가 1, 2 또는 99인 경우
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)

    def get_is_approved_display(self):
        if self.is_approved == 1:
            return "의사"
        elif self.is_approved == 2:
            return "간호사"
        elif self.is_approved == 99:
            return "관리자"  # 99일 때 관리자 권한을 표시
        return "승인 대기 중"
    class Meta:
        verbose_name = "병원 관계자"
