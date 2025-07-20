@echo off
REM Navega para o diretório onde este arquivo .bat está localizado
cd /d "%~dp0"

REM MUDANÇA AQUI: Usa o comando "start" para iniciar o programa em um novo processo
REM e fechar esta janela de console imediatamente. As aspas vazias no início são necessárias.
start "" ".\.venv\Scripts\pythonw.exe" "mac_lookupG6.py"

exit