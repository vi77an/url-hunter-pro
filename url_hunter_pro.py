#!/usr/bin/env python3
"""
URL Hunter - Versão otimizada para arquivos grandes
Autor: VL ~ villanelle | t.me/vi77an
"""

import os
import sys
import time
import threading
from typing import List, Optional, Generator, Tuple
from pathlib import Path
import itertools
from dataclasses import dataclass
from config import *

# ================ CONSTANTES DE CORES ================
class Colors:
    """Cores ANSI para formatação do terminal"""
    RESET = "\033[0m"
    RED = "\033[38;5;198m"
    PURPLE = "\033[38;5;135m"
    BLUE = "\033[38;5;81m"
    GREEN = "\033[38;5;119m"
    YELLOW = "\033[38;5;226m"
    CYAN = "\033[38;5;51m"

# ================ CONFIGURAÇÕES PROFISSIONAIS ================
CHUNK_SIZE = 10000  # Linhas por chunk
PROGRESS_UPDATE_INTERVAL = 0.1  # Segundos entre atualizações da barra
MAX_MEMORY_USAGE_MB = 500  # Limite de memória em MB
CANCEL_CHECK_INTERVAL = 1000  # Verificar cancelamento a cada N linhas

@dataclass
class SearchProgress:
    """Classe para controlar o progresso da busca"""
    total_lines: int
    processed_lines: int
    found_results: int
    start_time: float
    is_cancelled: bool = False
    
    @property
    def percentage(self) -> float:
        """Retorna a porcentagem de progresso"""
        if self.total_lines == 0:
            return 0.0
        return (self.processed_lines / self.total_lines) * 100
    
    @property
    def elapsed_time(self) -> float:
        """Retorna o tempo decorrido em segundos"""
        return time.time() - self.start_time
    
    @property
    def estimated_remaining(self) -> float:
        """Estima o tempo restante em segundos"""
        if self.processed_lines == 0:
            return 0.0
        elapsed = self.elapsed_time
        rate = self.processed_lines / elapsed
        remaining_lines = self.total_lines - self.processed_lines
        return remaining_lines / rate if rate > 0 else 0.0

class ProgressBar:
    """Barra de progresso profissional otimizada"""
    
    def __init__(self, total: int, description: str = "Processando"):
        self.total = total
        self.description = description
        self.current = 0
        self.start_time = time.time()
        self.last_update = 0
        self.last_percent = -1  # Evitar atualizações desnecessárias
        
    def update(self, current: int, extra_info: str = ""):
        """Atualiza a barra de progresso de forma otimizada"""
        self.current = current
        current_time = time.time()
        
        # Calcular porcentagem
        percentage = (current / self.total) * 100 if self.total > 0 else 0
        percent_int = int(percentage)
        
        # Atualizar apenas se a porcentagem mudou ou a cada intervalo
        if (current_time - self.last_update < PROGRESS_UPDATE_INTERVAL and 
            percent_int == self.last_percent):
            return
            
        self.last_update = current_time
        self.last_percent = percent_int
        
        # Calcular tempo decorrido e estimativa
        elapsed = current_time - self.start_time
        if current > 0 and elapsed > 0:
            rate = current / elapsed
            eta = (self.total - current) / rate if rate > 0 else 0
        else:
            eta = 0
        
        # Criar barra visual mais compacta
        bar_length = 25
        filled_length = int(bar_length * current // self.total)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        # Formatar tempo de forma mais compacta
        elapsed_str = self._format_time(elapsed)
        eta_str = self._format_time(eta)
        
        # Criar linha de status
        status_line = (f"{Colors.CYAN}{self.description}: {Colors.RESET}[{bar}] "
                      f"{percent_int:3d}% ({current:,}/{self.total:,}) | "
                      f"{elapsed_str} | ETA: {eta_str}")
        
        if extra_info:
            status_line += f" | {extra_info}"
        
        # Limpar linha anterior e imprimir nova linha usando ANSI
        print(f"\r\033[K{status_line}", end='', flush=True)
    
    def finish(self, message: str = ""):
        """Finaliza a barra de progresso"""
        elapsed = time.time() - self.start_time
        elapsed_str = self._format_time(elapsed)
        
        # Limpar a linha da barra e mostrar resultado final
        print(f"\r\033[K{Colors.GREEN}✅ Concluído em {elapsed_str} {message}{Colors.RESET}")
    
    def _format_time(self, seconds: float) -> str:
        """Formata tempo em formato legível e compacto"""
        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.1f}m"
        else:
            hours = seconds / 3600
            return f"{hours:.1f}h"

