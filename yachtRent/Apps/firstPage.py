from django.shortcuts import render


def show_first_page(request):
    """
    return first page
    :param request:
    :return: render
    """
    return render(request, 'firstPage.html')

