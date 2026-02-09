"""
Routes package initialization
"""
from .main_routes import main_bp
from .api_routes import api_bp
from .duplasena_routes import duplasena_bp

__all__ = ['main_bp', 'api_bp', 'duplasena_bp']
