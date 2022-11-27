from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . models import TaskPost
from . forms import TaskPostForm


@login_required
def upload_taskpost(request):
	if request.method == 'POST':
		form = TaskPostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('taskpost_list')
	else:
		form = TaskPostForm()
	context = {
        'form': form
    }
	return render(request, 'taskposts/upload_taskpost.html', context)


def taskpost_list(request):
	taskpost = TaskPost.objects.all()
	context = {
        'taskpost_list': taskpost
    }
	return render(request, 'taskposts/taskpost_list.html', context=context)


def delete_taskpost(request, id):
	if request.method == 'POST':
		task =TaskPost.objects.get(id=id)
		task.delete()
	return redirect('taskpost_list')


