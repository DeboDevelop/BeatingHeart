from django.shortcuts import redirect

def index(request):
    """
    Function to Redirect the homepage to admin dashboard
    Returns:
        Redirect to admin dashboard
    """
    return redirect('/admin')