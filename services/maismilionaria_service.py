"""
Serviço para geração de palpites da +Milionária
"""
import random
from typing import Dict, List
from services.estatistica_service import EstatisticaService
from models import ResultadoModel
from config import Config


class MaisMilionariaService:
    """Serviço para geração de palpites inteligentes"""
    
    def __init__(self):
        """Inicializa o serviço"""
        self.estatistica = EstatisticaService()
        self.model = ResultadoModel()
    
    def gerar_palpite(
        self,
        estrategia: str = 'equilibrada',
        quantidade_numeros: int = 6,
        quantidade_trevos: int = 2,
        quantidade_jogos: int = 1
    ) -> Dict:
        """
        Gera palpites baseados em estratégia
        
        Args:
            estrategia: Estratégia a ser usada
            quantidade_numeros: Quantidade de números (6-12)
            quantidade_trevos: Quantidade de trevos (2-6)
            quantidade_jogos: Quantidade de jogos a gerar
            
        Returns:
            Dicionário com palpites gerados
        """
        # Validar parâmetros
        quantidade_numeros = max(Config.MIN_JOGO, min(quantidade_numeros, Config.MAX_JOGO))
        quantidade_trevos = max(Config.MIN_TREVOS_JOGO, min(quantidade_trevos, Config.MAX_TREVOS_JOGO))
        
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
            
            # Gerar trevos baseado na estratégia
            if estrategia == 'combinacoes_trevos':
                trevos = self._gerar_trevos_combinacao_comum(quantidade_trevos)
            elif estrategia == 'agressiva':
                trevos = self._gerar_trevos_frequentes(quantidade_trevos)
            elif estrategia == 'conservadora':
                trevos = self._gerar_trevos_atrasados(quantidade_trevos)
            else:
                trevos = self._gerar_trevos_equilibrados(quantidade_trevos)
            
            jogos.append({
                'numeros': sorted(numeros),
                'trevos': sorted(trevos)
            })
        
        return {
            'sucesso': True,
            'estrategia': estrategia,
            'jogos': jogos
        }
    
    # ========== GERAÇÃO DE NÚMEROS ==========
    
    def _gerar_numeros_equilibrados(self, quantidade: int) -> List[int]:
        """Gera números com mix de frequentes e atrasados"""
        frequencias = self.estatistica.calcular_frequencia_numeros()
        atrasos = self.estatistica.calcular_atrasos_numeros()
        
        # Pegar metade dos mais frequentes e metade dos mais atrasados
        metade = quantidade // 2
        
        frequentes = [f['numero'] for f in frequencias[:15]]
        atrasados = [a['numero'] for a in atrasos[:15]]
        
        numeros = set()
        numeros.update(random.sample(frequentes, min(metade, len(frequentes))))
        numeros.update(random.sample(atrasados, min(quantidade - len(numeros), len(atrasados))))
        
        # Completar se necessário
        while len(numeros) < quantidade:
            numeros.add(random.randint(Config.MIN_NUMEROS, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    def _gerar_numeros_agressivos(self, quantidade: int) -> List[int]:
        """Gera números mais frequentes"""
        frequencias = self.estatistica.calcular_frequencia_numeros()
        
        # Pegar dos 20 mais frequentes
        pool = [f['numero'] for f in frequencias[:20]]
        return random.sample(pool, min(quantidade, len(pool)))
    
    def _gerar_numeros_conservadores(self, quantidade: int) -> List[int]:
        """Gera números mais atrasados"""
        atrasos = self.estatistica.calcular_atrasos_numeros()
        
        # Pegar dos 20 mais atrasados
        pool = [a['numero'] for a in atrasos[:20]]
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
            numeros.add(random.randint(Config.MIN_NUMEROS, Config.MAX_NUMEROS))
        
        return list(numeros)[:quantidade]
    
    # ========== GERAÇÃO DE TREVOS ==========
    
    def _gerar_trevos_equilibrados(self, quantidade: int) -> List[int]:
        """Gera trevos com mix de frequentes e atrasados"""
        frequencias = self.estatistica.calcular_frequencia_trevos()
        atrasos = self.estatistica.calcular_atrasos_trevos()
        
        metade = quantidade // 2
        
        frequentes = [f['trevo'] for f in frequencias[:3]]
        atrasados = [a['trevo'] for a in atrasos[:3]]
        
        trevos = set()
        trevos.update(random.sample(frequentes, min(metade, len(frequentes))))
        trevos.update(random.sample(atrasados, min(quantidade - len(trevos), len(atrasados))))
        
        # Completar se necessário
        while len(trevos) < quantidade:
            trevos.add(random.randint(Config.MIN_TREVOS, Config.MAX_TREVOS))
        
        return list(trevos)[:quantidade]
    
    def _gerar_trevos_frequentes(self, quantidade: int) -> List[int]:
        """Gera trevos mais frequentes"""
        frequencias = self.estatistica.calcular_frequencia_trevos()
        
        pool = [f['trevo'] for f in frequencias[:4]]
        return random.sample(pool, min(quantidade, len(pool)))
    
    def _gerar_trevos_atrasados(self, quantidade: int) -> List[int]:
        """Gera trevos mais atrasados"""
        atrasos = self.estatistica.calcular_atrasos_trevos()
        
        pool = [a['trevo'] for a in atrasos[:4]]
        return random.sample(pool, min(quantidade, len(pool)))
    
    def _gerar_trevos_combinacao_comum(self, quantidade: int) -> List[int]:
        """Usa combinação de trevos mais comum"""
        combinacoes = self.estatistica.calcular_combinacoes_trevos()
        
        if combinacoes and quantidade == 2:
            # Usar a combinação mais comum
            return combinacoes[0]['trevos']
        
        # Fallback para equilibrado
        return self._gerar_trevos_equilibrados(quantidade)
    
    def sugerir_trevos(self, estrategia: str = 'frequentes') -> List[int]:
        """
        Sugere 2 trevos baseado em estatísticas
        
        Args:
            estrategia: 'frequentes', 'atrasados' ou 'combinacao_comum'
            
        Returns:
            Lista com 2 trevos sugeridos
        """
        if estrategia == 'frequentes':
            return self._gerar_trevos_frequentes(2)
        elif estrategia == 'atrasados':
            return self._gerar_trevos_atrasados(2)
        elif estrategia == 'combinacao_comum':
            return self._gerar_trevos_combinacao_comum(2)
        else:
            return self._gerar_trevos_equilibrados(2)
    
    def conferir_jogo(self, numeros: List[int], trevos: List[int], concurso: int) -> Dict:
        """
        Confere um jogo contra um resultado
        
        Args:
            numeros: Números apostados
            trevos: Trevos apostados
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
        numeros_sorteados = [int(n) for n in resultado['listaDezenas']]
        trevos_sorteados = [int(t) for t in resultado['trevosSorteados']]
        
        # Contar acertos
        acertos_numeros = len(set(numeros) & set(numeros_sorteados))
        acertos_trevos = len(set(trevos) & set(trevos_sorteados))
        
        # Determinar faixa de premiação
        faixa = self._determinar_faixa(acertos_numeros, acertos_trevos)
        
        # Buscar valor do prêmio se houver
        valor_premio = 0.0
        if faixa > 0 and resultado.get('listaRateioPremio'):
            for rateio in resultado['listaRateioPremio']:
                if rateio.get('faixa') == faixa:
                    valor_premio = rateio.get('valorPremio', 0.0)
                    break
        
        return {
            'sucesso': True,
            'concurso': concurso,
            'acertos_numeros': acertos_numeros,
            'acertos_trevos': acertos_trevos,
            'faixa': faixa,
            'premiado': faixa > 0,
            'valor_premio': valor_premio,
            'numeros_sorteados': numeros_sorteados,
            'trevos_sorteados': trevos_sorteados
        }
    
    def _determinar_faixa(self, acertos_numeros: int, acertos_trevos: int) -> int:
        """
        Determina a faixa de premiação baseada nos acertos
        
        Args:
            acertos_numeros: Quantidade de números acertados
            acertos_trevos: Quantidade de trevos acertados
            
        Returns:
            Número da faixa (0 se não premiado)
        """
        # Faixa 1: 6 números + 2 trevos
        if acertos_numeros == 6 and acertos_trevos == 2:
            return 1
        
        # Faixa 2: 6 números + 1 ou 0 trevos
        if acertos_numeros == 6 and acertos_trevos in [0, 1]:
            return 2
        
        # Faixa 3: 5 números + 2 trevos
        if acertos_numeros == 5 and acertos_trevos == 2:
            return 3
        
        # Faixa 4: 5 números + 1 ou 0 trevos
        if acertos_numeros == 5 and acertos_trevos in [0, 1]:
            return 4
        
        # Faixa 5: 4 números + 2 trevos
        if acertos_numeros == 4 and acertos_trevos == 2:
            return 5
        
        # Faixa 6: 4 números + 1 ou 0 trevos
        if acertos_numeros == 4 and acertos_trevos in [0, 1]:
            return 6
        
        # Faixa 7: 3 números + 2 trevos
        if acertos_numeros == 3 and acertos_trevos == 2:
            return 7
        
        # Faixa 8: 3 números + 1 trevo
        if acertos_numeros == 3 and acertos_trevos == 1:
            return 8
        
        # Faixa 9: 2 números + 2 trevos
        if acertos_numeros == 2 and acertos_trevos == 2:
            return 9
        
        # Faixa 10: 2 números + 1 trevo
        if acertos_numeros == 2 and acertos_trevos == 1:
            return 10
        
        return 0  # Não premiado
