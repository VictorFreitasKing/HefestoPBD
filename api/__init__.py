from flask import Flask
from database import db

import config

app = Flask(__name__)
app.config.from_object(config)

from .entidades import funcionario, cliente, mecanico
from .services import funcionario_service, cliente_service, mecanico_service
from .urls import funcionario_url, cliente_url, mecanico_url

funcionario_service.criar_tabela()
cliente_service.criar_tabela()
mecanico_service.criar_tabela()

app.register_blueprint(funcionario_url.urls, url_prefix='/')
app.register_blueprint(cliente_url.urls, url_prefix='/')
app.register_blueprint(mecanico_url.urls, url_prefix='/')
