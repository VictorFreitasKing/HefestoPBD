from flask import Flask
from database import db

import config

app = Flask(__name__)
app.config.from_object(config)

from .entidades import funcionario, cliente, mecanico, chefe, recepcionista, faturista, auxiliar_de_faturista, oficina, loja_conveniada, produto, veiculo, servico, tabela_de_precos, etapa_servico, ordem_servico, item_OS, solicitacao_reboque, nota_fiscal, item_NF, nota_fiscal_servico, titulo
from .services import funcionario_service, cliente_service, mecanico_service, chefes_service, recepcionistas_service, faturistas_service, auxiliar_de_faturista_service, oficinas_service, lojas_conveniadas_service, produto_service, veiculos_service, servicos_service, tabela_de_preco_service, etapa_servico_services, ordem_servico_service, item_OS_service, solicitacao_reboque_service, notas_fiscais_service, itens_NF_service, notas_fiscais_servico_service, titulos_service
from .urls import funcionario_url, cliente_url, mecanico_url, chefes_url, recepcionistas_url, faturistas_url, auxiliares_de_faturistas_url, oficinas_url, lojas_conveniadas_url, produto_url, veiculos_url, servicos_url, tabela_de_preco_url, etapa_serviso_url, ordem_servico_url, item_OS_url, solicitacao_reboque_url, notas_fiscais_url, itens_NF_url, notas_fiscais_servico_url, titulos_url

funcionario_service.criar_tabela()
cliente_service.criar_tabela()
mecanico_service.criar_tabela()
chefes_service.criar_tabela()
recepcionistas_service.criar_tabela()
faturistas_service.criar_tabela()
auxiliar_de_faturista_service.criar_tabela()
oficinas_service.criar_tabela()
lojas_conveniadas_service.criar_tabela()
produto_service.criar_tabela()
veiculos_service.criar_tabela()
servicos_service.criar_tabela()
tabela_de_preco_service.criar_tabela()
etapa_servico_services.criar_tabela()
ordem_servico_service.criar_tabela()
item_OS_service.criar_tabela()
solicitacao_reboque_service.criar_tabela()
notas_fiscais_service.criar_tabela()
itens_NF_service.criar_tabela()
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
