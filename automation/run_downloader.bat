@echo off
:: Ativa o ambiente Python (ajuste o caminho conforme seu ambiente)
call C:\Users\SeuUsuario\anaconda3\Scripts\activate.bat

:: Vai para o diretório do projeto
cd %~dp0..

:: Executa o script Python
python src/downloader.py --filename "voz_brasil" --dest "C:\Caminho\Para\Downloads"

:: Log de execução
echo %date% %time% - Script executado >> logs\execucao.log