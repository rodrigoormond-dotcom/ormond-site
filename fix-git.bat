@echo off
cd /d "%~dp0"
echo.
echo === Corrigindo indice git ===
echo.

:: Mata processos git travados
taskkill /f /im git.exe >nul 2>&1
taskkill /f /im git-remote-https.exe >nul 2>&1

:: Aguarda um momento
timeout /t 2 /nobreak >nul

:: Remove todos os locks
if exist ".git\index.lock" del /f ".git\index.lock"
if exist ".git\MERGE_HEAD" del /f ".git\MERGE_HEAD"
if exist ".git\ORIG_HEAD.lock" del /f ".git\ORIG_HEAD.lock"
if exist ".git\maintenance.lock" del /f ".git\maintenance.lock"

git config gc.auto 0

echo Reconstruindo indice...
git rm --cached -r . --quiet
git add -A
echo.
git status --short
echo.

echo Commitando e publicando...
git commit -m "add: og image width height + fix indice git"
git push origin main

echo.
echo === Pronto! ===
echo.
pause
