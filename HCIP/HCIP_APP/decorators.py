from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Redirect authenticated users to home page
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func