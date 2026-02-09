"""
Rotas da API REST - Dupla Sena
"""
from flask import Blueprint, jsonify, request
from services import ApiDuplaSenaService, EstatisticaDuplaSenaService, DuplaSenaService

duplasena_bp = Blueprint('duplasena', __name__, url_prefix='/api/duplasena')

# Inicializar serviços
api_duplasena = ApiDuplaSenaService()
estatistica = EstatisticaDuplaSenaService()
duplasena = DuplaSenaService()


@duplasena_bp.route('/atualizar', methods=['POST'])
def atualizar():
    """Atualiza a base de dados com resultados da API"""
    try:
        data = request.get_json() or {}
        concurso_inicial = data.get('concurso_inicial', 1)
        
        resultado = api_duplasena.atualizar_base_dados(concurso_inicial)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro ao atualizar Dupla Sena: {str(e)}'
        }), 500


@duplasena_bp.route('/atualizar-ultimos', methods=['POST'])
def atualizar_ultimos():
    """Atualiza apenas os últimos concursos"""
    try:
        data = request.get_json() or {}
        quantidade = data.get('quantidade', 10)
        
        resultado = api_duplasena.atualizar_ultimos_concursos(quantidade)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro ao atualizar Dupla Sena: {str(e)}'
        }), 500


@duplasena_bp.route('/ultimo-resultado', methods=['GET'])
def ultimo_resultado():
    """Retorna o último resultado"""
    try:
        from models import DuplaSenaModel
        model = DuplaSenaModel()
        resultado = model.buscar_ultimo_resultado()
        
        if resultado:
            return jsonify({
                'sucesso': True,
                'resultado': resultado
            })
        else:
            return jsonify({
                'sucesso': False,
                'mensagem': 'Nenhum resultado da Dupla Sena encontrado'
            }), 404
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@duplasena_bp.route('/resultados', methods=['GET'])
def resultados():
    """Lista resultados"""
    try:
        limite = request.args.get('limite', 100, type=int)
        
        from models import DuplaSenaModel
        model = DuplaSenaModel()
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


@duplasena_bp.route('/resultado/<int:numero>', methods=['GET'])
def resultado(numero):
    """Retorna um resultado específico"""
    try:
        from models import DuplaSenaModel
        model = DuplaSenaModel()
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


@duplasena_bp.route('/estatisticas', methods=['GET'])
def estatisticas():
    """Retorna estatísticas completas"""
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


@duplasena_bp.route('/estatisticas/sorteio/<int:sorteio>', methods=['GET'])
def estatisticas_sorteio(sorteio):
    """Retorna estatísticas de um sorteio específico"""
    try:
        if sorteio not in [1, 2]:
            return jsonify({
                'sucesso': False,
                'mensagem': 'Sorteio deve ser 1 ou 2'
            }), 400
        
        stats = estatistica.calcular_estatisticas_sorteio(sorteio)
        return jsonify({
            'sucesso': True,
            'sorteio': sorteio,
            'estatisticas': stats
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@duplasena_bp.route('/estatisticas/gerais', methods=['GET'])
def estatisticas_gerais():
    """Retorna estatísticas gerais"""
    try:
        stats = estatistica.calcular_estatisticas_gerais()
        return jsonify({
            'sucesso': True,
            'estatisticas': stats
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro: {str(e)}'
        }), 500


@duplasena_bp.route('/gerar-palpite', methods=['POST'])
def gerar_palpite():
    """Gera palpites"""
    try:
        data = request.get_json() or {}
        
        estrategia = data.get('estrategia', 'equilibrada')
        quantidade_numeros = data.get('quantidade_numeros', 6)
        quantidade_jogos = data.get('quantidade_jogos', 1)
        
        resultado = duplasena.gerar_palpite(
            estrategia=estrategia,
            quantidade_numeros=quantidade_numeros,
            quantidade_jogos=quantidade_jogos
        )
        
        return jsonify(resultado)
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro ao gerar palpite: {str(e)}'
        }), 500


@duplasena_bp.route('/conferir', methods=['POST'])
def conferir():
    """Confere um jogo"""
    try:
        data = request.get_json() or {}
        
        numeros = data.get('numeros', [])
        concurso = data.get('concurso')
        
        if not numeros or not concurso:
            return jsonify({
                'sucesso': False,
                'mensagem': 'Números e concurso são obrigatórios'
            }), 400
        
        resultado = duplasena.conferir_jogo(numeros, concurso)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'mensagem': f'Erro ao conferir: {str(e)}'
        }), 500
