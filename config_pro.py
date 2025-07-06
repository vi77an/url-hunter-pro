"""
Configurações Avançadas - URL Hunter
"""

# ================ CONFIGURAÇÕES DE PERFORMANCE ================
CHUNK_SIZE = 10000  # Linhas por chunk
MAX_MEMORY_USAGE_MB = 500  # Limite de memória em MB
PROGRESS_UPDATE_INTERVAL = 0.1  # Segundos entre atualizações da barra
CANCEL_CHECK_INTERVAL = 1000  # Verificar cancelamento a cada N linhas

# ================ CONFIGURAÇÕES DE ARQUIVO ================
SUPPORTED_EXTENSIONS = ['.txt']
MAX_FILE_SIZE_MB = 1000  # Limite aumentado para versão otimizada
DEFAULT_ENCODING = 'utf-8'
FALLBACK_ENCODING = 'latin-1'

# ================ CONFIGURAÇÕES DE BUSCA ================
SEARCH_CASE_SENSITIVE = False
MAX_RESULTS_DISPLAY = 10000  # Aumentado para versão otimizada
ENABLE_REGEX_SEARCH = False  # Busca com regex (futuro)
ENABLE_FUZZY_SEARCH = False  # Busca fuzzy (futuro)

# ================ CONFIGURAÇÕES DE ARQUIVO DE SAÍDA ================
OUTPUT_FILE_PREFIX = "resultado_"
SAFE_FILENAME_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_."
INCLUDE_TIMESTAMP = True
INCLUDE_HEADER_INFO = True

# ================ CONFIGURAÇÕES DE INTERFACE ================
SHOW_FILE_SIZE = True
SHOW_LINE_COUNT = True
SHOW_PROGRESS = True
SHOW_ESTIMATED_TIME = True
SHOW_MEMORY_USAGE = True
ENABLE_COLOR_OUTPUT = True

# ================ CONFIGURAÇÕES DE LOGGING ================
ENABLE_LOGGING = True
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "url_hunter.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# ================ CONFIGURAÇÕES DE SEGURANÇA ================
VALIDATE_FILE_EXTENSION = True
CHECK_FILE_PERMISSIONS = True
SANITIZE_FILENAMES = True
MAX_CONCURRENT_SEARCHES = 1

# ================ CONFIGURAÇÕES DE ESTATÍSTICAS ================
TRACK_SEARCH_STATS = True
SAVE_SEARCH_HISTORY = True
HISTORY_FILE = "search_history.json"
MAX_HISTORY_ENTRIES = 100

# ================ MENSAGENS PERSONALIZÁVEIS ================
MESSAGES = {
    'no_files_found': "[💔] Nenhum arquivo .txt foi encontrado no diretório atual.",
    'file_too_large': "[⚠️] Arquivo muito grande ({size:.1f}MB). Máximo: {max}MB",
    'file_loaded': "[✅] Arquivo carregado: {filename} ({lines} linhas)",
    'searching': "[🔍] Buscando por '{term}'...",
    'no_results': "[!] Vixe, não encontramos nada com '{term}'.",
    'results_saved': "[💚] CONFIRA >> {filename}",
    'results_count': "[📊] {count} resultados salvos",
    'continue_prompt': "[?] Continuar? (s/n): ",
    'goodbye': "[👋] Ok, até a próxima!",
    'invalid_input': "[💔] Entrada inválida. Digite um número correspondente a um arquivo.",
    'empty_search': "[⚠️] Termo de busca não pode estar vazio.",
    'interrupted': "[⚠️] Programa interrompido pelo usuário.",
    'unexpected_error': "[💔] Erro inesperado: {error}",
    'finished': "[👋] Programa finalizado.",
    'search_cancelled': "[⚠️] Busca cancelada pelo usuário.",
    'memory_warning': "[⚠️] Uso de memória alto: {usage:.1f}MB",
    'processing_large_file': "[📊] Processando arquivo grande...",
    'estimated_time': "[⏱️] Tempo estimado: {time}",
    'search_complete': "[✅] Busca concluída em {time}",
    'performance_tip': "[💡] Dica: Para arquivos muito grandes, considere dividir em partes menores."
}

# ================ CONFIGURAÇÕES DE CORES ================
COLORS = {
    'RESET': "\033[0m",
    'RED': "\033[38;5;198m",
    'PURPLE': "\033[38;5;135m", 
    'BLUE': "\033[38;5;81m",
    'GREEN': "\033[38;5;119m",
    'YELLOW': "\033[38;5;226m",
    'CYAN': "\033[38;5;51m",
    'ORANGE': "\033[38;5;208m",
    'PINK': "\033[38;5;213m"
}

# ================ CONFIGURAÇÕES DE PERFORMANCE AVANÇADAS ================
# Otimizações para diferentes tipos de arquivo
PERFORMANCE_PROFILES = {
    'small': {
        'chunk_size': 5000,
        'memory_limit': 100,
        'progress_interval': 0.05
    },
    'medium': {
        'chunk_size': 10000,
        'memory_limit': 250,
        'progress_interval': 0.1
    },
    'large': {
        'chunk_size': 20000,
        'memory_limit': 500,
        'progress_interval': 0.2
    },
    'huge': {
        'chunk_size': 50000,
        'memory_limit': 1000,
        'progress_interval': 0.5
    }
}

# ================ CONFIGURAÇÕES DE BACKUP ================
AUTO_BACKUP_RESULTS = True
BACKUP_DIR = "backups"
MAX_BACKUP_FILES = 10
BACKUP_RETENTION_DAYS = 30

# ================ CONFIGURAÇÕES DE EXPORTAÇÃO ================
EXPORT_FORMATS = ['txt', 'csv', 'json']
DEFAULT_EXPORT_FORMAT = 'txt'
INCLUDE_METADATA_IN_EXPORT = True

# ================ CONFIGURAÇÕES DE FILTROS AVANÇADOS ================
ENABLE_ADVANCED_FILTERS = False
FILTER_OPTIONS = {
    'exact_match': False,
    'case_sensitive': False,
    'whole_word': False,
    'exclude_patterns': [],
    'include_patterns': []
}

# ================ CONFIGURAÇÕES DE NOTIFICAÇÕES ================
ENABLE_NOTIFICATIONS = False
NOTIFICATION_TYPES = {
    'search_complete': True,
    'large_file_warning': True,
    'memory_warning': True,
    'error_notification': True
} 