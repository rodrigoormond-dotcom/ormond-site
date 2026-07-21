@echo off
cd /d "%~dp0"
echo.
echo === ORMOND STUDIO — Publicar no GitHub ===
echo.

:: Desativa limpeza automatica (evita conflito com OneDrive)
git config gc.auto 0

:: Remove lock travado se existir
if exist ".git\index.lock" del /f ".git\index.lock"

:: Guarda alteracoes locais, puxa remoto, restaura
git stash
git pull origin main --no-rebase
git stash pop

:: Publica
git add -A
git commit -m "update: publicacao site ormond"
git push origin main

echo.
echo === Pronto! Site publicado em ormondimagens.com.br ===
echo.
pause
