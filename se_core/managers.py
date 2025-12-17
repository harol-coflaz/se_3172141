from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 

class UsuarioManager(BaseUserManager):
    
    """   
          Clase para la personalizacion de usuarios donde el correo es el unico
           identificador para la autenticacion de un usuario en el aplicativo 
    """
    def create_user(self, correo, password=None, **extra_fields):
        """
        Funcion para crear y guardar un usuario ingresando el correo y la contraseña
        
        :param self: Objeto propio de la clase 
        :param correo: Correo electronico
        :param password: Contraseña del usuario 
        :param extra_fields: Parametros adicionales 
        """    
        if not correo:
            raise ValueError(_('El correo electrónico es obligatorio'))
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        """
        Funcion para la creacion del superusuario
        
        :param self: Objeto propio de la clase 
        :param correo: Correo electronico del superusuario
        :param password: Contraseña del superusuario 
        :param extra_fields: Parametros adicionales 
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True: 
            raise ValueError(_('El superusuario debe tener el campo is_staff=True.'))
        
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError(_('El superusuario debe tener el campo is_staff=True.'))
        
        
        return self.create_user(correo, password, **extra_fields)