"""
Serviço para integração com a API da Caixa
"""
import requests
from typing import Dict, Optional
from config import Config
from models import ResultadoModel


class ApiCaixaService:
    """Serviço para buscar dados da API oficial da Caixa"""
    
    def __init__(self):
        """Inicializa o serviço"""
        self.api_url = Config.API_MAISMILIONARIA_URL
        self.model = ResultadoModel()
    
    def buscar_ultimo_concurso(self) -> Optional[Dict]:
        """
        Busca o último concurso da API
        
        Returns:
            Dicionário com dados do último concurso ou None
        """
        try:
            response = requests.get(self.api_url, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Erro ao buscar último concurso: {e}")
            return None
    
    def buscar_concurso(self, numero: int) -> Optional[Dict]:
        """
        Busca um concurso específico da API
        
        Args:
            numero: Número do concurso
            
        Returns:
            Dicionário com dados do concurso ou None
        """
        try:
            url = f"{self.api_url}/{numero}"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Erro ao buscar concurso {numero}: {e}")
            return None
    
    def atualizar_base_dados(self, concurso_inicial: int = 1) -> Dict:
        """
        Atualiza a base de dados com resultados da API
        
        Args:
            concurso_inicial: Número do concurso inicial para atualização
            
        Returns:
            Dicionário com estatísticas da atualização
        """
        inseridos = 0
        erros = 0
        
        # Buscar último concurso para saber até onde atualizar
        ultimo = self.buscar_ultimo_concurso()
        if not ultimo:
            return {
                'sucesso': False,
                'mensagem': 'Não foi possível buscar o último concurso',
                'inseridos': 0,
                'erros': 0
            }
        
        numero_final = ultimo.get('numero', 1)
        
        # Atualizar concursos
        for numero in range(concurso_inicial, numero_final + 1):
            resultado = self.buscar_concurso(numero)
            
            if resultado:
                if self.model.inserir_resultado(resultado):
                    inseridos += 1
                else:
                    erros += 1
            else:
                erros += 1
        
        return {
            'sucesso': True,
            'mensagem': f'Atualização concluída: {inseridos} concursos inseridos',
            'inseridos': inseridos,
            'erros': erros,
            'ultimo_concurso': numero_final
        }
    
    def atualizar_ultimos_concursos(self, quantidade: int = 10) -> Dict:
        """
        Atualiza apenas os últimos N concursos
        
        Args:
            quantidade: Quantidade de concursos a atualizar
            
        Returns:
            Dicionário com estatísticas da atualização
        """
        ultimo = self.buscar_ultimo_concurso()
        if not ultimo:
            return {
                'sucesso': False,
                'mensagem': 'Não foi possível buscar o último concurso',
                'inseridos': 0
            }
        
        numero_final = ultimo.get('numero', 1)
        numero_inicial = max(1, numero_final - quantidade + 1)
        
        return self.atualizar_base_dados(numero_inicial)
