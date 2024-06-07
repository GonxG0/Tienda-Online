from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import send_mail


def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            
            try:
                infForm= formulario_contacto.cleaned_data

                send_mail("Contacto desde Portfolio", f"Hola, mi nombre es {nombre}, me puedes contactar con {email} \n\n {contenido}",
                        infForm.get("email",""),["gonzalo.digangi@gmail.com"],)
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
            

    return render(request, "contacto/contacto.html", {"miFormulario":formulario_contacto})