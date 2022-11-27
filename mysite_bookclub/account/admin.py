from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account


class AccountAdmin(UserAdmin):
	list_display = ('is_active', 'email', 'username', 'last_login', 'is_admin', 'is_teacher', 'is_student')
	search_fields = ('email', 'username',)
	readonly_fields = ('date_joined', 'last_login')

	# privalomi djang UserAdmin laukai
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)

