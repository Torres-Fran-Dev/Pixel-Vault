# ⚡ Pixel-Vault 

Plataforma de e-commerce y gestión de videojuegos con estética cyberpunk, desarrollada con una arquitectura robusta orientada al rendimiento y a un diseño visual limpio y moderno.

## 🚀 Tecnologías Utilizadas

* **Backend:** Python, Django 
* **Base de Datos:** PostgreSQL
* **Frontend Web:** HTML5, CSS3, Tailwind CSS (con diseño cyberpunk personalizado)
* **Contenedorización & Deploy:** Docker, Docker Compose
* **Control de Versiones:** Git / GitHub


---

## 📂 Estructura del Proyecto

```text
pixel-vault/
│
├── core/             # Configuración principal de Django
├── store/            # Modelos, vistas y lógica de la tienda de videojuegos
├── static/           # Archivos estáticos (CSS con Tailwind, imágenes, JS)
├── templates/        # Plantillas HTML con estética cyberpunk
├── Dockerfile        # Configuración del contenedor de la aplicación
├── docker-compose.yml# Orquestador (Django + PostgreSQL)

# 1. Clonar el repositorio
git clone [https://github.com/tu-usuario/pixel-vault.git](https://github.com/tu-usuario/pixel-vault.git)
cd pixel-vault

# 2. Levantar los contenedores con Docker Compose
docker-compose up --build

Una vez que los servicios estén andando, vas a poder acceder a la plataforma desde tu navegador en:
http://localhost:8300/
