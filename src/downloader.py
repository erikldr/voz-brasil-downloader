#!/usr/bin/env python3
"""
Voz do Brasil Downloader

Este script permite fazer o download automático do programa "A Voz do Brasil"
a partir do site oficial da EBC (Empresa Brasil de Comunicação).

O programa permite especificar o nome do arquivo de saída e o diretório de destino,
além de possibilitar o download de programas de datas específicas.

Exemplo de uso:
    python downloader.py --filename "voz_brasil" --dest "./downloads"
    python downloader.py --filename "voz_brasil" --dest "./downloads" --data 05112024
"""

import requests
from datetime import datetime
import os
import logging
from pathlib import Path
import argparse
import textwrap

def criar_parser():
    """
    Cria e configura o parser de argumentos da linha de comando.

    Returns:
        argparse.ArgumentParser: Parser configurado com os argumentos necessários.
    """
    parser = argparse.ArgumentParser(
        description='Download automatizado do programa A Voz do Brasil',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
            Exemplos de uso:
              %(prog)s --filename voz_brasil --dest ./downloads
              %(prog)s --filename programa --dest "D:/Arquivos/Radio" --data 05112024
        ''')
    )
    
    parser.add_argument('--filename', 
                      help='Nome base do arquivo (será adicionada a data ao final)',
                      required=True)
    parser.add_argument('--dest',
                      help='Diretório de destino onde o arquivo será salvo',
                      required=True)
    parser.add_argument('--data',
                      help='Data específica para download no formato DDMMAAAA (opcional)')
    return parser

def download_voz_do_brasil(diretorio, nome_arquivo, data=None):
    """
    Realiza o download do arquivo de áudio da Voz do Brasil.

    Args:
        diretorio (str): Caminho do diretório onde o arquivo será salvo
        nome_arquivo (str): Nome base do arquivo (sem extensão)
        data (datetime, optional): Data específica para download. 
                                 Se None, usa a data atual.

    Returns:
        bool: True se o download foi bem sucedido, False caso contrário.
    """
    if data is None:
        data = datetime.now()
    
    # Formata a data para o nome do arquivo e URL
    data_formatada = data.strftime("%d-%m-%y")
    
    # Cria o diretório se não existir
    diretorio = Path(diretorio)
    diretorio.mkdir(parents=True, exist_ok=True)
    
    # Monta a URL
    url = f"https://audios.ebc.com.br/radiogov/{data.year}/{data.month}/{data_formatada}-a-voz-do-brasil.mp3"
    
    # Nome completo do arquivo
    nome_completo = diretorio / f"{nome_arquivo}.mp3"
    
    #print(f"URL: {url}")
    #print(f"Salvando em: {nome_completo}")
    
    try:
        # Faz o download do arquivo
        print(f"Baixando arquivo de {data_formatada}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Salva o arquivo
        with open(nome_completo, 'wb') as arquivo:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    arquivo.write(chunk)
        
        tamanho_mb = os.path.getsize(nome_completo) / 1024 / 1024
        print(f"Download concluído! Arquivo salvo como: {nome_completo}")
        print(f"Tamanho do arquivo: {tamanho_mb:.2f} MB")
        return True
                
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        return False

def main():
    """
    Função principal que processa os argumentos e inicia o download.
    """
    parser = criar_parser()
    args = parser.parse_args()
    
    if args.data:
        try:
            data = datetime.strptime(args.data, '%d%m%Y')
        except ValueError:
            print("Erro: Data inválida. Use o formato DDMMAAAA (exemplo: 06112024)")
            exit(1)
    else:
        data = None
        
    download_voz_do_brasil(args.dest, args.filename, data)

if __name__ == "__main__":
    main()