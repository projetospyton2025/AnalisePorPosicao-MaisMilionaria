// Funções gerais do sistema +Milionária

// Configuração base
const API_BASE = '/api';

// Utilitários
function showLoading(element) {
    if (element) {
        element.innerHTML = '<div class="loading active"><div class="spinner"></div><p>Carregando...</p></div>';
    }
}

function hideLoading(element) {
    if (element) {
        const loading = element.querySelector('.loading');
        if (loading) loading.remove();
    }
}

function showAlert(message, type = 'info', container = null) {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    
    if (container) {
        container.insertBefore(alert, container.firstChild);
    } else {
        document.querySelector('.container').insertBefore(alert, document.querySelector('.container').firstChild);
    }
    
    setTimeout(() => alert.remove(), 5000);
}

// Formatação de valores
function formatarMoeda(valor) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(valor);
}

function formatarData(data) {
    // Espera data no formato DD/MM/YYYY
    return data;
}

// ========== API - Atualização ==========

async function atualizarBaseDados() {
    try {
        showAlert('Iniciando atualização da base de dados...', 'info');
        
        const response = await fetch(`${API_BASE}/atualizar-ultimos`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ quantidade: 50 })
        });
        
        const data = await response.json();
        
        if (data.sucesso) {
            showAlert(`Atualização concluída! ${data.inseridos} concursos atualizados.`, 'success');
            setTimeout(() => location.reload(), 2000);
        } else {
            showAlert(data.mensagem || 'Erro ao atualizar', 'danger');
        }
    } catch (error) {
        showAlert('Erro ao conectar com o servidor', 'danger');
        console.error('Erro:', error);
    }
}

// ========== Dashboard - Último Resultado ==========

async function carregarUltimoResultado() {
    const container = document.getElementById('ultimo-resultado-container');
    if (!container) return;
    
    try {
        showLoading(container);
        
        const response = await fetch(`${API_BASE}/ultimo-resultado`);
        const data = await response.json();
        
        if (data.sucesso) {
            renderizarUltimoResultado(data.resultado, container);
        } else {
            container.innerHTML = '<p class="text-center">Nenhum resultado encontrado. Clique em "Atualizar" para buscar dados.</p>';
        }
    } catch (error) {
        container.innerHTML = '<p class="text-center">Erro ao carregar resultado</p>';
        console.error('Erro:', error);
    }
}

function renderizarUltimoResultado(resultado, container) {
    const numerosHtml = resultado.listaDezenas.map(n => 
        `<span class="numero">${n}</span>`
    ).join('');
    
    const trevosHtml = resultado.trevosSorteados.map(t => 
        `<span class="trevo">🍀 ${t}</span>`
    ).join('');
    
    const valorPremio = resultado.valorEstimadoProximoConcurso || 0;
    
    container.innerHTML = `
        <div class="ultimo-resultado">
            <div class="concurso-info">
                <strong>Concurso ${resultado.numero}</strong> - ${resultado.dataApuracao}
            </div>
            
            <div>
                <div style="font-weight: 600; margin-bottom: 10px;">Números Sorteados</div>
                <div class="numeros-container">
                    ${numerosHtml}
                </div>
            </div>
            
            <div class="trevos-section">
                <div class="trevos-label">Trevos da Sorte 🍀</div>
                <div class="trevos-container">
                    ${trevosHtml}
                </div>
            </div>
            
            <div class="premio-info">
                Estimativa Próximo Concurso<br>
                <span class="premio-valor">${formatarMoeda(valorPremio)}</span>
            </div>
        </div>
    `;
}

// ========== Estatísticas ==========

async function carregarEstatisticasNumeros() {
    const container = document.getElementById('stats-numeros-container');
    if (!container) return;
    
    try {
        showLoading(container);
        
        const response = await fetch(`${API_BASE}/estatisticas/numeros`);
        const data = await response.json();
        
        if (data.sucesso) {
            renderizarEstatisticasNumeros(data.estatisticas, container);
        }
    } catch (error) {
        container.innerHTML = '<p>Erro ao carregar estatísticas</p>';
        console.error('Erro:', error);
    }
}

