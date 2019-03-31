from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Olá Mundo")


def articles(request, year):
    return HttpResponse("O número informado é: " + str(year))


def recuperarPessoaEMontarString(request, name):
    print(name)
    result = lerDoBanco(name)
    print(result)

    if result['idade'] > 0:
        return HttpResponse(
            'Pessoa com o nome ' + str(result['nome']) + ' encontrada e com a idade de ' + str(result['idade']))
    else:
        return HttpResponse('Não encontrado')


def lerDoBanco(name):
    lista = [
        {'nome': 'Isabelle', 'idade' : 33},
        {'nome': 'Leo', 'idade': 27}
    ]

    for pessoa in lista:
        if pessoa['nome'] == name:
            return pessoa
    else:
        return {'nome' : '', 'idade' : 0}


def recuperarPessoa(request, nome):
    pessoa = lerDoBanco(nome)
    return render(request, 'pessoa.html', {
        'v_idade' : pessoa['idade'],
        'v_nome' : pessoa['nome']}
    )