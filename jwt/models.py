from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, usuario, password=None):
        user = self.model(
            usuario=usuario
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, usuario,  password):
        user = self.create_user(usuario, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class Usuario(AbstractBaseUser):
    usuario = models.CharField(max_length=15, unique=True)
    last_login = models.DateTimeField(blank=True, null=True, db_column='ultima_sesion')

    USERNAME_FIELD = 'usuario'
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'usuario'

