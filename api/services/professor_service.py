from ..models import professor_model
from api import db


def cadastrar_professor(professor):
    professor_bd = professor_model.Professor(nome=professor.nome, idade=professor.idade)
    try:
        db.session.begin()
        db.session.add(professor_bd)
        db.session.commit()
    except Exception as e:
        print(f"Erro ao adicionar professor: {str(e)}")
        db.session.rollback()  # Reverte a transação em caso de erro

    return professor_bd

def listar_professor():
    return professor_model.Professor.query.all()

def listar_professor_id(id):
    return professor_model.Professor.query.filter_by(id=id).first()

def atualiza_professor(professor_anterior, professor_atualizado):
    professor_anterior.nome = professor_atualizado.nome
    #professor_anterior.formacao = professor_atualizado.formacao
    professor_anterior.idade = professor_atualizado.idade
    db.session.commit()

def remove_professor(professor):
    db.session.delete(professor)
    db.session.commit()