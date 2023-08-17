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

def listar_cursos():
    return curso_model.Curso.query.all()

def listar_cursos_id(id):
    return curso_model.Curso.query.filter_by(id=id).first()

def atualizar_curso(curso_anterior, curso_atualizado):
    curso_anterior.nome = curso_atualizado.nome
    curso_anterior.descricao = curso_atualizado.descricao
    curso_anterior.data_publicacao = curso_atualizado.data_publicacao
    db.session.commit()

def remover_curso(curso):
    db.session.delete(curso)
    db.session.commit()