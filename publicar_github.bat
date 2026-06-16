@echo off
echo ============================================
echo  ORMOND STUDIO - Publicar no GitHub Pages
echo ============================================
echo.

cd /d "%~dp0"

echo [1/5] Inicializando Git...
git init
git branch -M main

echo.
echo [2/5] Adicionando arquivos...
git add .

echo.
echo [3/5] Criando commit...
git commit -m "feat: ormond studio site launch"

echo.
echo ============================================
echo  AGORA: crie o repositorio em github.com/new
echo  Nome: ormond-site  (publico, sem README)
echo ============================================
echo.
pause

echo.
echo [4/5] Digite o URL do repositorio GitHub:
echo  Exemplo: https://github.com/Ormond/ormond-site.git
echo.
set /p REPO_URL="URL: "

git remote add origin %REPO_URL%

echo.
echo [5/5] Fazendo push...
git push -u origin main

echo.
echo ============================================
echo  PRONTO! Agora ative o GitHub Pages:
echo  Settings - Pages - main / root - Save
echo ============================================
echo.
pause
