from django.contrib import admin

from content.models import Author, Book, Category, Comment, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone",
    )
    list_editable = ("phone",)
    list_filter = ("first_name",)
    search_fields = (
        "first_name",
        "last_name",
    )


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "year",
    )
    list_filter = (
        "name",
        "city",
        "year",
    )
    search_fields = (
        "name",
        "city",
        "year",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("book", "from_user", "is_active")
    search_fields = ("book", "from_user", "created_at", "is_active")
    list_per_page = 30
    list_filter = (
        "book",
        "from_user",
        "created_at",
    )


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
    list_per_page = 30
