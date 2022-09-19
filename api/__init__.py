from flask import Flask
from database import db

import config

app = Flask(__name__)
app.config.from_object(config)

from .services import criar_tabelas_servico
from .urls import funcionario_url, cliente_url, mecanico_url, chefe_url, recepcionista_url, faturista_url, auxiliar_de_faturista_url, oficina_url, loja_conveniada_url, produto_url, veiculo_url, servico_url, tabela_de_preco_url, etapa_serviso_url, ordem_servico_url, item_OS_url, solicitacao_reboque_url, nota_fiscal_url, item_NF_url, nota_fiscal_servico_url, titulo_url

from populando_BD import Popular

#Popular()

app.register_blueprint(funcionario_url.urls, url_prefix='/')
app.register_blueprint(cliente_url.urls, url_prefix='/')
app.register_blueprint(mecanico_url.urls, url_prefix='/')
app.register_blueprint(chefe_url.urls, url_prefix='/')
app.register_blueprint(recepcionista_url.urls, url_prefix='/')
app.register_blueprint(faturista_url.urls, url_prefix='/')
app.register_blueprint(auxiliar_de_faturista_url.urls, url_prefix='/')
app.register_blueprint(oficina_url.urls, url_prefix='/')
app.register_blueprint(loja_conveniada_url.urls, url_prefix='/')
app.register_blueprint(produto_url.urls, url_prefix='/')
app.register_blueprint(veiculo_url.urls, url_prefix='/')
app.register_blueprint(servico_url.urls, url_prefix='/')
app.register_blueprint(tabela_de_preco_url.urls, url_prefix='/')
app.register_blueprint(etapa_serviso_url.urls,  url_prefix='/')
app.register_blueprint(ordem_servico_url.urls, url_prefix='/')
app.register_blueprint(item_OS_url.urls, url_prefix='/')
app.register_blueprint(solicitacao_reboque_url.urls, url_prefix='/')
app.register_blueprint(nota_fiscal_url.urls, url_prefix='/')
app.register_blueprint(item_NF_url.urls, url_prefix='/')
app.register_blueprint(nota_fiscal_servico_url.urls, url_prefix='/')
app.register_blueprint(titulo_url.urls, url_prefix='/')
