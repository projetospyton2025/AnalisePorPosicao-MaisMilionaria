"""
Model para armazenamento de resultados da Dupla Sena
"""
import sqlite3
import json
from typing import List, Dict, Optional
from config import Config


class DuplaSenaModel:
    """Model para gerenciar resultados da Dupla Sena"""
    
    def __init__(self, db_path: str = None):
        """
        Inicializa o model
        
        Args:
            db_path: Caminho para o banco de dados
        """
        self.db_path = db_path or Config.DATABASE_PATH_DUPLASENA
        self._criar_tabela()
    
    def _criar_tabela(self):
        """Cria a tabela de resultados se não existir"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resultados_duplasena (
                numero INTEGER PRIMARY KEY,
                data_apuracao TEXT NOT NULL,
                acumulado BOOLEAN NOT NULL,
                lista_dezenas_sorteio1 TEXT NOT NULL,
                lista_dezenas_sorteio2 TEXT NOT NULL,
                dezenas_ordem_sorteio1 TEXT NOT NULL,
                dezenas_ordem_sorteio2 TEXT NOT NULL,
                valor_arrecadado REAL,
                valor_acumulado_proximo_concurso REAL,
                valor_estimado_proximo_concurso REAL,
                lista_rateio_premio TEXT,
                lista_municipio_uf_ganhadores TEXT,
                observacao TEXT,
                ultimo_concurso BOOLEAN
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def inserir_resultado(self, resultado: Dict) -> bool:
        """
        Insere ou atualiza um resultado
        
        Args:
            resultado: Dicionário com dados do resultado
            
        Returns:
            True se inserido com sucesso
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Converter listas para JSON
            # Dupla Sena tem dois sorteios independentes
            lista_dezenas_1 = json.dumps(resultado.get('listaDezenasSorteio1', []))
            lista_dezenas_2 = json.dumps(resultado.get('listaDezenasSorteio2', []))
            dezenas_ordem_1 = json.dumps(resultado.get('dezenasSorteio1OrdemSorteio', []))
            dezenas_ordem_2 = json.dumps(resultado.get('dezenasSorteio2OrdemSorteio', []))
            lista_rateio = json.dumps(resultado.get('listaRateioPremio', []))
            lista_municipios = json.dumps(resultado.get('listaMunicipioUFGanhadores', []))
            
            cursor.execute('''
                INSERT OR REPLACE INTO resultados_duplasena (
                    numero, data_apuracao, acumulado, lista_dezenas_sorteio1,
                    lista_dezenas_sorteio2, dezenas_ordem_sorteio1, dezenas_ordem_sorteio2,
                    valor_arrecadado, valor_acumulado_proximo_concurso,
                    valor_estimado_proximo_concurso, lista_rateio_premio,
                    lista_municipio_uf_ganhadores, observacao, ultimo_concurso
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                resultado.get('numero'),
                resultado.get('dataApuracao'),
                resultado.get('acumulado', False),
                lista_dezenas_1,
                lista_dezenas_2,
                dezenas_ordem_1,
                dezenas_ordem_2,
                resultado.get('valorArrecadado'),
                resultado.get('valorAcumuladoProximoConcurso'),
                resultado.get('valorEstimadoProximoConcurso'),
                lista_rateio,
                lista_municipios,
                resultado.get('observacao'),
                resultado.get('ultimoConcurso', False)
            ))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"Erro ao inserir resultado Dupla Sena: {e}")
            return False
    
    def buscar_resultado(self, numero: int) -> Optional[Dict]:
        """
        Busca um resultado específico
        
        Args:
            numero: Número do concurso
            
        Returns:
            Dicionário com dados do resultado ou None
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM resultados_duplasena WHERE numero = ?', (numero,))
        row = cursor.fetchone()
        conn.close()
        
        if not row:
            return None
        
        return self._row_to_dict(row)
    
    def buscar_ultimo_resultado(self) -> Optional[Dict]:
        """
        Busca o último resultado registrado
        
        Returns:
            Dicionário com dados do último resultado ou None
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM resultados_duplasena ORDER BY numero DESC LIMIT 1')
        row = cursor.fetchone()
        conn.close()
        
        if not row:
            return None
        
        return self._row_to_dict(row)
    
    def listar_resultados(self, limite: int = 100) -> List[Dict]:
        """
        Lista resultados ordenados por número
        
        Args:
            limite: Número máximo de resultados
            
        Returns:
            Lista de dicionários com resultados
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM resultados_duplasena ORDER BY numero DESC LIMIT ?', (limite,))
        rows = cursor.fetchall()
        conn.close()
        
        return [self._row_to_dict(row) for row in rows]
    
    def contar_resultados(self) -> int:
        """
        Conta total de resultados no banco
        
        Returns:
            Número total de resultados
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM resultados_duplasena')
        count = cursor.fetchone()[0]
        conn.close()
        
        return count
    
    def _row_to_dict(self, row) -> Dict:
        """
        Converte uma linha do banco para dicionário
        
        Args:
            row: Tupla com dados da linha
            
        Returns:
            Dicionário com dados do resultado
        """
        return {
            'numero': row[0],
            'dataApuracao': row[1],
            'acumulado': bool(row[2]),
            'listaDezenasSorteio1': json.loads(row[3]),
            'listaDezenasSorteio2': json.loads(row[4]),
            'dezenasSorteio1OrdemSorteio': json.loads(row[5]),
            'dezenasSorteio2OrdemSorteio': json.loads(row[6]),
            'valorArrecadado': row[7],
            'valorAcumuladoProximoConcurso': row[8],
            'valorEstimadoProximoConcurso': row[9],
            'listaRateioPremio': json.loads(row[10]) if row[10] else [],
            'listaMunicipioUFGanhadores': json.loads(row[11]) if row[11] else [],
            'observacao': row[12],
            'ultimoConcurso': bool(row[13])
        }
