"""
Serviço de estatísticas para Dupla Sena
"""
from typing import Dict, List
from collections import Counter
from models import DuplaSenaModel
from config import Config


class EstatisticaDuplaSenaService:
    """Serviço para cálculo de estatísticas da Dupla Sena"""
    
    def __init__(self):
        """Inicializa o serviço"""
        self.model = DuplaSenaModel()
    
    def calcular_estatisticas_completas(self) -> Dict:
        """
        Calcula estatísticas completas dos dois sorteios
        
        Returns:
            Dicionário com estatísticas dos dois sorteios
        """
        return {
            'sorteio1': self.calcular_estatisticas_sorteio(1),
            'sorteio2': self.calcular_estatisticas_sorteio(2),
            'geral': self.calcular_estatisticas_gerais()
        }
    
    def calcular_estatisticas_sorteio(self, sorteio: int) -> Dict:
        """
        Calcula estatísticas de um sorteio específico
        
        Args:
            sorteio: Número do sorteio (1 ou 2)
            
        Returns:
            Dicionário com estatísticas do sorteio
        """
        return {
            'frequencia': self.calcular_frequencia_numeros(sorteio),
            'atrasos': self.calcular_atrasos_numeros(sorteio),
            'pares_impares': self.calcular_pares_impares_numeros(sorteio),
            'por_faixa': self.calcular_por_faixa_numeros(sorteio),
            'por_posicao': self.calcular_por_posicao_sorteio(sorteio)
        }
    
    def calcular_frequencia_numeros(self, sorteio: int) -> List[Dict]:
        """
        Calcula a frequência de cada número em um sorteio
        
        Args:
            sorteio: Número do sorteio (1 ou 2)
            
        Returns:
            Lista com frequência de cada número
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        # Determinar campo correto
        campo = 'listaDezenasSorteio1' if sorteio == 1 else 'listaDezenasSorteio2'
        
        # Contar frequência
        contador = Counter()
        for resultado in resultados:
            for dezena in resultado[campo]:
                contador[int(dezena)] += 1
        
        # Calcular total de sorteios
        total_sorteios = len(resultados) * Config.DUPLASENA_NUMEROS_SORTEADOS
        
        # Criar lista de frequências
        frequencias = []
        for numero in range(Config.DUPLASENA_MIN_NUMEROS, Config.DUPLASENA_MAX_NUMEROS + 1):
            vezes = contador.get(numero, 0)
            percentual = (vezes / total_sorteios * 100) if total_sorteios > 0 else 0
            
            frequencias.append({
                'numero': numero,
                'vezes': vezes,
                'percentual': round(percentual, 2)
            })
        
        # Ordenar por frequência
        frequencias.sort(key=lambda x: x['vezes'], reverse=True)
        
        return frequencias
    
    def calcular_atrasos_numeros(self, sorteio: int) -> List[Dict]:
        """
        Calcula o atraso de cada número em um sorteio
        
        Args:
            sorteio: Número do sorteio (1 ou 2)
            
        Returns:
            Lista com atraso de cada número
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        if not resultados:
            return []
        
        # Determinar campo correto
        campo = 'listaDezenasSorteio1' if sorteio == 1 else 'listaDezenasSorteio2'
        
        # Calcular atraso
        atrasos = {}
        for numero in range(Config.DUPLASENA_MIN_NUMEROS, Config.DUPLASENA_MAX_NUMEROS + 1):
            for i, resultado in enumerate(resultados):
                dezenas = [int(d) for d in resultado[campo]]
                if numero in dezenas:
                    atrasos[numero] = i
                    break
            else:
                atrasos[numero] = len(resultados)
        
        # Criar lista de atrasos
        lista_atrasos = []
        for numero, atraso in atrasos.items():
            lista_atrasos.append({
                'numero': numero,
                'atraso': atraso
            })
        
        # Ordenar por atraso
        lista_atrasos.sort(key=lambda x: x['atraso'], reverse=True)
        
        return lista_atrasos
    
    def calcular_pares_impares_numeros(self, sorteio: int) -> Dict:
        """
        Calcula distribuição de números pares e ímpares
        
        Args:
            sorteio: Número do sorteio (1 ou 2)
            
        Returns:
            Dicionário com contagem de pares e ímpares
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        # Determinar campo correto
        campo = 'listaDezenasSorteio1' if sorteio == 1 else 'listaDezenasSorteio2'
        
        pares = 0
        impares = 0
        
        for resultado in resultados:
            for dezena in resultado[campo]:
                numero = int(dezena)
                if numero % 2 == 0:
                    pares += 1
                else:
                    impares += 1
        
        total = pares + impares
        
        return {
            'pares': pares,
            'impares': impares,
            'percentual_pares': round((pares / total * 100) if total > 0 else 0, 2),
            'percentual_impares': round((impares / total * 100) if total > 0 else 0, 2)
        }
    
    def calcular_por_faixa_numeros(self, sorteio: int) -> List[Dict]:
        """
        Calcula distribuição por faixas (01-10, 11-20, etc)
        
        Args:
            sorteio: Número do sorteio (1 ou 2)
            
        Returns:
            Lista com contagem por faixa
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        # Determinar campo correto
        campo = 'listaDezenasSorteio1' if sorteio == 1 else 'listaDezenasSorteio2'
        
        faixas = {
            '01-10': 0,
            '11-20': 0,
            '21-30': 0,
            '31-40': 0,
            '41-50': 0
        }
        
        for resultado in resultados:
            for dezena in resultado[campo]:
                numero = int(dezena)
                if 1 <= numero <= 10:
                    faixas['01-10'] += 1
                elif 11 <= numero <= 20:
                    faixas['11-20'] += 1
                elif 21 <= numero <= 30:
                    faixas['21-30'] += 1
                elif 31 <= numero <= 40:
                    faixas['31-40'] += 1
                elif 41 <= numero <= 50:
                    faixas['41-50'] += 1
        
        return [{'faixa': k, 'quantidade': v} for k, v in faixas.items()]
    
    def calcular_por_posicao_sorteio(self, sorteio: int) -> Dict:
        """
        Calcula estatísticas por posição de sorteio
        
        Args:
            sorteio: Número do sorteio (1 ou 2)
            
        Returns:
            Dicionário com dados por posição
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        # Determinar campo correto
        campo = 'listaDezenasSorteio1' if sorteio == 1 else 'listaDezenasSorteio2'
        
        posicoes = {i: [] for i in range(Config.DUPLASENA_NUMEROS_SORTEADOS)}
        
        for resultado in resultados:
            dezenas = sorted([int(d) for d in resultado[campo]])
            for i, numero in enumerate(dezenas):
                if i < Config.DUPLASENA_NUMEROS_SORTEADOS:
                    posicoes[i].append(numero)
        
        estatisticas = {}
        for posicao, numeros in posicoes.items():
            if numeros:
                estatisticas[f'posicao_{posicao + 1}'] = {
                    'media': round(sum(numeros) / len(numeros), 2),
                    'minimo': min(numeros),
                    'maximo': max(numeros)
                }
        
        return estatisticas
    
    def calcular_estatisticas_gerais(self) -> Dict:
        """
        Calcula estatísticas gerais (ambos sorteios combinados)
        
        Returns:
            Dicionário com estatísticas gerais
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        # Números que aparecem em ambos os sorteios
        numeros_duplicados = []
        for resultado in resultados:
            dezenas1 = set([int(d) for d in resultado['listaDezenasSorteio1']])
            dezenas2 = set([int(d) for d in resultado['listaDezenasSorteio2']])
            duplicados = dezenas1.intersection(dezenas2)
            numeros_duplicados.append(len(duplicados))
        
        # Calcular frequência de números duplicados
        media_duplicados = sum(numeros_duplicados) / len(numeros_duplicados) if numeros_duplicados else 0
        
        # Números mais comuns em ambos sorteios
        contador_geral = Counter()
        for resultado in resultados:
            for dezena in resultado['listaDezenasSorteio1']:
                contador_geral[int(dezena)] += 1
            for dezena in resultado['listaDezenasSorteio2']:
                contador_geral[int(dezena)] += 1
        
        mais_comuns = [{'numero': num, 'vezes': vezes} for num, vezes in contador_geral.most_common(10)]
        
        return {
            'media_numeros_duplicados': round(media_duplicados, 2),
            'numeros_mais_comuns_geral': mais_comuns,
            'total_concursos': len(resultados)
        }
