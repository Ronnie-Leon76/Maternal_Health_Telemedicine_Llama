from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required!")
        if not password:
            raise ValueError("Password is a must!")

        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self , email , password):
        user = self.create_user(
            email = self.normalize_email(email) , 
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class UserAccount(AbstractBaseUser):
    class Types(models.TextChoices):
        MOTHER = "Mother" , "mother"
        SPECIALIST = "Specialist" , "specialist"
          
    type = models.CharField(max_length = 10, choices = Types.choices , 
                            # Default is user is mother
                            default = Types.MOTHER)

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    clinic = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30)
    residence = models.CharField(max_length=30)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

      
    # special permission which define that
    # the new user is mother or specialist
    is_mother = models.BooleanField(default = False)
    is_specialist = models.BooleanField(default = False)
      
    USERNAME_FIELD = "email"
      
    # defining the manager for the UserAccount model
    objects = UserAccountManager()
      
    def __str__(self):
        return str(self.email)
      
    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True
      
    def save(self , *args , **kwargs):
        if not self.type or self.type == None : 
            self.type = UserAccount.Types.TEACHER
        return super().save(*args , **kwargs)


class MotherManager(models.Manager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = UserAccount.Types.MOTHER)
        return queryset    

class Mother(UserAccount):
    class Meta : 
        proxy = True
    objects = MotherManager()
      
    def save(self , *args , **kwargs):
        self.type = UserAccount.Types.MOTHER
        self.is_mother = True
        return super().save(*args , **kwargs)

class SpecialistManager(models.Manager):
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    def get_queryset(self , *args , **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = UserAccount.Types.SPECIALIST)
        return queryset

class Specialist(UserAccount):
    class Meta :
        proxy = True
    objects = SpecialistManager()
      
    def save(self  , *args , **kwargs):
        self.type = UserAccount.Types.SPECIALIST
        self.is_specialist = True
        return super().save(*args , **kwargs)