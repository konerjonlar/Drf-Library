from django.contrib import admin

from content.models import Author, Book, Category, Comment, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ("category",)
    search_fields = (
        "title",
        "author__full_name",
    )
    list_display = (
        "title",
        "score",
        "is_active",
    )
