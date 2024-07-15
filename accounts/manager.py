from django.contrib.auth.base_user import BaseUserManager

class UserManager (BaseUserManager):
    use_in_migrations = True
    def create_user(self, phone_no, password= None, **extra_fields): 
        if not phone_no:
            raise ValueError('Phone number is required')
        user= self.model(phone_no= phone_no, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser (self, phone_no, password, **extra_fields): 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(phone_no, password, **extra_fields)