from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Renders the polls index page.

    Args:
        request: The HttpRequest object.

    Returns:
        HttpResponse: A response object containting the welcome message.
    """
    
    return HttpResponse("Hello, world. You're at the polls index.")