from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_service
from datetime import datetime, date


class ListaCursos(Resource):
    def get(self):
        return "Olá Mundo"

    def post(self):
        print("post enviado")
        cs = curso_schema.CursoSchema()
        validacao = cs.validate(request.json)
        if validacao:
            return make_response(jsonify(validacao), 400)
        else:

            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]
            data_publicacao = datetime.strptime(data_publicacao, "%Y-%m-%d").date()

            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)

            resultado = curso_service.cadastrar_curso(novo_curso)

            resposta = cs.jsonify(resultado)

            return make_response(resposta, 201)


api.add_resource(ListaCursos, '/cursos')
