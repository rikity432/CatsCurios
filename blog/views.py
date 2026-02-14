from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .forms import CommentForm
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return (
            Post.objects.filter(status=1)
            .select_related("author")
            .prefetch_related("comments")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        context["comments"] = post.comments.filter(approved=True).select_related("user")
        context["comment_form"] = context.get("comment_form") or CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            login_url = reverse("login")
            return redirect(f"{login_url}?next={request.path}")

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment posted.")
            return HttpResponseRedirect(request.path)

        context = self.get_context_data(comment_form=comment_form)
        return self.render_to_response(context)