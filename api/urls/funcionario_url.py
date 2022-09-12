from ..entidades import funcionario
from ..views import funcionario_view
from flask import request, Blueprint, make_response, render_template
from api import app

urls = Blueprint('funcionarios', __name__)

@urls.route('/')
def home():
    return render_template("home.html")

@app.route('/api/funcionarios/', methods=['GET', 'POST'])
def url_geral_funcionario():
    if (request.method == "GET"):
        return funcionario_view.Funcionario_view().getAll()
    if (request.method == "POST"):
        funcionarioTemp = funcionario.Funcionario(
            nome=request.json["nome"],
            cpf=request.json["cpf"],
            rg=request.json["rg"],
            telefone=request.json["telefone"],
            celular=request.json["celular"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"],
            data_admissao=request.json["data_admissao"],
            data_demissao=request.json["data_demissao"],
            salario=request.json["salario"],
            senha=request.json["senha"]
        )

        return funcionario_view.Funcionario_view().post(funcionarioTemp)


@app.route('/api/funcionarios/<int:id>/', methods=['GET', 'POST'])
def url_unico_funcionario(id):
    if request.method == 'GET':
        return funcionario_view.Funcionario_view().get(id)
    if request.method == 'POST':
        funcionarioTemp = funcionario.Funcionario(
            matricula=id,
            nome=request.json["nome"],
            cpf=request.json["cpf"],
            rg=request.json["rg"],
            telefone=request.json["telefone"],
            celular=request.json["celular"],
            pais=request.json["pais"],
            estado=request.json["estado"],
            cidade=request.json["cidade"],
            bairro=request.json["bairro"],
            logradouro=request.json["logradouro"],
            data_admissao=request.json["data_admissao"],
            data_demissao=request.json["data_demissao"],
            salario=request.json["salario"],
            senha=request.json["senha"]
        )
        return funcionario_view.Funcionario_view().patch(id, funcionarioTemp)
    else:
        return make_response({}, 404)
