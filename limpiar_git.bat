@echo off
echo.
echo === Generando .gitignore ===
echo data/> .gitignore
echo reports/>> .gitignore
echo models/>> .gitignore
echo __pycache__/>> .gitignore
echo *.pyc>> .gitignore
echo *.pkl>> .gitignore
echo.

echo === Eliminando archivos grandes del control de Git ===
git rm --cached -r data
git rm --cached -r reports
git rm --cached -r models
echo.

echo === Agregando y haciendo commit ===
git add .gitignore
git commit -m "Ignorar archivos pesados, limpiar Git"

echo.
echo === Subiendo a GitHub ===
git push origin main

echo.
echo ✔️ Sincronización completa. Presiona una tecla para cerrar.
pause >nul
