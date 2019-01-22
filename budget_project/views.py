"""To control views of project budget_project."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# @login_required
def home_view(request):
    """To control views for the project budget_project."""
    return render(request, 'generic/home.html', {'message': 'This is budget tool.'})

