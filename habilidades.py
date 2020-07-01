from flask_restful import Resource, request
import json
lista_habilidades = ['Python', 'Java', 'Flask','PHP']
class Habilidades(Resource):
    def get(self,id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            mensagem = 'Habilidade com ID {} não existe'.format(id)
            response = {'staus':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. procure o administrado da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response
    def put(self, id):
        try:
            response = json.loads(request.data)
            lista_habilidades[id] = response
        except IndexError:
            mensagem = 'Habilidade com ID {} não existe'.format(id)
            response = {'staus': 'erro', 'mensagem': mensagem}
        return response
    def delete(self,id):
        try:
            lista_habilidades.pop(id)
            response ={'status':'sucesso', 'mensagem':'Registro excluído'}
        except IndexError:
            mensagem = 'O ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        return response

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