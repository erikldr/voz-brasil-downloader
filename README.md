# Voz do Brasil Downloader

Download automatizado do programa "A Voz do Brasil" diretamente do site oficial da EBC (Empresa Brasil de Comunicação).

## Características

- Download do programa do dia atual
- Download de programas de datas específicas
- Especificação do nome do arquivo de saída
- Escolha do diretório de destino
- Criação automática de diretórios

## Requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/erikldr/voz-brasil-downloader.git
cd voz-brasil-downloader
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar

### Download do programa do dia atual:
```bash
python src/downloader.py --filename "voz_brasil" --dest "./downloads"
```

### Download de uma data específica:
```bash
python src/downloader.py --filename "voz_brasil" --dest "./downloads" --data 05112024
```

### Parâmetros:

- `--filename`: Nome base do arquivo (obrigatório)
- `--dest`: Diretório onde o arquivo será salvo (obrigatório)
- `--data`: Data específica no formato DDMMAAAA (opcional)

O arquivo será salvo com o nome no formato: `{filename}.mp3`

## Automatização

O projeto oferece duas formas de automatizar os downloads:

### 1. Usando Windows Task Scheduler

1. Configure o arquivo `automation/run_downloader.bat`
2. Abra o Task Scheduler do Windows
3. Crie uma nova tarefa básica
4. Configure para executar diariamente às 20:30
5. Aponte para o arquivo .bat

### 2. Usando Python Scheduler

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o scheduler:
```bash
python automation/scheduler.py
```

O scheduler irá:
- Executar o download todos os dias às 20:30
- Pular automaticamente fins de semana
- Manter logs de execução em `logs/voz_brasil_scheduler.log`
- Salvar os arquivos na pasta `downloads`

## Observações

- O programa "A Voz do Brasil" é transmitido apenas em dias úteis
- Os arquivos ficam disponíveis algumas horas após a transmissão
- Em caso de erro, verifique se a data é válida e se não é fim de semana
