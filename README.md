# ⚡ Pixel Vault - E-commerce de Videojuegos

Plataforma de e-commerce y gestión de videojuegos con estética cyberpunk, desarrollada con una arquitectura robusta orientada al rendimiento y a un diseño visual limpio y moderno.

## 🚀 Enlaces
- **🌐 Ver página en vivo:** [https://pixel-vault-0rkn.onrender.com/)
- **📦 Repositorio:** [https://github.com/Torres-Fran-Dev/Pixel-Vault](https://github.com/Torres-Fran-Dev/Pixel-Vault)

---

## 🛠️ Tecnologías Utilizadas
- **Backend:** Python, Django (Arquitectura MTV, ORM, autenticación)
- **Base de Datos:** PostgreSQL
- **Frontend Web:** HTML5, CSS3, Tailwind CSS (con diseño cyberpunk personalizado y componentes modernos)
- **Contenedorización & DevOps:** Docker, Docker Compose
- **Hosting & Deploy:** Render (Producción) & Git / GitHub (Control de versiones)

---

## 📂 Estructura del Proyecto

```text
pixel-vault/
│
├── core/             # Configuración principal de Django (settings, urls, wsgi)
├── store/            # Modelos, vistas, urls y lógica de la tienda de videojuegos
├── static/           # Archivos estáticos (CSS, Tailwind, imágenes, JS)
├── templates/        # Plantillas HTML con estética cyberpunk
├── Dockerfile        # Configuración del contenedor de la aplicación
├── docker-compose.yml# Orquestador local (Django + PostgreSQL)
└── requirements.txt  # Dependencias del proyecto Python

