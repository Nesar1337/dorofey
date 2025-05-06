from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.models import Reviews, Order

User = get_user_model()

def main(request):
    reviews = Reviews.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'index.html', context)


def auth_view(request):
    return render(request, 'auth.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            return HttpResponse("Заполните корректно все поля!")
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("Данный username уже зарегистрирован в БД!")
        
        if User.objects.filter(email=email).exists():
            return HttpResponse("Данный email уже зарегистрирован в БД!")
    
        user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
        login(request, user)

        return redirect('main')
    return HttpResponse("Ожидается POST-запрос!")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return HttpResponse("Заполните корректно все поля!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse("Неправильный username или password!")
    return HttpResponse("Ожидается POST-запрос!")


def logout_view(request):
    logout(request)
    return redirect('main')


def create_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        address = request.POST.get('address')
        date = request.POST.get('date')
        time = request.POST.get('time')

        Order.objects.create(
            name=name,
            phone=phone,
            service=service,
            address=address,
            date=date,
            time=time
        )

        print(f"""
            Данные заказа:
            {name},
            {phone},
            {service},
            {address},
            {date},
            {time},
            """)

        return redirect('main')
    return HttpResponse("Ожидается POST-запрос!")

@login_required
def create_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        text = request.POST.get('text')
        image = request.FILES.get('image')

        if image:
            Reviews.objects.create(
                name=name,
                role=role,
                text=text,
                image=image,
            )

        return redirect('/#testLink')
    return HttpResponse("Ожидается POST-запрос!")