def get_file_info(file_path: str) -> Tuple[int, float]:
    """
    Obtém informações do arquivo (número de linhas e tamanho)
    Versão otimizada com contagem rápida e barra de progresso eficiente.
    
    Args:
        file_path: Caminho do arquivo
        
    Returns:
        Tuple[int, float]: (número de linhas, tamanho em MB)
    """
    try:
        size_mb = os.path.getsize(file_path) / (1024 * 1024)
        
        # Método otimizado: usar buffer maior e atualizar progresso menos frequentemente
        line_count = 0
        total_bytes = os.path.getsize(file_path)
        bytes_read = 0
        last_percent = -1
        update_interval = max(1, total_bytes // 1000)  # Atualizar a cada 0.1% do arquivo
        
        with open(file_path, 'r', encoding=DEFAULT_ENCODING) as f:
            # Usar buffer maior para melhor performance
            f.read(8192)  # Primeira leitura para inicializar
            while True:
                line = f.readline()
                if not line:
                    break
                line_count += 1
                bytes_read = f.tell()
                
                # Atualizar progresso apenas a cada intervalo
                if bytes_read - f.tell() >= update_interval or bytes_read >= total_bytes:
                    percent = int((bytes_read / total_bytes) * 100) if total_bytes > 0 else 100
                    if percent != last_percent:
                        bar_length = 20
                        filled_length = int(bar_length * percent // 100)
                        bar = '█' * filled_length + '░' * (bar_length - filled_length)
                        print(f"\r{Colors.YELLOW}[📊] Contando: [{bar}] {percent:3d}%{Colors.RESET}", end='', flush=True)
                        last_percent = percent
        
        # Finaliza barra e mostra total
        print(f"\r{Colors.YELLOW}[📊] Total: {line_count:,} linhas{' ' * 30}{Colors.RESET}")
        return line_count, size_mb
        
    except UnicodeDecodeError:
        # Fallback para encoding alternativo
        try:
            print(f"{Colors.YELLOW}[📊] Contando linhas...{Colors.RESET}", end='', flush=True)
            with open(file_path, 'r', encoding=FALLBACK_ENCODING) as f:
                line_count = sum(1 for _ in f)
            print(f"\r{Colors.YELLOW}[📊] Total: {line_count:,} linhas{' ' * 30}{Colors.RESET}")
            return line_count, size_mb
        except Exception as e:
            print(f"{Colors.RED}[💔] Erro ao ler arquivo: {e}{Colors.RESET}")
            return 0, size_mb

def read_file_in_chunks(file_path: str, chunk_size: int = CHUNK_SIZE) -> Generator[List[str], None, None]:
    """
    Lê arquivo em chunks para economizar memória
    
    Args:
        file_path: Caminho do arquivo
        chunk_size: Tamanho do chunk em linhas
        
    Yields:
        List[str]: Chunk de linhas
    """
    try:
        with open(file_path, 'r', encoding=DEFAULT_ENCODING) as file:
            while True:
                chunk = list(itertools.islice(file, chunk_size))
                if not chunk:
                    break
                yield chunk
    except UnicodeDecodeError:
        # Fallback para encoding alternativo
        with open(file_path, 'r', encoding=FALLBACK_ENCODING) as file:
            while True:
                chunk = list(itertools.islice(file, chunk_size))
                if not chunk:
                    break
                yield chunk

def filter_lines(lines: List[str], search_term: str, progress: SearchProgress) -> List[str]:
    """
    Filtra linhas com controle de progresso e cancelamento
    
    Args:
        lines: Lista de linhas para filtrar
        search_term: Termo de busca
        progress: Objeto de progresso
        
    Returns:
        List[str]: Linhas que contêm o termo de busca
    """
    if not search_term or progress.is_cancelled:
        return []
        
    resultados = []
    search_term_lower = search_term.lower()
    
    for i, linha in enumerate(lines):
        if progress.is_cancelled:
            break
            
        if not linha.strip():
            continue
            
        partes = linha.rsplit(':', 2)
        if len(partes) == 3:
            dominio_atual, _, _ = partes
            if search_term_lower in dominio_atual.lower():
                resultados.append(linha)
                progress.found_results += 1
        
        progress.processed_lines += 1
        
        # Verificar cancelamento periodicamente
        if i % CANCEL_CHECK_INTERVAL == 0:
            if progress.is_cancelled:
                break
    
    return resultados

def search_large_file(file_path: str, search_term: str, progress: SearchProgress) -> List[str]:
    """
    Busca em arquivo grande com processamento em chunks
    Exibe apenas mensagem de início e resumo final.
    
    Args:
        file_path: Caminho do arquivo
        search_term: Termo de busca
        progress: Objeto de progresso
        
    Returns:
        List[str]: Resultados encontrados
    """
    resultados = []
    print(f"{Colors.CYAN}[🔍] Processando busca por '{search_term}'... aguarde.{Colors.RESET}")
    start_time = time.time()
    try:
        for chunk in read_file_in_chunks(file_path):
            if progress.is_cancelled:
                break
            chunk_results = filter_lines(chunk, search_term, progress)
            resultados.extend(chunk_results)
        elapsed = time.time() - start_time
        if not progress.is_cancelled:
            print(f"{Colors.GREEN}✅ Busca concluída em {elapsed:.1f}s | Total: {len(resultados)} resultados{Colors.RESET}")
        else:
            print(f"\n{Colors.YELLOW}[⚠️] Busca cancelada pelo usuário{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[💔] Erro durante a busca: {e}{Colors.RESET}")
    return resultados

def print_banner():
    """Exibe o banner do programa"""
    print(f"""
{Colors.GREEN} ==* coded by *== {Colors.PURPLE}

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
      {Colors.GREEN} ==*  {Colors.RED}VL{Colors.RESET} ~ {Colors.RED}villanelle{Colors.RESET} | {Colors.RED}t.me/vi77an{Colors.GREEN} *=={Colors.RESET}
      {Colors.CYAN} === VERSÃO OTIMIZADA === {Colors.RESET}
""")

def get_txt_files_with_size() -> List[Tuple[str, float]]:
    """
    Lista arquivos .txt com tamanho (sem contar linhas)
    
    Returns:
        List[Tuple[str, float]]: Lista de (nome_arquivo, tamanho_mb)
    """
    try:
        txt_files = [
            f for f in os.listdir('.') 
            if os.path.isfile(f) and f.endswith('.txt')
        ]
        
        # Obter apenas tamanho dos arquivos (muito rápido)
        files_with_size = []
        for file in txt_files:
            try:
                size_mb = os.path.getsize(file) / (1024 * 1024)
                files_with_size.append((file, size_mb))
            except OSError:
                files_with_size.append((file, 0.0))
        
        return files_with_size
    except PermissionError:
        print(f"{Colors.RED}[💔] Erro: Sem permissão para listar arquivos no diretório.{Colors.RESET}")
        return []
    except Exception as e:
        print(f"{Colors.RED}[💔] Erro ao listar arquivos: {e}{Colors.RESET}")
        return []

def validate_file_size(file_path: str) -> bool:
    """Valida se o arquivo não é muito grande"""
    try:
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            print(f"{Colors.YELLOW}[⚠️] Arquivo muito grande ({file_size_mb:.1f}MB). Máximo: {MAX_FILE_SIZE_MB}MB{Colors.RESET}")
            print(f"{Colors.CYAN}[💡] Dica: Use a versão profissional para arquivos maiores{Colors.RESET}")
            return False
        return True
    except OSError:
        print(f"{Colors.RED}[💔] Erro ao verificar tamanho do arquivo.{Colors.RESET}")
        return False

def select_file() -> Optional[Tuple[str, int, float]]:
    """
    Permite ao usuário selecionar um arquivo .txt
    Conta linhas apenas do arquivo selecionado.
    
    Returns:
        Optional[Tuple[str, int, float]]: (caminho, linhas, tamanho_mb) ou None
    """
    files_with_size = get_txt_files_with_size()
    
    if not files_with_size:
        print(f"{Colors.RED}[💔] Nenhum arquivo .txt foi encontrado no diretório atual.{Colors.RESET}")
        return None

    print(f"{Colors.PURPLE}[💌] Arquivos disponíveis:{Colors.RESET}")
    for i, (file, size_mb) in enumerate(files_with_size, 1):
        print(f"  [{i}] {file} ({size_mb:.1f}MB)")
    
    print("  [0] Cancelar e sair")

    while True:
        try:
            choice = input(f"{Colors.PURPLE}[*] Selecione o número do arquivo desejado: {Colors.GREEN}").strip()
            
            if not choice:
                print(f"{Colors.RED}[💔] Entrada vazia. Tente novamente.{Colors.RESET}")
                continue
                
            choice = int(choice)
            
            if choice == 0:
                print(f"{Colors.PURPLE}[👋] Operação cancelada. Até mais!{Colors.RESET}")
                return None
            elif 1 <= choice <= len(files_with_size):
                selected_file, size_mb = files_with_size[choice - 1]
                
                print(f"{Colors.GREEN}[✅] Arquivo selecionado: {selected_file}{Colors.RESET}")
                print(f"{Colors.CYAN}[📊] Analisando arquivo...{Colors.RESET}")
                
                # Agora sim, contar as linhas do arquivo selecionado
                line_count, _ = get_file_info(selected_file)
                
                return selected_file, line_count, size_mb
            else:
                print(f"{Colors.RED}[💔] Escolha inválida. Tente novamente.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}[💔] Entrada inválida. Digite um número correspondente a um arquivo.{Colors.RESET}")

def save_results(results: List[str], search_term: str) -> str:
    """Salva os resultados em um arquivo com informações detalhadas"""
    if not results:
        print(f"{Colors.YELLOW}[⚠️] Nenhum resultado para salvar.{Colors.RESET}")
        return ""
    
    # Criar pasta de resultados se não existir
    resultados_dir = "resultados"
    try:
        if not os.path.exists(resultados_dir):
            os.makedirs(resultados_dir)
            print(f"{Colors.CYAN}[📁] Pasta '{resultados_dir}' criada para organizar os resultados{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[💔] Erro ao criar pasta de resultados: {e}{Colors.RESET}")
        resultados_dir = "."  # Fallback para diretório atual
        
    # Criar nome de arquivo seguro
    safe_term = "".join(c for c in search_term if c.isalnum() or c in ('-', '_', '.'))
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(resultados_dir, f"resultado_{safe_term}_{timestamp}.txt")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            # Adicionar cabeçalho compacto com informações
            file.write(f"# URL Hunter - Resultados da Busca\n")
            file.write(f"# Termo buscado: {search_term} | Data/Hora: {time.strftime('%Y-%m-%d %H:%M:%S')} | Total: {len(results)}\n")
            file.write(f"# {'='*60}\n")
            
            # Escrever resultados sem quebras de linha extras
            file.write('\n'.join(results))
        
        print(f"{Colors.PURPLE}[💚] CONFIRA >> {Colors.GREEN}{output_file}{Colors.RESET}")
        print(f"{Colors.GREEN}[📊] {len(results)} resultados salvos{Colors.RESET}")
        return output_file
    except Exception as e:
        print(f"{Colors.RED}[💔] Erro ao salvar arquivo: {e}{Colors.RESET}")
        return ""

def perform_search(file_path: str, line_count: int) -> bool:
    """
    Realiza a pesquisa no arquivo
    
    Args:
        file_path: Caminho do arquivo
        line_count: Número de linhas no arquivo
        
    Returns:
        bool: True se deve continuar, False para sair
    """
    while True:
        search_term = input(f"{Colors.PURPLE}[*] Domínio ou parte do domínio (ex: insta): {Colors.RESET}").strip()
        
        if not search_term:
            print(f"{Colors.YELLOW}[⚠️] Termo de busca não pode estar vazio.{Colors.RESET}")
            continue
            
        print(f"{Colors.BLUE}[🔍] Iniciando busca por '{search_term}'...{Colors.RESET}")
        print(f"{Colors.CYAN}[📊] Arquivo: {file_path} ({line_count:,} linhas){Colors.RESET}")
        
        # Criar objeto de progresso
        progress = SearchProgress(
            total_lines=line_count,
            processed_lines=0,
            found_results=0,
            start_time=time.time()
        )
        
        # Realizar busca
        results = search_large_file(file_path, search_term, progress)

        if results and not progress.is_cancelled:
            save_results(results, search_term)
            return True
        elif progress.is_cancelled:
            print(f"{Colors.YELLOW}[⚠️] Busca cancelada.{Colors.RESET}")
            return False
        else:
            print(f"{Colors.RED}[!] Vixe, não encontramos nada com '{search_term}'.{Colors.RESET}")
            retry = input(f"{Colors.PURPLE}[?] Tentar novamente com outro termo? (s/n): {Colors.RESET}").strip().lower()
            if retry != 's':
                print(f"\n{Colors.PURPLE}[👋] Até mais!{Colors.RESET}")
                return False

def ask_continue() -> bool:
    """Pergunta se o usuário quer continuar"""
    while True:
        response = input(f"{Colors.PURPLE}[?] Continuar? (s/n): {Colors.RESET}").strip().lower()
        if response in ('s', 'sim', 'y', 'yes'):
            return True
        elif response in ('n', 'não', 'nao', 'no'):
            print(f"{Colors.PURPLE}[👋] Ok, até a próxima!{Colors.RESET}")
            return False
        else:
            print(f"{Colors.RED}[!] Por favor, digite 's' para continuar ou 'n' para encerrar.{Colors.RESET}")

def main():
    """Função principal do programa"""
    try:
        print_banner()
        print('+-+-+-+-+-++-+-+-+-+-++-+-+-+')
        print(f'.:|| {Colors.PURPLE}URL:LOG:PASS HUNTER {Colors.RESET}||:.')
        print('+-+-+-+-+-++-+-+-+-+-++-+-+-+\n')

        while True:
            file_selection = select_file()
            if file_selection is None:
                break

            file_path, line_count, size_mb = file_selection
            
            # Mostrar informações do arquivo
            print(f"{Colors.CYAN}[📋] Informações do arquivo:{Colors.RESET}")
            print(f"  📁 Arquivo: {file_path}")
            print(f"  📊 Tamanho: {size_mb:.1f}MB")
            print(f"  📝 Linhas: {line_count:,}")
            print(f"  ⚡ Velocidade estimada: {line_count/1000:.0f}k linhas/segundo")
            print()

            if not perform_search(file_path, line_count):
                break

            if not ask_continue():
                break
                
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[⚠️] Programa interrompido pelo usuário.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[💔] Erro inesperado: {e}{Colors.RESET}")
    finally:
        print(f"{Colors.GREEN}[👋] Programa finalizado.{Colors.RESET}")

if __name__ == "__main__":
    main() 