from django.contrib import admin
from . import models
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ["id","name","mobile","prnno","member_type"]

class BookAdmin(admin.ModelAdmin):
    list_display = ["id","title","author","category","qty"]

class LoanAdmin(admin.ModelAdmin):
    list_display = ["id","member","book","date_borrow","date_due","days_on_books"]

class ReturnBookAdmin(admin.ModelAdmin):
    list_display = ["id","loan","return_date","charges","dateoverdue"]

admin.site.register(models.Member,MemberAdmin)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Loan,LoanAdmin)
admin.site.register(models.ReturnBook,ReturnBookAdmin)

