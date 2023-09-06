from django.shortcuts import render


def catalog_list(request):
    """Функция, возвращающая домашнюю страницу"""
    return render(request, 'catalog/home.html', {})


def contact_list(request):
    """Функция, возвращающая страницу контактов"""
    if request.method == 'POST':
        print(f"name: {request.POST.get('name')}")
        print(f"phone: {request.POST.get('phone')}")
        print(f"message: {request.POST.get('message')}")
    return render(request, 'catalog/contacts.html', {})
