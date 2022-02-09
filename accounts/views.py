from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from accounts.forms import ProfileForm


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필을 수정/저장했습니다.')
            return redirect('profile_edit')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile_edit_form.html', {
        'form':form,
    })

