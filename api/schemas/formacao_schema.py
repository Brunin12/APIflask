from api import ma
from ..models import formacao_model
from marshmallow import fields
from ..schemas import curso_schema

class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = formacao_model.Formacao
        load_instance = True
        fields = ("id", "nome", "descricao", "cursos")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    cursos = fields.List(fields.Nested(curso_schema.CursoSchema, only=('id', 'nome')))
    