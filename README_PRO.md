# URL Hunter 🔍⚡

Versão otimizada para arquivos grandes e uso intensivo.

## 🚀 Principais Melhorias da Versão Otimizada

### ⚡ **Performance Avançada**
- **Processamento em Chunks**: Arquivos grandes são processados em pedaços para economizar memória
- **Barra de Progresso**: Visualização em tempo real do progresso da busca
- **Estimativa de Tempo**: Calcula tempo restante baseado na velocidade atual
- **Cancelamento Inteligente**: Permite cancelar buscas longas com Ctrl+C

### 📊 **Monitoramento Avançado**
- **Estatísticas Detalhadas**: Número de linhas, tamanho do arquivo, velocidade de processamento
- **Uso de Memória**: Monitoramento do consumo de RAM
- **Logs Profissionais**: Sistema de logging para auditoria
- **Histórico de Buscas**: Mantém registro das buscas realizadas

### 🛡️ **Segurança e Estabilidade**
- **Validação Robusta**: Verificações de segurança para arquivos
- **Tratamento de Erros**: Recuperação automática de problemas
- **Backup Automático**: Salvamento automático de resultados importantes
- **Sanitização**: Nomes de arquivo seguros e validação de entrada

## 📋 Comparação: Versão Normal vs Otimizada

| Característica | Versão Normal | Versão Otimizada |
|----------------|---------------|---------------------|
| **Limite de Arquivo** | 100MB | 1GB |
| **Processamento** | Carregamento completo | Chunks inteligentes |
| **Barra de Progresso** | ❌ | ✅ |
| **Estimativa de Tempo** | ❌ | ✅ |
| **Cancelamento** | ❌ | ✅ |
| **Logs** | ❌ | ✅ |
| **Backup** | ❌ | ✅ |
| **Estatísticas** | Básicas | Avançadas |

## 🚀 Como Usar a Versão Otimizada

### 1. **Execução Básica**
```bash
python3 url_hunter_pro.py
```

### 2. **Configuração Avançada**
Edite `config_pro.py` para personalizar:
```python
# Aumentar limite de arquivo
MAX_FILE_SIZE_MB = 2000  # 2GB

# Ajustar tamanho dos chunks
CHUNK_SIZE = 20000  # Mais linhas por chunk

# Ativar logs detalhados
ENABLE_LOGGING = True
LOG_LEVEL = "DEBUG"
```

### 3. **Perfis de Performance**
A versão otimizada detecta automaticamente o tamanho do arquivo e ajusta:
- **Small** (< 50MB): Chunks de 5k linhas
- **Medium** (50-200MB): Chunks de 10k linhas  
- **Large** (200-500MB): Chunks de 20k linhas
- **Huge** (> 500MB): Chunks de 50k linhas

## 📊 Exemplo de Uso Otimizado

```bash
$ python3 url_hunter_pro.py

 ==* coded by *== 

 ██▒   █▓ ██▓ ██▓     ██▓    ▄▄▄       ███▄    █ 
▓██░   █▒▓██▒▓██▒    ▓██▒   ▒████▄     ██ ▀█   █ 
 ▓██  █▒░▒██▒▒██░    ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒
  ▒██ █░░░██░▒██░    ▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒
   ▒▀█░  ░██░░██████▒░██████▒▓█   ▓██▒▒██░   ▓██░
   ░ ▐░  ░▓  ░ ▒░▓  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ 
   ░ ░░   ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░
     ░░   ▒ ░  ░ ░     ░ ░    ░   ▒      ░   ░ ░ 
      ░   ░      ░  ░    ░  ░     ░  ░         ░ 
     ░                                           
      ==*  VL ~ villanelle | t.me/vi77an *==
      === VERSÃO OTIMIZADA ===

+-+-+-+-+-++-+-+-+-+-++-+-+-+
.:|| URL:LOG:PASS HUNTER ||:.
+-+-+-+-+-++-+-+-+-+-++-+-+-+

[💌] Arquivos disponíveis:
  [1] dados_grandes.txt (850.3MB, 2,500,000 linhas) - Analisando...
  [1] dados_grandes.txt (850.3MB, 2,500,000 linhas)
  [0] Cancelar e sair

[*] Selecione o número do arquivo desejado: 1
[✅] Arquivo selecionado: dados_grandes.txt
[📋] Informações do arquivo:
  📁 Arquivo: dados_grandes.txt
  📊 Tamanho: 850.3MB
  📝 Linhas: 2,500,000
  ⚡ Velocidade estimada: 50k linhas/segundo

[*] Domínio ou parte do domínio (ex: insta): gmail
[🔍] Iniciando busca por 'gmail'...
[📊] Arquivo: dados_grandes.txt (2,500,000 linhas)
[🔍] Processando busca por 'gmail'... aguarde.
✅ Busca concluída em 45.2s | Total: 1,247 resultados
[💚] CONFIRA >> resultados/resultado_gmail_20241206_143022.txt
[📊] 1,247 resultados salvos
```

