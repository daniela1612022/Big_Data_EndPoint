# Flask S3 Bucket Lister

Este proyecto es una aplicación web simple construida con Flask que lista los buckets de S3 de tu cuenta de AWS. La lista de buckets se puede ver en formato HTML o en JSON.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes elementos:

- Python 3.x
- pip
- AWS CLI configurado con las credenciales de acceso
- Entorno virtual de Python

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

    git clone https://github.com/tu-usuario/flask-s3-bucket-lister.git
    cd flask-s3-bucket-lister

## 2. Crear y activar un entorno virtual
Crea un entorno virtual para el proyecto:

    python3 -m venv myenv
    source myenv/bin/activate

## 3. Instalar las dependencias
Instala las dependencias necesarias utilizando pip:

    pip install Flask boto3
    
## 4. Configurar AWS CLI
Asegúrate de que la AWS CLI esté configurada en tu sistema con las credenciales correctas:

    aws configure


## 1. Ejecutar la aplicación
Con el entorno virtual activado, ejecuta la aplicación Flask:

    Copiar código
    python app.py
    
## 2. Acceder a la aplicación
Abre tu navegador y navega a las siguientes URLs:
    HTML: http://127.0.0.1:5000/ - Muestra la lista de buckets de S3 en formato HTML.
    JSON: http://127.0.0.1:5000/api/buckets - Devuelve la lista de buckets de S3 en formato JSON.
    
## Estructura del Proyecto

    flask-s3-bucket-lister/
    │
    ├── app.py              # Código principal de la aplicación Flask
    ├── templates/
    │   └── buckets.html    # Plantilla HTML para mostrar los buckets
    ├── README.md           # Este archivo README
    └── myenv/              # Entorno virtual (no se incluye en el repositorio)
    
## Contribuir
Si deseas contribuir a este proyecto, por favor, crea un fork y envía un pull request con tus mejoras o correcciones.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

