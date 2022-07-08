from dataclasses import fields
from rest_framework import serializers
from blog.models import Usuario,Publicacao  

class UsuarioSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        style={'input_type':'password'},
        write_only = True,
        label='Senha'
    )
    confirma_password = serializers.CharField(
        style={'input_type':'password'},
        write_only = True,
        label="Confirme sua senha"
    )
    is_staff = serializers.BooleanField(
        label = "Funcionario",
        help_text = "Indica se o usuário é ou não membro da empresa"
    )
    is_superuser = serializers.BooleanField(
        label="Usuario ADM",
        help_text = "Indica se o usuário é super usuário"
    )
    class Meta:
        model = Usuario 
        fields = ('username','e_mail','password','confirma_password','is_staff','is_superuser')
        extra_kwargs = {'password':{'write_only':True}}
        
    def save(self):
        conta = Usuario(
            e_mail = self.validated_data['e_mail'],
            username=self.validated_data['username'],
            is_staff = self.validated_data['is_staff'],
            is_superuser = self.validated_data['is_superuser']
        )
        password = self.validated_data['password']
        confirma_password = self.validated_data['confirma_password']
        
        if password != confirma_password:
            raise serializers.ValidationError({'password':'As senhas não batem!'})
        conta.set_password(password)
        conta.save()
        return conta

class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = '__all__' 