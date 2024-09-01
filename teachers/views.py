# teachers/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeacherProfileForm
from .models import TeacherProfile

def home(request):
    return render(request, 'home.html')

def teacher_list(request):
    teachers = TeacherProfile.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

@login_required
def create_teacher_profile(request):
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES)
        if form.is_valid():
            teacher_profile_data = form.cleaned_data
            user = request.user
            # Check if a profile already exists for the user
            if TeacherProfile.objects.filter(user=user).exists():
                # Optionally, handle the case where a profile already exists
                return redirect('teacher_list')  # Redirect or show an error message
            teacher_profile = form.save(commit=False)
            teacher_profile.user = user
            teacher_profile.save()
            return redirect('teacher_list')
    else:
        form = TeacherProfileForm()
    return render(request, 'teacher_profile_form.html', {'form': form})
