from flask import Flask
from database import db

import config

app = Flask(__name__)
app.config.from_object(config)

from .entidades import funcionario, cliente, mecanico, chefes, recepcionistas, faturistas, auxiliares_de_faturistas, oficinas, lojas_conveniadas, produto, veiculos, servicos
from .services import funcionario_service, cliente_service, mecanico_service, chefes_service, recepcionistas_service, faturistas_service, auxiliares_de_faturistas_service, oficinas_service, lojas_conveniadas_service, produto_service, veiculos_service, servicos_service
from .urls import funcionario_url, cliente_url, mecanico_url, chefes_url, recepcionistas_url, faturistas_url, auxiliares_de_faturistas_url, oficinas_url, lojas_conveniadas_url, produto_url, veiculos_url, servicos_url

funcionario_service.criar_tabela()
cliente_service.criar_tabela()
mecanico_service.criar_tabela()
chefes_service.criar_tabela()
recepcionistas_service.criar_tabela()
faturistas_service.criar_tabela()
auxiliares_de_faturistas_service.criar_tabela()
oficinas_service.criar_tabela()
lojas_conveniadas_service.criar_tabela()
produto_service.criar_tabela()
veiculos_service.criar_tabela()
servicos_service.criar_tabela()

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
