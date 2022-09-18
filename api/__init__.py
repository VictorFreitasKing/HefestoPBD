from flask import Flask
from database import db

import config

app = Flask(__name__)
app.config.from_object(config)

from .services import criar_tabelas_servico
from .urls import funcionario_url, cliente_url, mecanico_url, chefes_url, recepcionistas_url, faturistas_url, auxiliares_de_faturistas_url, oficinas_url, lojas_conveniadas_url, produto_url, veiculos_url, servicos_url, tabela_de_preco_url, etapa_serviso_url, ordem_servico_url, item_OS_url, solicitacao_reboque_url, notas_fiscais_url, itens_NF_url, notas_fiscais_servico_url, titulos_url

app.register_blueprint(funcionario_url.urls, url_prefix='/')
app.register_blueprint(cliente_url.urls, url_prefix='/')
app.register_blueprint(mecanico_url.urls, url_prefix='/')
app.register_blueprint(chefes_url.urls, url_prefix='/')
app.register_blueprint(recepcionistas_url.urls, url_prefix='/')
app.register_blueprint(faturistas_url.urls, url_prefix='/')
app.register_blueprint(auxiliares_de_faturistas_url.urls, url_prefix='/')
app.register_blueprint(oficinas_url.urls, url_prefix='/')
app.register_blueprint(lojas_conveniadas_url.urls, url_prefix='/')
app.register_blueprint(produto_url.urls, url_prefix='/')
app.register_blueprint(veiculos_url.urls, url_prefix='/')
app.register_blueprint(servicos_url.urls, url_prefix='/')
app.register_blueprint(tabela_de_preco_url.urls, url_prefix='/')
app.register_blueprint(etapa_serviso_url.urls,  url_prefix='/')
app.register_blueprint(ordem_servico_url.urls, url_prefix='/')
app.register_blueprint(item_OS_url.urls, url_prefix='/')
app.register_blueprint(solicitacao_reboque_url.urls, url_prefix='/')
app.register_blueprint(notas_fiscais_url.urls, url_prefix='/')
app.register_blueprint(itens_NF_url.urls, url_prefix='/')
app.register_blueprint(notas_fiscais_servico_url.urls, url_prefix='/')
app.register_blueprint(titulos_url.urls, url_prefix='/')
