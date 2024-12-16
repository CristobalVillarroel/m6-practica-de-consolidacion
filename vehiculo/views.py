from django.shortcuts import render, redirect
from .forms import VehiculoForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from django.contrib.auth.models import User
from django.views import View
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    context = {}
    return render(request, "index.html", context)

@login_required
@permission_required('vehiculo.add_vehiculomodel')
def vehiculoform_view(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = VehiculoForm()

    context = { "form": form }
    return render(request, 'add_vehiculo.html', context)


class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect(reverse('register'))  
        user = User.objects.create_user(username=email, email=email, password=password1, first_name=first_name, last_name=last_name)

        content_type = ContentType.objects.get_for_model(VehiculoModel)
        visualizar = Permission.objects.get(
                codename='visualizar_catalogo',
                content_type = content_type
        )
        
        user.user_permissions.add(visualizar)
		
        user.save()
        user = authenticate(username=email, password=password1)
        if user is not None:
            login(request, user)
        messages.success(request, 'Usuario creado exitosamente')
        return redirect('index')
    
class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesion Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.WARNING, "Sesion Cerrada Exitosamente")
        return response
    
def vehiculolist_view(request):
    vehiculos = VehiculoModel.objects.all()

    for item in vehiculos:
        item.precio2 = f"${item.precio:.0f}"
        
    context = { 'vehiculos':vehiculos }
    return render(request, "list_vehiculo.html", context)