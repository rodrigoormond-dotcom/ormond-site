@echo off
cd /d "%~dp0"
echo.
echo === ORMOND STUDIO — Publicar no GitHub ===
echo.

:: Remove lock file se existir (lock travado)
if exist ".git\index.lock" (
  echo Removendo lock travado...
  del /f ".git\index.lock"
)
if exist ".git\MERGE_HEAD" (
  del /f ".git\MERGE_HEAD"
)

:: Sincroniza com o remoto antes de publicar
echo Sincronizando com GitHub...
git pull origin main --rebase

git add -A
git commit -m "add: og tags preview de link + post fazenda bom retiro com todas as imagens"
git push origin main
echo.
echo === Pronto! Site publicado em ormondimagens.com.br ===
echo.
pause
