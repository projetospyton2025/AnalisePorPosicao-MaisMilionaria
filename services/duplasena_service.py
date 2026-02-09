"""
Serviço para geração de palpites da Dupla Sena
"""
import random
from typing import Dict, List
from services.estatistica_duplasena_service import EstatisticaDuplaSenaService
from models import DuplaSenaModel
from config import Config


class DuplaSenaService:
    """Serviço para geração de palpites inteligentes da Dupla Sena"""
    
    def __init__(self):
        """Inicializa o serviço"""
        self.estatistica = EstatisticaDuplaSenaService()
        self.model = DuplaSenaModel()
    
    def gerar_palpite(
        self,
        estrategia: str = 'equilibrada',
        quantidade_numeros: int = 6,
        quantidade_jogos: int = 1
    ) -> Dict:
        """
        Gera palpites baseados em estratégia
        
        Args:
            estrategia: Estratégia a ser usada
            quantidade_numeros: Quantidade de números (6-15)
            quantidade_jogos: Quantidade de jogos a gerar
            
        Returns:
            Dicionário com palpites gerados
        """
        # Validar parâmetros
        quantidade_numeros = max(Config.DUPLASENA_MIN_JOGO, min(quantidade_numeros, Config.DUPLASENA_MAX_JOGO))
        
        jogos = []
        
        for _ in range(quantidade_jogos):
            # Gerar números baseado na estratégia
            if estrategia == 'agressiva':
                numeros = self._gerar_numeros_agressivos(quantidade_numeros)
            elif estrategia == 'conservadora':
                numeros = self._gerar_numeros_conservadores(quantidade_numeros)
            elif estrategia == 'atrasados':
                numeros = self._gerar_numeros_atrasados(quantidade_numeros)
            elif estrategia == 'por_faixa':
                numeros = self._gerar_numeros_por_faixa(quantidade_numeros)
            else:  # equilibrada ou mista
                numeros = self._gerar_numeros_equilibrados(quantidade_numeros)
            
            jogos.append({
                'numeros': sorted(numeros)
            })
        
        return {
            'sucesso': True,
            'estrategia': estrategia,
            'jogos': jogos
        }
    
    # ========== GERAÇÃO DE NÚMEROS ==========
    
    def _gerar_numeros_equilibrados(self, quantidade: int) -> List[int]:
        """Gera números com mix de frequentes e atrasados de ambos sorteios"""
        # Usar estatísticas gerais (média dos dois sorteios)
        freq1 = self.estatistica.calcular_frequencia_numeros(1)
        freq2 = self.estatistica.calcular_frequencia_numeros(2)
        atr1 = self.estatistica.calcular_atrasos_numeros(1)
        atr2 = self.estatistica.calcular_atrasos_numeros(2)
        
        # Combinar estatísticas dos dois sorteios
        frequentes1 = [f['numero'] for f in freq1[:10]]
        frequentes2 = [f['numero'] for f in freq2[:10]]
        atrasados1 = [a['numero'] for a in atr1[:10]]
        atrasados2 = [a['numero'] for a in atr2[:10]]
        
        # Pool combinado
        frequentes = list(set(frequentes1 + frequentes2))
        atrasados = list(set(atrasados1 + atrasados2))
        
        metade = quantidade // 2
        
        numeros = set()
        if frequentes:
            numeros.update(random.sample(frequentes, min(metade, len(frequentes))))
        if atrasados:
            numeros.update(random.sample(atrasados, min(quantidade - len(numeros), len(atrasados))))
        
        # Completar se necessário
        while len(numeros) < quantidade:
            numeros.add(random.randint(Config.DUPLASENA_MIN_NUMEROS, Config.DUPLASENA_MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _gerar_numeros_agressivos(self, quantidade: int) -> List[int]:
        """Gera números mais frequentes de ambos sorteios"""
        freq1 = self.estatistica.calcular_frequencia_numeros(1)
        freq2 = self.estatistica.calcular_frequencia_numeros(2)
        
        # Combinar top números de ambos sorteios
        frequentes1 = [f['numero'] for f in freq1[:15]]
        frequentes2 = [f['numero'] for f in freq2[:15]]
        pool = list(set(frequentes1 + frequentes2))
        
        if len(pool) < quantidade:
            # Adicionar mais números se necessário
            todos = list(range(Config.DUPLASENA_MIN_NUMEROS, Config.DUPLASENA_MAX_NUMEROS + 1))
            pool.extend([n for n in todos if n not in pool])
        
        return random.sample(pool, min(quantidade, len(pool)))
    
    def _gerar_numeros_conservadores(self, quantidade: int) -> List[int]:
        """Gera números mais atrasados de ambos sorteios"""
        atr1 = self.estatistica.calcular_atrasos_numeros(1)
        atr2 = self.estatistica.calcular_atrasos_numeros(2)
        
        # Combinar números atrasados de ambos sorteios
        atrasados1 = [a['numero'] for a in atr1[:15]]
        atrasados2 = [a['numero'] for a in atr2[:15]]
        pool = list(set(atrasados1 + atrasados2))
        
        if len(pool) < quantidade:
            # Adicionar mais números se necessário
            todos = list(range(Config.DUPLASENA_MIN_NUMEROS, Config.DUPLASENA_MAX_NUMEROS + 1))
            pool.extend([n for n in todos if n not in pool])
        
        return random.sample(pool, min(quantidade, len(pool)))
    
    def _gerar_numeros_atrasados(self, quantidade: int) -> List[int]:
        """Gera números com maior atraso"""
        return self._gerar_numeros_conservadores(quantidade)
    
    def _gerar_numeros_por_faixa(self, quantidade: int) -> List[int]:
        """Distribui números por faixas"""
        faixas = [
            (1, 10),
            (11, 20),
            (21, 30),
            (31, 40),
            (41, 50)
        ]
        
        numeros = set()
        por_faixa = quantidade // len(faixas)
        resto = quantidade % len(faixas)
        
        for i, (inicio, fim) in enumerate(faixas):
            qtd = por_faixa + (1 if i < resto else 0)
            for _ in range(qtd):
                if len(numeros) < quantidade:
                    numero = random.randint(inicio, fim)
                    numeros.add(numero)
        
        # Completar se necessário
        while len(numeros) < quantidade:
            numeros.add(random.randint(Config.DUPLASENA_MIN_NUMEROS, Config.DUPLASENA_MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def conferir_jogo(self, numeros: List[int], concurso: int) -> Dict:
        """
        Confere um jogo contra um resultado (ambos sorteios)
        
        Args:
            numeros: Números apostados
            concurso: Número do concurso
            
        Returns:
            Dicionário com resultado da conferência
        """
        resultado = self.model.buscar_resultado(concurso)
        
        if not resultado:
            return {
                'sucesso': False,
                'mensagem': 'Concurso não encontrado'
            }
        
        # Converter para inteiros
        numeros_sorteio1 = [int(n) for n in resultado['listaDezenasSorteio1']]
        numeros_sorteio2 = [int(n) for n in resultado['listaDezenasSorteio2']]
        
        # Contar acertos em cada sorteio
        acertos_sorteio1 = len(set(numeros) & set(numeros_sorteio1))
        acertos_sorteio2 = len(set(numeros) & set(numeros_sorteio2))
        
        # Determinar faixas de premiação
        faixa_sorteio1 = self._determinar_faixa(acertos_sorteio1)
        faixa_sorteio2 = self._determinar_faixa(acertos_sorteio2)
        
        return {
            'sucesso': True,
            'concurso': concurso,
            'sorteio1': {
                'acertos': acertos_sorteio1,
                'faixa': faixa_sorteio1,
                'premiado': faixa_sorteio1 > 0,
                'numeros_sorteados': numeros_sorteio1
            },
            'sorteio2': {
                'acertos': acertos_sorteio2,
                'faixa': faixa_sorteio2,
                'premiado': faixa_sorteio2 > 0,
                'numeros_sorteados': numeros_sorteio2
            }
        }
    
    def _determinar_faixa(self, acertos: int) -> int:
        """
        Determina a faixa de premiação baseada nos acertos
        Dupla Sena tem 6 faixas baseadas apenas em acertos de números
        
        Args:
            acertos: Quantidade de números acertados
            
        Returns:
            Número da faixa (0 se não premiado)
        """
        # Faixa 1: 6 acertos (sena)
        if acertos == 6:
            return 1
        
        # Faixa 2: 5 acertos (quina)
        if acertos == 5:
            return 2
        
        # Faixa 3: 4 acertos (quadra)
        if acertos == 4:
            return 3
        
        # Faixa 4: 3 acertos (terno)
        if acertos == 3:
            return 4
        
        return 0  # Não premiado
