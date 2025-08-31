# Repuestos\_site

Inventario y consulta de repuestos automotrices construido con **Django**, siguiendo el patrón **MVT** (Model–View–Template). Incluye herencia de plantillas, formularios para alta y búsqueda, y listados con filtrado.

> Proyecto educativo y práctico para gestionar estructuras de repuestos por **Clase**, **Marca**, **Modelo**, **Parte** y **Elemento**.

---

## 🧭 Tabla de contenidos

* [Características](#-características)

* [Tecnologías](#-tecnologías)

* [Estructura del modelo de datos](#-estructura-del-modelo-de-datos)

* [Vistas y URLs](#-vistas-y-urls)

* [Plantillas](#-plantillas)

* [Requisitos](#-requisitos)

* [Instalación y ejecución](#-instalación-y-ejecución)

* [Migraciones y superusuario](#-migraciones-y-superusuario)

* [Estructura del proyecto](#-estructura-del-proyecto)

* [Comandos rápidos](#-comandos-rápidos)

* [Licencia](#-licencia)

---

## ✨ Características

* ✅ **Herencia de plantillas** (base.html + bloques `title` y `content`).
* ✅ **Modelo de datos** con relaciones entre Clase, Marca, Modelo, Parte, Elemento y Estructura.
* ✅ **Formulario de alta** para crear nuevas estructuras de repuesto.
* ✅ **Búsqueda** simple por texto con método `GET`.
* ✅ **Listado** de estructuras (marca, modelo, parte, elemento, N° pieza, precio).
* ✅ Código organizado por app `inventario` con `models.py`, `forms.py`, `views.py`, `urls.py` y `templates/`.

> Nota: Si tu repositorio incluye funcionalidades extra (paginación, auth, importación CSV, API REST), agrégalas aquí.

---

## 🛠 Tecnologías

* **Python** 3.10+
* **Django** 4.x o 5.x
* **SQLite** (dev) / Postgres (prod opcional)
* **Bootstrap** 5 (CDN) para estilos básicos

---

## 🧱 Estructura del modelo de datos

Relaciones principales de la app `inventario` (nombres orientativos):

* `Clase`
* `Marca`
* `Modelo (cod_modelo, clase → Clase, marca → Marca, descripción, cod_veh)`
* `Parte`
* `Elemento`
* `Estructura (clase, marca, modelo, parte, elemento, nro_pieza?, precio?)`

```text
Clase ─┐
       ├── Modelo ◀── Marca
       │
       └── Estructura ── Parte ── Elemento
```

> `Estructura.__str__`: `"{modelo} | {parte} | {elemento} | pieza={nro_pieza or '-'}"`

---

## 🔗 Vistas y URLs

* **Listado**: `estructura_list` — muestra tabla de estructuras con formulario `GET` para búsqueda (`q`).
* **Alta**: `estructura_create` — formulario para crear una nueva `Estructura`.

Rutas (ejemplo `inventario/urls.py`):

```py
from django.urls import path
from . import views

urlpatterns = [
    path('estructuras/', views.estructura_list, name='estructura_list'),
    path('estructuras/nueva/', views.estructura_create, name='estructura_create'),
]
```

Incluidas desde `repuestos_site/urls.py`:

```py
from django.urls import path, include

urlpatterns = [
    path('', include('inventario.urls')),
]
```

---

## 🧩 Plantillas

* `templates/inventario/base.html` — define bloques `title` y `content` y carga el **navbar** (`{% include 'inventario/navbar.html' %}`).
* `templates/inventario/estructura_list.html` — extiende `base.html`, muestra **formulario de búsqueda** y **tabla** con: Marca, Modelo, Parte, Elemento, N° pieza, Precio.
* `templates/inventario/estructura_form.html` — formulario de alta (ModelForm o Form clásico).

Fragmento (búsqueda + listado):

```django
<form method="get">
  {{ form.q.label_tag }} {{ form.q }}
  <button type="submit">Buscar</button>
</form>

<p><a href="{% url 'estructura_create' %}">+ Nueva estructura</a></p>

<table>
  <thead>
    <tr>
      <th>Marca</th><th>Modelo</th><th>Parte</th><th>Elemento</th><th>N° pieza</th><th>Precio</th>
    </tr>
  </thead>
  <tbody>
    {% for e in objetos %}
      <tr>
        <td>{{ e.modelo.marca.nombre }}</td>
        <td>{{ e.modelo.descripcion }}</td>
        <td>{{ e.parte.nombre }}</td>
        <td>{{ e.elemento.nombre }}</td>
        <td>{{ e.nro_pieza|default:"-" }}</td>
        <td>{{ e.precio|default:"-" }}</td>
      </tr>
    {% empty %}
      <tr><td colspan="6">Sin resultados</td></tr>
    {% endfor %}
  </tbody>
</table>
```

---

## 📦 Requisitos

* Python 3.10+
* pip
* (Opcional) virtualenv
* Git

---

## 🚀 Instalación y ejecución

Clona el repo y levanta el entorno (Windows / PowerShell):

```ps1
# 1) Clonar
git clone https://github.com/<usuario>/Repuestos_site.git
cd Repuestos_site

# 2) Entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # en CMD: .\.venv\Scripts\activate.bat

# 3) Dependencias
pip install -r requirements.txt  # si existe
# o bien (mínimo)
pip install django

# 4) Migraciones\python manage.py migrate

# 5) Superusuario (opcional)
python manage.py createsuperuser

# 6) Ejecutar\python manage.py runserver
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt || pip install django
python manage.py migrate
python manage.py createsuperuser  # opcional
python manage.py runserver
```

Abre: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🗃 Migraciones y superusuario

```bash
python manage.py makemigrations inventario
python manage.py migrate
python manage.py createsuperuser
```

Admin: `/admin/`

---

## 🗂 Estructura del proyecto

```text
Repuestos_site/
├─ repuestos_site/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ inventario/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations/
│  ├─ models.py
│  ├─ urls.py
│  ├─ views.py
│  └─ templates/
│     └─ inventario/
│        ├─ base.html
│        ├─ navbar.html
│        ├─ estructura_list.html
│        └─ estructura_form.html
├─ manage.py
├─ requirements.txt (opcional)
└─ README.md
```

---

## ⚡ Comandos rápidos

```bash
# Ejecutar servidor
python manage.py runserver

# Crear nueva app
python manage.py startapp <nombre_app>

# Shell de Django
python manage.py shell

# Exportar requirements (si usas venv)
pip freeze > requirements.txt
```

## 🧑‍💻 Autor

**Seba** — *Inspecciones y cotizaciones de siniestros*

>
