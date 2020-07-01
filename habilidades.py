from flask_restful import Resource, request
import json
lista_habilidades = ['Python', 'Java', 'Flask','PHP']
class Lista_habilidades(Resource):
    def get(self):
        return lista_habilidades
    def post(self):
        dados = json.loads(request.data)
        if dados not in lista_habilidades:
            lista_habilidades.append(dados)
            response = {'status':'sucesso', 'mensagem':'Registro inserido ','lista':lista_habilidades}
        else:
            mensagem = 'O registro {} ja existe na lista'.format(dados)
            response = {'status':'erro', 'mensagem':mensagem}
        return response
class Verificando_habilidades(Resource):
    def get(self):
        dados = json.loads(request.data)
        if dados in lista_habilidades:
            mensagem = 'Habilidade {} encontrado'.format(dados)
            response = {'status':'sucesso', 'mensagem':mensagem}
        else:
            mensagem = 'Habilidade {} não encontrado'.format(dados)
            response = {'status':'erro', 'mensagem':mensagem}
        return response