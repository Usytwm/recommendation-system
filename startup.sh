echo "[Activando entorno virtual...]"
source venv/Scripts/activate
echo "Completado"
echo "---------------------------------"

echo "[Instalando dependencias...]"
pip3 install -r requirements.txt
echo "Completado"
echo "---------------------------------"

echo "[Navegando al directorio src...]"
cd src
echo "Completado"
echo "---------------------------------"

echo "[Ejecutando script de GUI...]"
python3 gui/main.py
echo "Completado"
echo "---------------------------------"

echo "[Regresando al directorio raíz...]"
cd ..
echo "Completado"
echo "---------------------------------"

echo "Script finalizado."

