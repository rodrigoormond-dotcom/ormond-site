@echo off
cd /d "%~dp0"
echo.
echo === Corrigindo repositorio git ===
echo.

:: Remove todos os locks
if exist ".git\index.lock" del /f ".git\index.lock"
if exist ".git\MERGE_HEAD" del /f ".git\MERGE_HEAD"
if exist ".git\ORIG_HEAD.lock" del /f ".git\ORIG_HEAD.lock"
if exist ".git\maintenance.lock" del /f ".git\maintenance.lock"

:: Desativa gc automatico (evita conflito com OneDrive)
git config gc.auto 0

:: Puxa e faz merge com o remoto
git fetch origin main
git merge origin/main --no-edit

:: Puxa nossas alteracoes e publica
git add -A
git commit -m "add: og tags preview de link em todas as paginas"
git push origin main

echo.
echo === Pronto! ===
echo.
pause