## ⚙️ Configurações Avançadas

### **Otimização de Memória**
```python
# config_pro.py
MAX_MEMORY_USAGE_MB = 1000  # 1GB de limite de memória
CHUNK_SIZE = 50000  # Chunks maiores para arquivos enormes
```

### **Logs Detalhados**
```python
ENABLE_LOGGING = True
LOG_LEVEL = "DEBUG"  # Logs muito detalhados
LOG_FILE = "url_hunter_debug.log"
```

### **Backup Automático**
```python
AUTO_BACKUP_RESULTS = True
BACKUP_DIR = "backups"
MAX_BACKUP_FILES = 20
```

## 🔧 Recursos Avançados

### **1. Monitoramento de Performance**
- Velocidade de processamento em tempo real
- Uso de memória monitorado
- Estimativas precisas de tempo restante

### **2. Cancelamento Inteligente**
- Ctrl+C para cancelar buscas longas
- Salvamento parcial de resultados
- Recuperação graciosa de interrupções

### **3. Logs Profissionais**
- Registro detalhado de todas as operações
- Histórico de buscas com estatísticas
- Debugging avançado para troubleshooting

### **4. Backup e Segurança**
- Backup automático de resultados importantes
- Validação de integridade de arquivos
- Sanitização de nomes de arquivo

## 📈 Casos de Uso Avançados

### **1. Arquivos Muito Grandes (> 500MB)**
```bash
# A versão otimizada processa eficientemente
python3 url_hunter_pro.py
# Selecionar arquivo grande
# Busca com barra de progresso e estimativas
```

### **2. Processamento em Lote**
```bash
# Script para múltiplos arquivos
for file in *.txt; do
    echo "Processando $file..."
    python3 url_hunter_pro.py --file "$file" --search "termo"
done
```

### **3. Monitoramento de Performance**
```bash
# Logs detalhados para análise
tail -f url_hunter.log
```

## 🛠️ Requisitos Avançados

- **Python 3.8+**: Para recursos avançados
- **8GB+ RAM**: Para arquivos muito grandes
- **SSD**: Para melhor performance de I/O
- **Terminal com cores**: Para interface otimizada

## 📊 Estatísticas de Performance

| Tamanho do Arquivo | Tempo Estimado | Memória Usada |
|-------------------|----------------|---------------|
| 100MB | 30s | 200MB |
| 500MB | 2.5min | 500MB |
| 1GB | 5min | 800MB |
| 2GB | 10min | 1.2GB |

## 🎯 Melhorias Futuras

- [ ] Busca com expressões regulares
- [ ] Busca fuzzy (aproximada)
- [ ] Processamento paralelo
- [ ] Interface gráfica
- [ ] API REST
- [ ] Integração com bancos de dados

## 👨‍💻 Autor

**VL ~ villanelle** | [Telegram](https://t.me/vi77an)

## 📄 Licença

Este projeto é de uso pessoal e educacional. 