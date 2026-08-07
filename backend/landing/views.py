from django.shortcuts import render


def landing_page(request):
    """
    Public marketing/landing page that explains what Mr Exchange can do.
    """
    return render(request, "landing/index.html")


