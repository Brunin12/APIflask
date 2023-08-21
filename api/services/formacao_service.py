from ..models import formacao_model
from api import db


def cadastrar_formacao(formacao):
    formacao_bd = formacao_model.Formacao(nome=formacao.nome, descricao=formacao.descricao, formacao=curso.formacao)
    try:
        db.session.begin()
        db.session.add(formacao_bd)
        db.session.commit()
    except Exception as e:
        print(f"Erro ao adicionar formacao: {str(e)}")
        db.session.rollback()  # Reverte a transação em caso de erro

    return formacao_bd

def listar_formacoes():
    return formacao_model.Formacao.query.all()

def listar_formacao_id(id):
    return formacao_model.Formacao.query.filter_by(id=id).first()

def atualiza_formacao(formacao_anterior, formacao_atualizada):
    formacao_anterior.nome = formacao_atualizada.nome
    formacao_anterior.formacao = formacao_atualizada.formacao
    formacao_anterior.descricao = formacao_atualizada.descricao
    db.session.commit()

def remove_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()