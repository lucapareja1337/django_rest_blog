from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone 

class Usuario(AbstractUser):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    e_mail = models.EmailField(max_length=100, unique=True,error_messages={'unique':'O e-mail já foi cadastrado!'})
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'e_mail'
    
class Publicacao(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    texto = models.TextField()
    created_at     = models.DateTimeField(editable=False)
    modified_at    = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' Salvando as modificações e criações '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Publicacao, self).save(*args, **kwargs)