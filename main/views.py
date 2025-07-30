from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import CarAnnouncement
from django.contrib.auth import authenticate, login, logout as django_logout
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from accounts.models import CustomUser, EmailOTP
from accounts.forms import LoginForm, OTPForm, RegisterForm



def index(request):
    """Главная страница."""
    cars = CarAnnouncement.objects.all()
    return render(
            request, 
            'main/index.html', 
            {'cars': cars}
            )

def car_detail(request, car_id):
    car = get_object_or_404(CarAnnouncement, id=car_id)
    return render(
            request, 
            'main/car_detail.html', 
            {'car': car}
            )

def category_view(request, category_name):
    cars = CarAnnouncement.objects.filter(category__name=category_name)
    return render(
            request, 
            'main/category.html', 
            {
                'cars': cars, 
                'category_name': category_name
                }
            )

