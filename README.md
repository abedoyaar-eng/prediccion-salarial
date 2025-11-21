Predicción Salarial — Proyecto Ciencia de los Datos

Universidad Nacional de Colombia
Entrega: 21 de noviembre

👥 Integrantes del grupo
Nombre Completo	Correo UNAL
Anderson Bedoya	abedoyaar@unal.edu.co

Sergio Gómez Galeano	segomezga@unal.edu.co
🧠 Descripción del proyecto

Este proyecto implementa una aplicación completa de predicción salarial usando tres modelos de Machine Learning:

Regresión Lineal (predice el salario en valor numérico)

KNN (predice el rango salarial)

MLP (red neuronal, también predice el rango salarial)

La aplicación está dividida en dos partes:

✔ Frontend

Interfaz web donde el usuario ingresa su edad, género, nivel educativo, años de experiencia y título de trabajo.
Luego selecciona el modelo y ve el resultado directamente en pantalla.

✔ Backend (API con Flask)

Recibe los datos del usuario, ejecuta el modelo seleccionado y devuelve la predicción al frontend.

Todo está conectado y funcionando de forma interactiva.

📁 Estructura del repositorio
prediccion-salarial/
│
├── backend/
│   ├── app.py
│   ├── regresion_model.pkl
│   ├── scaler_regresion.pkl
│   ├── knn_model.pkl
│   ├── scaler_knn.pkl
│   ├── mlp_model.pkl
│   ├── scaler_mlp.pkl
│   ├── ohe_columns.pkl
│   └── data/
│       ├── Salary_Data_Procesada_Numerica.csv
│       └── job_titles.json
│
└── frontend/
    ├── index.html
    ├── styles.css
    └── script.js

🛠️ Guía paso a paso para ejecutar el proyecto

A continuación tendrás una guía escrita como si la persona jamás hubiera visto Python ni programación.
Sigue exactamente cada paso y funciona sin errores.

1️⃣ Instalar Python

Este proyecto funciona con Python 3.10 o superior.

▶ Windows

Ir a:
https://www.python.org/downloads/windows/

Descargar Windows Installer.

MUY IMPORTANTE:
☑ Marcar la casilla "Add Python to PATH"

Instalar.

▶ Mac

https://www.python.org/downloads/macos/

▶ Linux

Python ya viene instalado.
Verifica con:

python3 --version

2️⃣ Instalar dependencias del backend

Abrir una terminal dentro de la carpeta backend/.

✔ Windows:

Abre la carpeta backend.

Mantén SHIFT presionado.

Haz clic derecho → “Open PowerShell window here”.

Ejecutar este comando:
pip install flask flask-cors scikit-learn pandas numpy joblib


Esto instala:

Flask (API)

CORS

Modelos de ML

Lectura de CSV

Conversión numérica

3️⃣ Ejecutar el backend

Desde la carpeta backend/:

python app.py


Si todo está bien, verás algo así:

Running on http://127.0.0.1:5000


No cierres esta ventana.
Debe quedar abierta mientras usas la aplicación.

4️⃣ Abrir el frontend

Ahora abre la carpeta frontend/ y haz doble clic en:

index.html


La página se abre automáticamente en tu navegador.

5️⃣ Usar la aplicación

Completa los campos:

Edad

Género

Nivel educativo

Título de trabajo

Años de experiencia

Elige un modelo:

Regresión

KNN

MLP

Haz clic en "Conocer predicción".

El resultado aparece inmediatamente en la tarjeta inferior.

💡 Recomendaciones importantes

El backend SIEMPRE debe ejecutarse antes de abrir la página.

Si el frontend muestra "Error de conexión al backend", significa que:

el backend no está ejecutándose, o

se cerró la ventana donde estaba corriendo Flask.

📌 Notas técnicas (opcionales para el docente)

Los modelos fueron entrenados con el dataset procesado final.

Regresión usa One Hot Encoding de forma consistente con el backend.

KNN y MLP utilizan archivos .pkl generados desde Google Colab.

Todo el proyecto está organizado siguiendo buenas prácticas básicas:

separación frontend/backend

API REST

manejo de CORS

escalado y vectorización alineada
