from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ("user", "body", "approved", "created_on")
    readonly_fields = ("created_on",)
    show_change_link = True


@admin.action(description="Approve selected posts (publish)")
def approve_posts(modeladmin, request, queryset):
    updated = queryset.update(status=1)
    modeladmin.message_user(request, f"Approved {updated} post(s).")


@admin.action(description="Unapprove selected posts (set to draft)")
def unapprove_posts(modeladmin, request, queryset):
    updated = queryset.update(status=0)
    modeladmin.message_user(request, f"Unapproved {updated} post(s).")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ('status', 'created_on', 'mood')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_on',)
    inlines = [CommentInline]
    actions = [approve_posts, unapprove_posts]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj=obj))
        if not request.user.is_superuser:
            readonly_fields.append("status")
        return readonly_fields

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            actions.pop("approve_posts", None)
            actions.pop("unapprove_posts", None)
        return actions

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.status = 0
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user__username', 'body')


