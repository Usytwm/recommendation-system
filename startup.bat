@echo off
echo [Activando entorno virtual...]
call venv\Scripts\activate.bat
echo ----------Completado----------

echo [Instalando dependencias...]
pip install -r requirements.txt
echo ----------Completado----------

echo [Navegando al directorio src...]
cd src
echo ----------Completado----------

echo [Ejecutando script de GUI...]
python project_code\code.py
echo ----------Completado----------

echo [Regresando al directorio raiz...]
cd ..
echo ----------Completado----------

echo Script finalizado.

