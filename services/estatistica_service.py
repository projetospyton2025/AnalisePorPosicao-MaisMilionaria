"""
Serviço de estatísticas para números e trevos da +Milionária
"""
from typing import Dict, List
from collections import Counter
from models import ResultadoModel
from config import Config


class EstatisticaService:
    """Serviço para cálculo de estatísticas de números e trevos"""
    
    def __init__(self):
        """Inicializa o serviço"""
        self.model = ResultadoModel()
    
    def calcular_estatisticas_completas(self) -> Dict:
        """
        Calcula estatísticas completas de números e trevos
        
        Returns:
            Dicionário com estatísticas de números e trevos
        """
        return {
            'numeros': self.calcular_estatisticas_numeros(),
            'trevos': self.calcular_estatisticas_trevos()
        }
    
    # ========== ESTATÍSTICAS DE NÚMEROS ==========
    
    def calcular_estatisticas_numeros(self) -> Dict:
        """
        Calcula todas as estatísticas dos números
        
        Returns:
            Dicionário com estatísticas dos números
        """
        return {
            'frequencia': self.calcular_frequencia_numeros(),
            'atrasos': self.calcular_atrasos_numeros(),
            'pares_impares': self.calcular_pares_impares_numeros(),
            'por_faixa': self.calcular_por_faixa_numeros(),
            'por_posicao': self.calcular_por_posicao_sorteio()
        }
    
    def calcular_frequencia_numeros(self) -> List[Dict]:
        """
        Calcula a frequência de cada número
        
        Returns:
            Lista com frequência de cada número
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        # Contar frequência
        contador = Counter()
        for resultado in resultados:
            for dezena in resultado['listaDezenas']:
                contador[int(dezena)] += 1
        
        # Calcular total de sorteios
        total_sorteios = len(resultados) * Config.NUMEROS_SORTEADOS
        
        # Criar lista de frequências
        frequencias = []
        for numero in range(Config.MIN_NUMEROS, Config.MAX_NUMEROS + 1):
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
    
    def calcular_atrasos_numeros(self) -> List[Dict]:
        """
        Calcula o atraso de cada número (concursos sem aparecer)
        
        Returns:
            Lista com atraso de cada número
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        if not resultados:
            return []
        
        # Calcular atraso
        atrasos = {}
        for numero in range(Config.MIN_NUMEROS, Config.MAX_NUMEROS + 1):
            atrasos[numero] = 0
        
        # Percorrer resultados do mais recente ao mais antigo
        for resultado in resultados:
            dezenas = [int(d) for d in resultado['listaDezenas']]
            
            for numero in range(Config.MIN_NUMEROS, Config.MAX_NUMEROS + 1):
                if numero in dezenas:
                    break
                atrasos[numero] += 1
        
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
    
    def calcular_pares_impares_numeros(self) -> Dict:
        """
        Calcula distribuição de números pares e ímpares
        
        Returns:
            Dicionário com contagem de pares e ímpares
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        pares = 0
        impares = 0
        
        for resultado in resultados:
            for dezena in resultado['listaDezenas']:
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
    
    def calcular_por_faixa_numeros(self) -> List[Dict]:
        """
        Calcula distribuição por faixas (01-10, 11-20, etc)
        
        Returns:
            Lista com contagem por faixa
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        faixas = {
            '01-10': 0,
            '11-20': 0,
            '21-30': 0,
            '31-40': 0,
            '41-50': 0
        }
        
        for resultado in resultados:
            for dezena in resultado['listaDezenas']:
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
    
    def calcular_por_posicao_sorteio(self) -> Dict:
        """
        Calcula estatísticas por posição de sorteio
        
        Returns:
            Dicionário com dados por posição
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        posicoes = {i: [] for i in range(Config.NUMEROS_SORTEADOS)}
        
        for resultado in resultados:
            dezenas = sorted([int(d) for d in resultado['listaDezenas']])
            for i, numero in enumerate(dezenas):
                if i < Config.NUMEROS_SORTEADOS:
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
    
    # ========== ESTATÍSTICAS DE TREVOS ==========
    
    def calcular_estatisticas_trevos(self) -> Dict:
        """
        Calcula todas as estatísticas dos trevos
        
        Returns:
            Dicionário com estatísticas dos trevos
        """
        return {
            'frequencia': self.calcular_frequencia_trevos(),
            'atrasos': self.calcular_atrasos_trevos(),
            'pares_impares': self.calcular_pares_impares_trevos(),
            'combinacoes': self.calcular_combinacoes_trevos(),
            'quentes_frios': self.calcular_trevos_quentes_frios()
        }
    
    def calcular_frequencia_trevos(self) -> List[Dict]:
        """
        Calcula a frequência de cada trevo
        
        Returns:
            Lista com frequência de cada trevo
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        # Contar frequência
        contador = Counter()
        for resultado in resultados:
            for trevo in resultado['trevosSorteados']:
                contador[int(trevo)] += 1
        
        # Calcular total de sorteios
        total_sorteios = len(resultados) * Config.TREVOS_SORTEADOS
        
        # Criar lista de frequências
        frequencias = []
        for trevo in range(Config.MIN_TREVOS, Config.MAX_TREVOS + 1):
            vezes = contador.get(trevo, 0)
            percentual = (vezes / total_sorteios * 100) if total_sorteios > 0 else 0
            
            frequencias.append({
                'trevo': trevo,
                'vezes': vezes,
                'percentual': round(percentual, 2)
            })
        
        # Ordenar por frequência
        frequencias.sort(key=lambda x: x['vezes'], reverse=True)
        
        return frequencias
    
    def calcular_atrasos_trevos(self) -> List[Dict]:
        """
        Calcula o atraso de cada trevo (concursos sem aparecer)
        
        Returns:
            Lista com atraso de cada trevo
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        if not resultados:
            return []
        
        # Calcular atraso
        atrasos = {}
        for trevo in range(Config.MIN_TREVOS, Config.MAX_TREVOS + 1):
            atrasos[trevo] = 0
        
        # Percorrer resultados do mais recente ao mais antigo
        for resultado in resultados:
            trevos_sorteados = [int(t) for t in resultado['trevosSorteados']]
            
            for trevo in range(Config.MIN_TREVOS, Config.MAX_TREVOS + 1):
                if trevo in trevos_sorteados:
                    break
                atrasos[trevo] += 1
        
        # Criar lista de atrasos
        lista_atrasos = []
        for trevo, atraso in atrasos.items():
            lista_atrasos.append({
                'trevo': trevo,
                'atraso': atraso
            })
        
        # Ordenar por atraso
        lista_atrasos.sort(key=lambda x: x['atraso'], reverse=True)
        
        return lista_atrasos
    
    def calcular_pares_impares_trevos(self) -> Dict:
        """
        Calcula distribuição de trevos pares e ímpares
        
        Returns:
            Dicionário com contagem de pares e ímpares
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        pares = 0
        impares = 0
        
        for resultado in resultados:
            for trevo in resultado['trevosSorteados']:
                numero = int(trevo)
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
    
    def calcular_combinacoes_trevos(self) -> List[Dict]:
        """
        Calcula as combinações de trevos mais comuns
        
        Returns:
            Lista com combinações mais frequentes
        """
        resultados = self.model.listar_resultados(limite=10000)
        
        # Contar combinações
        contador = Counter()
        for resultado in resultados:
            trevos = tuple(sorted([int(t) for t in resultado['trevosSorteados']]))
            contador[trevos] += 1
        
        # Criar lista de combinações
        combinacoes = []
        for trevos, vezes in contador.most_common(10):
            combinacoes.append({
                'trevos': list(trevos),
                'vezes': vezes
            })
        
        return combinacoes
    
    def calcular_trevos_quentes_frios(self) -> Dict:
        """
        Identifica trevos quentes (mais frequentes) e frios (menos frequentes)
        
        Returns:
            Dicionário com trevos quentes e frios
        """
        frequencias = self.calcular_frequencia_trevos()
        
        # Ordenar por frequência
        ordenados = sorted(frequencias, key=lambda x: x['vezes'], reverse=True)
        
        return {
            'quentes': ordenados[:3],  # Top 3
            'frios': ordenados[-3:]     # Bottom 3
        }
