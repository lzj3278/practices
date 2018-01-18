from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post
from django.utils import timezone
from .forms import PostForm
import urlparse

# Create your views here.

# def post_list(request,id):
# 	return HttpResponse('you are look at %s' % id)


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# paginator = Paginator(posts,5)
	# try:
	# 	topics = paginator.page(page)
	# except PageNotAnInteger:
	# 	topics =paginator.page(1)
	# except EmptyPage:
	# 	topics = paginator.page(paginator.num_pages)
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
	posts = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'posts': posts})


def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			# return redirect(reverse('post_list'))
			url = urlparse.urljoin('/post/', str(post.pk))
			return redirect(url)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			# return redirect(reverse('post_list'))
			url = urlparse.urljoin('/post/', str(post.pk))
			return redirect(url)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

