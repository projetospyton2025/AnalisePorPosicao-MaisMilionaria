"""
Rotas principais (HTML)
"""
from flask import Blueprint, render_template
from models import ResultadoModel

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Página principal - Dashboard"""
    model = ResultadoModel()
    ultimo_resultado = model.buscar_ultimo_resultado()
    total_concursos = model.contar_resultados()
    
    return render_template(
        'index.html',
        ultimo_resultado=ultimo_resultado,
        total_concursos=total_concursos
    )


@main_bp.route('/palpites')
def palpites():
    """Página de geração de palpites"""
    return render_template('palpites.html')


@main_bp.route('/estatisticas')
def estatisticas():
    """Página de estatísticas detalhadas"""
    return render_template('estatisticas.html')


@main_bp.route('/conferir')
def conferir():
    """Página para conferir jogos"""
    return render_template('conferir.html')