function renderizarEstatisticasNumeros(stats, container) {
    const maisFrequentes = stats.frequencia.slice(0, 10);
    const maisAtrasados = stats.atrasos.slice(0, 10);
    
    const frequentesHtml = maisFrequentes.map(item => `
        <div class="stat-item">
            <div class="numero" style="display: inline-block; margin-right: 10px;">${item.numero}</div>
            <div style="display: inline-block;">
                <div class="stat-label">Frequência</div>
                <div class="stat-value">${item.vezes}x (${item.percentual}%)</div>
            </div>
        </div>
    `).join('');
    
    const atrasadosHtml = maisAtrasados.map(item => `
        <div class="stat-item">
            <div class="numero" style="display: inline-block; margin-right: 10px;">${item.numero}</div>
            <div style="display: inline-block;">
                <div class="stat-label">Atraso</div>
                <div class="stat-value">${item.atraso} concursos</div>
            </div>
        </div>
    `).join('');
    
    container.innerHTML = `
        <div class="stats-grid">
            <div>
                <h3>Mais Frequentes</h3>
                ${frequentesHtml}
            </div>
            <div>
                <h3>Mais Atrasados</h3>
                ${atrasadosHtml}
            </div>
        </div>
        
        <div class="mt-3">
            <h3>Distribuição Par/Ímpar</h3>
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-label">Números Pares</div>
                    <div class="stat-value">${stats.pares_impares.pares} (${stats.pares_impares.percentual_pares}%)</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Números Ímpares</div>
                    <div class="stat-value">${stats.pares_impares.impares} (${stats.pares_impares.percentual_impares}%)</div>
                </div>
            </div>
        </div>
    `;
}

async function carregarEstatisticasTrevos() {
    const container = document.getElementById('stats-trevos-container');
    if (!container) return;
    
    try {
        showLoading(container);
        
        const response = await fetch(`${API_BASE}/estatisticas/trevos`);
        const data = await response.json();
        
        if (data.sucesso) {
            renderizarEstatisticasTrevos(data.estatisticas, container);
        }
    } catch (error) {
        container.innerHTML = '<p>Erro ao carregar estatísticas</p>';
        console.error('Erro:', error);
    }
}

function renderizarEstatisticasTrevos(stats, container) {
    const frequenciasHtml = stats.frequencia.map(item => {
        const largura = item.percentual;
        return `
            <div class="trevo-stat-item">
                <div class="trevo-numero">🍀 ${item.trevo}</div>
                <div class="trevo-info">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                        <span>${item.vezes} vezes</span>
                        <span>${item.percentual}%</span>
                    </div>
                    <div class="barra-progresso">
                        <div class="barra-preenchimento" style="width: ${largura}%;"></div>
                    </div>
                </div>
            </div>
        `;
    }).join('');
    
    const combinacoesHtml = stats.combinacoes.slice(0, 5).map((item, index) => `
        <div class="stat-item">
            <div style="font-weight: 600;">${index + 1}º. Trevos ${item.trevos.join(' + ')}</div>
            <div class="stat-value">${item.vezes} vezes</div>
        </div>
    `).join('');
    
    container.innerHTML = `
        <div>
            <h3>Frequência dos Trevos 🍀</h3>
            <div class="trevos-stats">
                ${frequenciasHtml}
            </div>
        </div>
        
        <div class="mt-3">
            <h3>Combinações Mais Comuns</h3>
            <div class="stats-grid">
                ${combinacoesHtml}
            </div>
        </div>
    `;
}

// ========== Geração de Palpites ==========

