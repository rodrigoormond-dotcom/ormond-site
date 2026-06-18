@echo off
cd /d "%~dp0"
echo.
echo === ORMOND STUDIO — Publicar no GitHub ===
echo.
git add -A
git commit -m "fix: strips homepage, nav categorias, thera no blog"
git push origin main
echo.
echo === Pronto! Site publicado em rodrigoormond-dotcom.github.io ===
echo.
echo Para o dominio ormondimagens.com.br funcionar, configure os DNS:
echo   Tipo A  @   185.199.108.153
echo   Tipo A  @   185.199.109.153
echo   Tipo A  @   185.199.110.153
echo   Tipo A  @   185.199.111.153
echo   CNAME   www rodrigoormond-dotcom.github.io
echo.
pause
