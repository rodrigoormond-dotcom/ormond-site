@echo off
cd /d "%~dp0"
echo.
echo === ORMOND STUDIO — Publicar no GitHub ===
echo.

:: Mata processos git travados
taskkill /f /im git.exe >nul 2>&1
taskkill /f /im git-remote-https.exe >nul 2>&1
timeout /t 2 /nobreak >nul

:: Remove todos os locks
if exist ".git\index.lock" del /f ".git\index.lock"
if exist ".git\MERGE_HEAD" del /f ".git\MERGE_HEAD"
if exist ".git\ORIG_HEAD.lock" del /f ".git\ORIG_HEAD.lock"
if exist ".git\maintenance.lock" del /f ".git\maintenance.lock"

git config gc.auto 0

:: Pega mudancas do remoto sem sobrescrever as locais
git fetch origin main
git merge origin/main --no-edit --strategy-option=ours

:: Adiciona tudo e publica
git add -A
git commit -m "add: SEO estrategico - titulos, schema, sitemap, cidades Sul do Brasil"
git push origin main

echo.
echo === Pronto! Site publicado em ormondimagens.com.br ===
echo.
pause
