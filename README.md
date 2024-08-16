

# Agencia de Viajes - Proyecto Django

Este es un proyecto de una **Agencia de Viajes** desarrollado con Django. El objetivo del proyecto es proporcionar una plataforma donde los usuarios puedan registrarse, iniciar sesión y navegar por los destinos turísticos que la agencia ofrece.

## Características

- **Registro de Usuarios:** Permite a los usuarios crear una cuenta.
- **Inicio de Sesión:** Los usuarios pueden iniciar sesión con sus credenciales.
- **Perfil de Usuario:** Cada usuario registrado tiene su propio perfil.
- **Galería de Fotos:** Muestra imágenes relacionadas con los destinos ofrecidos.
- **Sistema de Navegación:** Incluye páginas como inicio, acerca de, destinos, contacto y noticias.
- **Formulario de Contacto:** Los usuarios pueden ponerse en contacto con los asesores de viajes.

## Estructura del Proyecto

proyecto/
│
├── app/
│ ├── templates/
│ │ ├── app/
│ │ │ ├── signup.html
│ │ │ ├── login.html
│ │ │ ├── profile.html
│ │ │ ├── index.html
│ │ │ ├── acerca_de.html
│ │ │ ├── destinos.html
│ │ │ ├── contacto.html
│ ├── static/
│ │ ├── app/
│ │ │ ├── css/
│ │ │ │ └── styles.css
│ │ │ ├── img/
│ │ │ │ └── (imágenes utilizadas en el proyecto)
│ ├── views.py
│ ├── forms.py
│ ├── models.py
│
├── manage.py
└── README.md


## Instalación y Configuración

### Prerrequisitos

- Python 3.10 o superior
- Django 5.1
- pip para instalar dependencias

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/usuario/proyecto-agencia-viajes.git

   cd proyecto-agencia-viajes

cd proyecto-agencia-viajes
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Este README cubre todos los aspectos importantes de tu proyecto, incluyendo la instalación, configuración, estructura del proyecto y cómo contribuir. Puedes modificarlo según sea necesario para adaptarlo a los detalles específicos de tu proyecto.
















