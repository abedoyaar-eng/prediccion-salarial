Predicción Salarial — Proyecto Ciencia de los Datos

Universidad Nacional de Colombia
Entrega: 21 de noviembre

Integrantes del grupo
Nombre	Correo UNAL
Anderson Bedoya	abedoyaar@unal.edu.co

Sergio Gómez Galeano	segomezga@unal.edu.co
Descripción del proyecto

Este proyecto implementa una aplicación completa para la predicción de salarios utilizando tres modelos de Machine Learning:

Regresión Lineal: predice el valor numérico del salario.

KNN: predice el rango salarial (Muy bajo, Bajo, Medio, Alto, Muy alto).

MLP (Perceptrón Multicapa): también predice el rango salarial.

La aplicación está dividida en dos partes:

1. Frontend

Interfaz web donde el usuario puede ingresar sus datos:

Edad

Género

Nivel educativo

Título de trabajo

Años de experiencia

Modelo de predicción a utilizar

El resultado aparece directamente en pantalla.

2. Backend

API construida en Flask, encargada de:

Recibir los datos desde el frontend

Procesarlos

Seleccionar el modelo solicitado

Retornar la predicción generada

El backend contiene:

Código de la API (app.py)

Modelos entrenados (.pkl)

Escaladores y columnas del One-Hot Encoding

Archivos de datos (.csv y .json)

Estructura del repositorio
prediccion-salarial/
│
├── backend/
│   ├── app.py
│   ├── knn_model.pkl
│   ├── mlp_model.pkl
│   ├── regresion_model.pkl
│   ├── scaler_knn.pkl
│   ├── scaler_mlp.pkl
│   ├── scaler_regresion.pkl
│   ├── ohe_columns.pkl
│   └── data/
│       ├── job_titles.json
│       └── Salary_Data_Procesada_Numerica.csv
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── styles.css
│
└── README.md

Requisitos del sistema

Antes de ejecutar el proyecto, se debe tener instalado:

1. Python (versión 3.10 o superior)

Puedes verificarlo con:

python --version

2. Pip (gestor de paquetes de Python)

Verificar con:

pip --version

3. Navegador web actualizado

(Chrome, Edge, Firefox, etc.)

Instalación de dependencias

En la carpeta raíz del proyecto, ejecutar:

pip install flask flask-cors pandas numpy scikit-learn joblib


Esto instala todo lo necesario para que funcione la API.

Ejecución del backend

Abrir una terminal y ubicarse en la carpeta:

cd backend


Ejecutar el servidor Flask:

python app.py


Cuando aparezca el mensaje:

Running on http://127.0.0.1:5000


el backend ya está funcionando correctamente.

Ejecución del frontend

El frontend funciona simplemente abriendo el archivo:

frontend/index.html


Pasos:

Abrir la carpeta frontend/.

Hacer doble clic en index.html.

La interfaz se abrirá en el navegador.

Ingresar los datos y seleccionar un modelo.

Presionar el botón Conocer predicción.

Nota: Para que funcione la comunicación, el backend debe estar corriendo en la terminal.

Cómo funciona la comunicación

El frontend envía una solicitud HTTP al backend.

El backend recibe los datos, selecciona el modelo indicado y genera la predicción.

El frontend muestra el resultado de inmediato en pantalla.

Observaciones finales

Este proyecto cumple los requisitos del curso:

Tres modelos implementados

API en Flask

Frontend funcional

Comunicación completa entre frontend y backend

Repositorio con estructura correcta

Instrucciones claras para despliegue
