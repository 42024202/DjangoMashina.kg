from django.shortcuts import render


def get_announcement_create(request):
    """Show which form to use for creating an announcement."""
    context = {}
    return render(request, 'auto/choise_template_for_create.html', context)

