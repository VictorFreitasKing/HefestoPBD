from database import db
from entidades import funcionario, cliente, mecanico, chefe, recepcionista, faturista, auxiliar_de_faturista, oficina, loja_conveniada, produto, veiculo, servico, tabela_de_precos, etapa_servico, ordem_servico, item_OS, solicitacao_reboque, nota_fiscal, item_NF, nota_fiscal_servico, titulo
from services import funcionario_service, cliente_service, mecanico_service, chefe_service, recepcionista_service, faturista_service, auxiliar_de_faturista_service, oficina_service, loja_conveniada_service, produto_service, veiculos_service, servico_service, tabela_de_precos_service, etapa_servico_services, ordem_servico_service, item_OS_service, solicitacao_reboque_service, nota_fiscal_servico_service, item_NF_service, nota_fiscal_service, titulos_service

def Popular():
    funcionario_service.cadastrar(
        funcionario=funcionario.Funcionario(
            nome="Victor",
            cpf="11111111111",
            rg="1111111",
            telefone="87999999999",
            celular="87999999999",
            pais="Brasil",
            estado="PE",
            cidade="Custodia",
            bairro="Centro",
            logradouro="Rua A",
            data_admissao="01/01/2000",
            data_demissao="",
            salario=2500,
            senha="lorenipsu",
            urlImagem="a"
        )
    )

    funcionario_service.cadastrar(
        funcionario=funcionario.Funcionario(
            nome="Helen",
            cpf="11111111112",
            rg="1111112",
            telefone="87999999999",
            celular="87999999999",
            pais="Brasil",
            estado="PE",
            cidade="Afogados",
            bairro="Centro",
            logradouro="Rua A",
            data_admissao="01/01/2000",
            data_demissao="",
            salario=2500,
            senha="lorenipsu",
            urlImagem=""
        )
    )

    funcionario_service.cadastrar(
        funcionario=funcionario.Funcionario(
            nome="Victor",
            cpf="11111111113",
            rg="1111113",
            telefone="87999999999",
            celular="87999999999",
            pais="Brasil",
            estado="PE",
            cidade="Afogados",
            bairro="Centro",
            logradouro="Rua A",
            data_admissao="01/01/2000",
            data_demissao="",
            salario=1500,
            senha="lorenipsu",
            urlImagem=""
        )
    )

    cliente_service.cadastrar(
        cliente=cliente.Cliente(
            nome="Victor",
            cpf="11111111113",
            rg="1111113",
            telefone="87999999999",
            celular="87999999999",
            pais="Brasil",
            estado="PE",
            cidade="Afogados",
            bairro="Centro",
            logradouro="Rua A",
            tipo="Especial"
        )
    )

    cliente_service.cadastrar(
        cliente=cliente.Cliente(
            nome="Marcos",
            cpf="11111111114",
            rg="1111114",
            telefone="87999999999",
            celular="87999999999",
            pais="Brasil",
            estado="PE",
            cidade="Serra Talhada",
            bairro="Centro",
            logradouro="Rua A",
            tipo="Devedor"
        )
    )

    mecanico_service.cadastrar(
        mecanico=mecanico.Mecanico(
            matriculaFuncionario=3,
            especialidade="Troca de oleo"
        )
    )

    chefe_service.cadastrar(
        chefe=chefe.Chefe(
            matriculaFuncionario=1
        )
    )

    recepcionista_service.cadastrar(
        recepcionista=recepcionista.Recepcionista(
            matriculaFuncionario=1
        )
    )

    faturista_service.cadastrar(
        faturista=faturista.Faturista(
            matriculaFuncionario=1
        )
    )

    auxiliar_de_faturista_service.cadastrar(
        auxiliar_de_faturista=auxiliar_de_faturista.Auxiliar_de_Faturista(
            matriculaFuncionario=1
        )
    )

    oficina_service.cadastrar(
        oficina=oficina.Oficina(
            codigoChefe=1,
            razao_social="Oficina Santa Luzia",
            cnpj="11111111111111",
            IE="11111111111",
            pais="Brasil",
            estado="PE",
            cidade="Serra Talhada",
            bairro="Centro",
            logradouro="Rua A"
        )
    )

    loja_conveniada_service.cadastrar(
        loja_conveniada=loja_conveniada.Loja_Conveniada(
            razao_social="Loja das dores",
            cnpj="11111111111112",
            IE="11111111112",
            pais="Brasil",
            estado="PE",
            cidade="Serra Talhada",
            bairro="Centro",
            logradouro="Rua A",
            inicio_vigencia="01/01/2000",
            fim_vigencia="01/01/2022"
        )
    )

    produto_service.cadastrar(
        produto=produto.Produto(
            descricao="Oleo disel"
        )
    )

    veiculos_service.cadastrar(
        veiculo=veiculo.Veiculo(
            codigoCliente=1,
            placa="PGF001",
            marca="FIAT",
            modelo="UNO 2015"
        )
    )

    veiculos_service.cadastrar(
        veiculo=veiculo.Veiculo(
            codigoCliente=1,
            placa="PGF001",
            marca="FIAT",
            modelo="UNO 2017"
        )
    )

    veiculos_service.cadastrar(
        veiculo=veiculo.Veiculo(
            codigoCliente=1,
            placa="PGF002",
            marca="Volkswagen",
            modelo="GOL"
        )
    )

    servico_service.cadastrar(
        servico=servico.Servico(
            descricao="troca de oleo"
        )
    )

    etapa_servico_services.cadastrar(
        etapa_servico=etapa_servico.Etapa_Servico(
            codigoServico=1,
            descricao="trocar o oleo",
            ordem=1
        )
    )

    tabela_de_precos_service.cadastrar(
        tabela_de_precos=tabela_de_precos.Tabela_de_preco(
            codigoServico=1,
            preco=30,
            inicio="01/01/2022",
            fim="31/12/2022"
        )
    )

    ordem_servico_service.cadastrar(
        ordem_servicos=ordem_servico.Ordem_servico(
            codigoMecanico=1,
            codigoVeiculo=1,
            entrada="01/01/2022",
            saida="01/01/2022",
            total=30
        )
    )

    item_OS_service.cadastrar(
        item_OS=item_OS.Item_OS(
            codigoOS=1,
            codigoServico=1,
            codigoMecanico=1,
            preco=30,
            status="Ok"
        )
    )

    solicitacao_reboque_service.cadastrar(
        solicitacao_reboque=solicitacao_reboque.Solicitacao_reboque(
            codigoCliente=1,
            latitude="11111111111",
            longitude="11111111111"
        )
    )

    nota_fiscal_service.cadastrar(
        nota_fiscal=nota_fiscal.Nota_Fiscal(
            codigo_loja_conveniada=1,
            numero=1,
            serie=1,
            codigoAuxiliarFaturista=1,
            codigoOS=1,
            total=15
        )
    )

    item_NF_service.cadastrar(
        item_NF=item_NF.Item_NF(
            codigoNF=1,
            codigoProduto=1,
            quantidade=1,
            preco=15
        )
    )

    nota_fiscal_servico_service.cadastrar(
        nota_fiscal_servico=nota_fiscal_servico.Nota_Fiscal_Servico(
            codigoOS=1,
            codigoFaturista=1,
            data_emissao="01/01/2022",
            total=30
        )
    )

    titulos_service.cadastrar(
        titulo=titulo.Titulo(
            codigoNFS=1,
            codigoRecepcionista=1,
            valor=30,
            vencimento="01/01/2022",
            data_baixa="01/01/2022"
        )
    )