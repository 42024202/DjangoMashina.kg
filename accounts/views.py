from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import login, logout as django_logout, authenticate
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from accounts.models import CustomUser, EmailOTP
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from auto.models import CarAnnouncement
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['registration_data'] = form.cleaned_data

            code = f"{random.randint(100000, 999999)}"

            email = form.cleaned_data['email']
            EmailOTP.objects.create(user=username, code=code)

            send_mail(
                subject='Подтверждение регистрации',
                message=f'Ваш код подтверждения: {code}',
                from_email='esen.belov@mail.ru',
                recipient_list=[email],
                fail_silently=False,
            )

            messages.info(request, 'Код отправлен на email')
            return redirect('accounts:verify_otp', username)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field == '__all__':
                        messages.error(request, error)
                    else:
                        label = form.fields[field].label if field in form.fields else field
                        messages.error(request, f"{label}: {error}")
    form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def verify_otp_view(request, username):
    registration_data = request.session.get('registration_data')
    if not registration_data:
        messages.error(request, 'Сначала заполните форму регистрации')
        return redirect('accounts:register')

    if request.method == 'POST':
        code_input = request.POST.get('code')
        try:
            otp = EmailOTP.objects.get(user=username, code=code_input)
        except EmailOTP.DoesNotExist:
            messages.error(request, 'Неверный код')
            return redirect('accounts:verify_otp', username)

        if otp.is_expired():
            otp.delete()
            messages.warning(request, 'Код истёк. Запросите новый.')
            return redirect('accounts:verify_otp', username)
        email = registration_data.get('email')
        user = CustomUser(
            email=email,
            username=registration_data.get('username'),
            is_verified=True,
            password=make_password(registration_data.get('password1')),
        )
        user.save()

        del request.session['registration_data']
        EmailOTP.objects.filter(user=username).delete()

        login(request, user)
        messages.success(request, 'Аккаунт подтверждён и вы вошли в систему')
        return redirect('index:index')

    return render(request, 'accounts/verify_otp.html')


def resend_otp_view(request):
    registration_data = request.session.get('registration_data')
    if not registration_data:
        messages.error(request, 'Сначала заполните форму регистрации')
        return redirect('accounts:register')

    username = registration_data.get('username')
    email = registration_data.get('email')

    EmailOTP.objects.filter(user=username).delete()

    code = f"{random.randint(100000, 999999)}"
    EmailOTP.objects.create(user=username, code=code)

    send_mail(
        subject='Новый код подтверждения',
        message=f'Ваш новый код: {code}',
        from_email='esen.belov@mail.ru',
        recipient_list=[email],
        fail_silently=False,
    )

    messages.success(request, 'Новый код отправлен на email')
    return redirect('accounts:verify_otp', username)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('auto:index')
        messages.error(request, 'Неверный email или пароль')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    django_logout(request)
    return redirect('auto:index')

