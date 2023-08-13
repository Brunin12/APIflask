from ..models import curso_model
from api import db


def cadastrar_curso(curso):
    curso_bd = curso_model.Curso(nome=curso.nome, descricao=curso.descricao, data_publicacao=curso.data_publicacao)
    try:
        db.session.begin()
        db.session.add(curso_bd)
        db.session.commit()
    except Exception as e:
        print(f"Erro ao adicionar curso: {str(e)}")
        db.session.rollback()  # Reverte a transação em caso de erro

    return curso_bd
