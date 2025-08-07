from django.contrib import admin
from payments.models import Balance, Transaction


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


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'amount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'user__username')

