from django.contrib import admin
from .models import Category, Author, Book, Bookcomment

class bookCommentStackedInline(admin.StackedInline):
    model = Bookcomment

class BookTabulaInline(admin.TabularInline):
    model = Bookcomment
    extra = 2

class BookAdmin(admin.ModelAdmin):
    list_display = ['code','name','category', 'price', 'level', 'published','show_image']
    list_filter = ['published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug':['name']}

    fieldsets = (
        (None, {'fields': ['code','slug','name','description','level','image','price','published']}),
        ('Category', {'fields': ['category','author'], 'classes':['collapse']}),
    )
    # inlines = [bookCommentStackedInline]
    inlines = [BookTabulaInline]


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)

