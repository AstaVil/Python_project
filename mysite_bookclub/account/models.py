from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# userio ir superuserio paskyros kurimas
class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Paskyrai būtinas el.paštas!')
		if not username:
			raise ValueError('Paskyrai būtinas vartotojo vardas!')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

def get_profile_img_path(self, filename):
	return f'accounts/profile_img/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
	return 'account/static/profile_img/default.jpg'

class Account(AbstractBaseUser, PermissionsMixin):
	# būtini laukai kuriant userio modelį
	email = models.EmailField('El. paštas', max_length=60, unique=True)
	username = models.CharField('Vartotojo vardas', max_length=30, unique=True, )
	date_joined = models.DateTimeField(verbose_name='Prisijungimo data', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='Paskutiną kartą matytas', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	# papildomi laukai - skirtingo tipo useriams
	is_teacher = models.BooleanField(default=False)
	is_student = models.BooleanField(default=True)
	# pagal defoltinę reikšmę userio emailas nesimato išorės vartotojams
	hide_email = models.BooleanField(default=True)

	profile_image = models.ImageField(max_length=255, upload_to=get_profile_img_path,
                                    null=True, blank=True, default=get_default_profile_image)
	# useris loginasi su emailu
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return f'{self.email}'

	# privalomos funkcijos nustatancios useriams leidimus
	#  jei ne admin neturi leidimus
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# useriui duodamas leidimas irasineti i app_label
	def has_module_perms(self, app_label):
		return True

# funkcija tvarkanti profilio nuotraukos failo pavadinima
	def get_profile_image_filename(self):
		return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
