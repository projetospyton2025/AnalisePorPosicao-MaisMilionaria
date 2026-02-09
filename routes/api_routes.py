"""
Rotas da API REST
"""
from flask import Blueprint, jsonify, request
from services import ApiCaixaService, EstatisticaService, MaisMilionariaService

api_bp = Blueprint('api', __name__, url_prefix='/api')

# Inicializar serviços
api_caixa = ApiCaixaService()
estatistica = EstatisticaService()
maismilionaria = MaisMilionariaService()


@api_bp.route('/atualizar', methods=['POST'])
def atualizar():
    """Atualiza a base de dados com resultados da API"""
    try:
        data = request.get_json() or {}
        concurso_inicial = data.get('concurso_inicial', 1)
        
        resultado = api_caixa.atualizar_base_dados(concurso_inicial)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro ao atualizar: {str(e)}'
        }), 500


@api_bp.route('/atualizar-ultimos', methods=['POST'])
def atualizar_ultimos():
    """Atualiza apenas os últimos concursos"""
    try:
        data = request.get_json() or {}
        quantidade = data.get('quantidade', 10)
        
        resultado = api_caixa.atualizar_ultimos_concursos(quantidade)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro ao atualizar: {str(e)}'
        }), 500


@api_bp.route('/ultimo-resultado', methods=['GET'])
def ultimo_resultado():
    """Retorna o último resultado"""
    try:
        from models import ResultadoModel
        model = ResultadoModel()
        resultado = model.buscar_ultimo_resultado()
        
        if resultado:
            return jsonify({
                'sucesso': True,
                'resultado': resultado
            })
        else:
            return jsonify({
                'sucesso': False,
                'mensagem': 'Nenhum resultado encontrado'
            }), 404
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@api_bp.route('/resultados', methods=['GET'])
def resultados():
    """Lista resultados"""
    try:
        limite = request.args.get('limite', 100, type=int)
        
        from models import ResultadoModel
        model = ResultadoModel()
        lista = model.listar_resultados(limite)
        
        return jsonify({
            'sucesso': True,
            'resultados': lista,
            'total': len(lista)
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@api_bp.route('/resultado/<int:numero>', methods=['GET'])
def resultado(numero):
    """Retorna um resultado específico"""
    try:
        from models import ResultadoModel
        model = ResultadoModel()
        res = model.buscar_resultado(numero)
        
        if res:
            return jsonify({
                'sucesso': True,
                'resultado': res
            })
        else:
            return jsonify({
                'sucesso': False,
                'mensagem': 'Resultado não encontrado'
            }), 404
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@api_bp.route('/estatisticas', methods=['GET'])
def estatisticas():
    """Retorna estatísticas completas (números + trevos)"""
    try:
        stats = estatistica.calcular_estatisticas_completas()
        return jsonify({
            'sucesso': True,
            'estatisticas': stats
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@api_bp.route('/estatisticas/numeros', methods=['GET'])
def estatisticas_numeros():
    """Retorna estatísticas apenas dos números"""
    try:
        stats = estatistica.calcular_estatisticas_numeros()
        return jsonify({
            'sucesso': True,
            'estatisticas': stats
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@api_bp.route('/estatisticas/trevos', methods=['GET'])
def estatisticas_trevos():
    """Retorna estatísticas apenas dos trevos"""
    try:
        stats = estatistica.calcular_estatisticas_trevos()
        return jsonify({
            'sucesso': True,
            'estatisticas': stats
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@api_bp.route('/sugerir-trevos', methods=['GET'])
def sugerir_trevos():
    """Sugere 2 trevos automaticamente"""
    try:
        estrategia = request.args.get('estrategia', 'frequentes')
        trevos = maismilionaria.sugerir_trevos(estrategia)
        
        return jsonify({
            'sucesso': True,
            'trevos': trevos,
            'estrategia': estrategia
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@api_bp.route('/gerar-palpite', methods=['POST'])
def gerar_palpite():
    """Gera palpites (números + trevos)"""
    try:
        data = request.get_json() or {}
        
        estrategia = data.get('estrategia', 'equilibrada')
        quantidade_numeros = data.get('quantidade_numeros', 6)
        quantidade_trevos = data.get('quantidade_trevos', 2)
        quantidade_jogos = data.get('quantidade_jogos', 1)
        
        palpite = maismilionaria.gerar_palpite(
            estrategia=estrategia,
            quantidade_numeros=quantidade_numeros,
            quantidade_trevos=quantidade_trevos,
            quantidade_jogos=quantidade_jogos
        )
        
        return jsonify(palpite)
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@api_bp.route('/conferir', methods=['POST'])
def conferir():
    """Confere um jogo"""
    try:
        data = request.get_json() or {}
        
        numeros = data.get('numeros', [])
        trevos = data.get('trevos', [])
        concurso = data.get('concurso')
        
        if not numeros or not trevos or not concurso:
            return jsonify({
                'sucesso': False,
                'mensagem': 'Parâmetros inválidos'
            }), 400
        
        resultado = maismilionaria.conferir_jogo(numeros, trevos, concurso)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500
