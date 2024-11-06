#!/usr/bin/env python3
"""
Agendador para o Voz do Brasil Downloader.
Este script executa o download automaticamente todos os dias às 20:30,
exceto fins de semana.
"""

import schedule
import time
from datetime import datetime
import subprocess
import logging
from pathlib import Path
import os

# Obtém o diretório do projeto (um nível acima do diretório automation)
PROJECT_DIR = Path(__file__).parent.parent.absolute()

# Configuração do logging
log_dir = PROJECT_DIR / 'logs'
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / 'voz_brasil_scheduler.log'),
        logging.StreamHandler()
    ]
)

def is_weekday():
    """Verifica se hoje é dia útil (não é sábado nem domingo)"""
    return datetime.now().weekday() < 5

def executar_download():
    """Executa o script de download se for dia útil"""
    if not is_weekday():
        logging.info("Hoje é fim de semana. Download não será realizado.")
        return

    try:
        logging.info("Iniciando download da Voz do Brasil...")
        
        # Monta o caminho para o script e diretório de downloads
        script_path = PROJECT_DIR / 'src' / 'downloader.py'
        downloads_dir = PROJECT_DIR / 'downloads'
        downloads_dir.mkdir(exist_ok=True)
        
        comando = [
            'python',
            str(script_path),
            '--filename', 'voz_brasil',
            '--dest', str(downloads_dir)
        ]
        
        resultado = subprocess.run(
            comando, 
            capture_output=True, 
            text=True,
            cwd=str(PROJECT_DIR)
        )
        
        if resultado.returncode == 0:
            logging.info("Download concluído com sucesso!")
            if resultado.stdout:
                logging.info(f"Saída: {resultado.stdout}")
        else:
            logging.error(f"Erro no download: {resultado.stderr}")
            
    except Exception as e:
        logging.error(f"Erro ao executar o download: {e}")

def main():
    """Função principal que configura e executa o agendador"""
    logging.info("Iniciando agendador da Voz do Brasil...")
    logging.info(f"Diretório do projeto: {PROJECT_DIR}")
    
    # Agenda para 20:30 todos os dias
    schedule.every().day.at("20:30").do(executar_download)
    
    logging.info("Agendador configurado. Downloads programados para 20:30")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Verifica a cada minuto

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Agendador finalizado pelo usuário")
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")