async function gerarPalpite() {
    const form = document.getElementById('form-palpite');
    const resultContainer = document.getElementById('palpite-resultado');
    
    if (!form || !resultContainer) return;
    
    const estrategia = form.querySelector('[name="estrategia"]').value;
    const quantidadeNumeros = parseInt(form.querySelector('[name="quantidade_numeros"]').value);
    const quantidadeTrevos = parseInt(form.querySelector('[name="quantidade_trevos"]').value);
    const quantidadeJogos = parseInt(form.querySelector('[name="quantidade_jogos"]')?.value || 1);
    
    try {
        showLoading(resultContainer);
        
        const response = await fetch(`${API_BASE}/gerar-palpite`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                estrategia,
                quantidade_numeros: quantidadeNumeros,
                quantidade_trevos: quantidadeTrevos,
                quantidade_jogos: quantidadeJogos
            })
        });
        
        const data = await response.json();
        
        if (data.sucesso) {
            renderizarPalpites(data.jogos, resultContainer);
        } else {
            resultContainer.innerHTML = `<div class="alert alert-danger">${data.mensagem}</div>`;
        }
    } catch (error) {
        resultContainer.innerHTML = '<div class="alert alert-danger">Erro ao gerar palpite</div>';
        console.error('Erro:', error);
    }
}

function renderizarPalpites(jogos, container) {
    const jogosHtml = jogos.map((jogo, index) => {
        const numerosHtml = jogo.numeros.map(n => 
            `<span class="numero">${String(n).padStart(2, '0')}</span>`
        ).join('');
        
        const trevosHtml = jogo.trevos.map(t => 
            `<span class="trevo">🍀 ${t}</span>`
        ).join('');
        
        return `
            <div class="palpite-gerado">
                <h3>Palpite ${jogos.length > 1 ? index + 1 : ''}</h3>
                
                <div style="margin: 1.5rem 0;">
                    <div style="font-weight: 600; margin-bottom: 10px;">Números</div>
                    <div class="numeros-container">
                        ${numerosHtml}
                    </div>
                </div>
                
                <div class="trevos-section">
                    <div class="trevos-label">Trevos 🍀</div>
                    <div class="trevos-container">
                        ${trevosHtml}
                    </div>
                </div>
            </div>
        `;
    }).join('');
    
    container.innerHTML = jogosHtml;
}

async function sugerirTrevos() {
    const estrategia = document.getElementById('estrategia-trevos')?.value || 'frequentes';
    
    try {
        const response = await fetch(`${API_BASE}/sugerir-trevos?estrategia=${estrategia}`);
        const data = await response.json();
        
        if (data.sucesso) {
            // Atualizar campos de trevos se existirem
            const trevoInputs = document.querySelectorAll('[name="trevos[]"]');
            data.trevos.forEach((trevo, index) => {
                if (trevoInputs[index]) {
                    trevoInputs[index].value = trevo;
                }
            });
            
            showAlert(`Trevos sugeridos: ${data.trevos.join(', ')} 🍀`, 'success');
        }
    } catch (error) {
        showAlert('Erro ao sugerir trevos', 'danger');
        console.error('Erro:', error);
    }
}

// ========== Inicialização ==========

document.addEventListener('DOMContentLoaded', function() {
    // Carregar dados da página inicial
    if (document.getElementById('ultimo-resultado-container')) {
        carregarUltimoResultado();
    }
    
    if (document.getElementById('stats-numeros-container')) {
        carregarEstatisticasNumeros();
    }
    
    if (document.getElementById('stats-trevos-container')) {
        carregarEstatisticasTrevos();
    }
    
    // Event listeners para formulários
    const formPalpite = document.getElementById('form-palpite');
    if (formPalpite) {
        formPalpite.addEventListener('submit', function(e) {
            e.preventDefault();
            gerarPalpite();
        });
    }
    
    const btnAtualizar = document.getElementById('btn-atualizar');
    if (btnAtualizar) {
        btnAtualizar.addEventListener('click', atualizarBaseDados);
    }
    
    const btnSugerirTrevos = document.getElementById('btn-sugerir-trevos');
    if (btnSugerirTrevos) {
        btnSugerirTrevos.addEventListener('click', sugerirTrevos);
    }
});
