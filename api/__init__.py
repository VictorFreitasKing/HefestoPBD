from flask import Flask
from database import db

import config

app = Flask(__name__)
app.config.from_object(config)

from .entidades import funcionario, cliente, mecanico, chefe, recepcionista, faturista, auxiliar_de_faturista, oficina, loja_conveniada, produto, veiculo, servico, tabela_de_precos, etapa_servico, ordem_servico, item_OS, solicitacao_reboque, nota_fiscal, item_NF, nota_fiscal_servico, titulo
from .services import funcionario_service, cliente_service, mecanico_service, chefe_service, recepcionista_service, faturista_service, auxiliar_de_faturista_service, oficina_service, loja_conveniada_service, produto_service, veiculos_service, servico_service, tabela_de_precos_service, etapa_servico_services, ordem_servico_service, item_OS_service, solicitacao_reboque_service, nota_fiscal_service, item_NF_service, notas_fiscais_servico_service, titulos_service
from .urls import funcionario_url, cliente_url, mecanico_url, chefes_url, recepcionistas_url, faturistas_url, auxiliares_de_faturistas_url, oficinas_url, lojas_conveniadas_url, produto_url, veiculos_url, servicos_url, tabela_de_preco_url, etapa_serviso_url, ordem_servico_url, item_OS_url, solicitacao_reboque_url, notas_fiscais_url, itens_NF_url, notas_fiscais_servico_url, titulos_url

funcionario_service.criar_tabela()
cliente_service.criar_tabela()
mecanico_service.criar_tabela()
chefe_service.criar_tabela()
recepcionista_service.criar_tabela()
faturista_service.criar_tabela()
auxiliar_de_faturista_service.criar_tabela()
oficina_service.criar_tabela()
loja_conveniada_service.criar_tabela()
produto_service.criar_tabela()
veiculos_service.criar_tabela()
servico_service.criar_tabela()
tabela_de_precos_service.criar_tabela()
etapa_servico_services.criar_tabela()
ordem_servico_service.criar_tabela()
item_OS_service.criar_tabela()
solicitacao_reboque_service.criar_tabela()
nota_fiscal_service.criar_tabela()
item_NF_service.criar_tabela()
notas_fiscais_servico_service.criar_tabela()
titulos_service.criar_tabela()

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
