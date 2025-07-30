from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    CustomUser, Balance, Transaction,
    Favorite, Message, EmailOTP
)

# -----------------------
# Inline классы
# -----------------------

class BalanceInline(admin.StackedInline):
    model = Balance
    can_delete = False
    extra = 0
    readonly_fields = ('account_number',)
    verbose_name_plural = 'Баланс'

class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0
    readonly_fields = ('name', 'amount', 'description', 'created_at')
    verbose_name_plural = 'Транзакции'

# -----------------------
# Admin кастомного юзера
# -----------------------

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'username', 'phone', 'is_verified', 'is_staff', 'is_active')
    list_filter = ('is_verified', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'phone')
    ordering = ('id',)
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Личная информация', {'fields': ('phone', 'avatar', 'is_verified')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    inlines = [BalanceInline, TransactionInline]

# -----------------------
# Остальные модели
# -----------------------


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'amount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'user__username')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp', 'is_read')
    search_fields = ('sender__email', 'recipient__email')
    list_filter = ('is_read', 'timestamp')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_object', 'added_at')
    list_filter = ('added_at',)

@admin.register(EmailOTP)
class EmailOTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'created_at', 'is_used')
