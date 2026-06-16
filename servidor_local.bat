@echo off
echo Iniciando servidor local...
echo Acesse: http://localhost:8000
echo Para encerrar: Ctrl+C
echo.
cd /d "%~dp0"
python -m http.server 8000
pause
