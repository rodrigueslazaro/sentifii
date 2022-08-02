#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Object-relational mapping

from peewee import BooleanField, CompositeKey, DateField, ForeignKeyField, \
    IntegerField, Model, SQL, SqliteDatabase, TextField, FloatField

# TODO: Check options to increase performance
DATABASE = SqliteDatabase('dados.db')

class BaseModel(Model):
    '''
    Base ORM class
    '''

    def get_dict(self):
        '''
        Return data dictionary
        '''
        return self.__data__

    class Meta:  # pylint: disable=too-few-public-methods
        '''
        Connection database
        '''
        database = DATABASE

class Segmento(BaseModel):

    # Segmento

    class Meta:
        table_name = "segmentos"

    id = IntegerField()
    nome = TextField()

class Ativo(BaseModel):

    # Ativos

    class Meta:
        table_name = "ativos"

    id = TextField()
    nome = TextField()
    razao_social = TextField()
    segmento = ForeignKeyField(Segmento, backref="ativos")

class Fundo(BaseModel):

    # Fundo

    class Meta:
        table_name = "fundos"

    id = TextField()
    ativo = ForeignKeyField(Ativo, backref="fundos")
    ffo_yield = FloatField()
    div_yield = FloatField()
    p_valorpatr = FloatField()
    div_cota = FloatField()
    valorpatr = FloatField()
    ffo_cota = FloatField()
    receita12 = FloatField()
    venda12 = FloatField()
    ffo12 = FloatField()
    rend_distr12 = FloatField()
    receita3 = FloatField()
    venda3 = FloatField()
    rend_distr3 = FloatField()
    ffo3 = FloatField()

class Provento(BaseModel):

    # Provento

    class Meta:
        table_name = "proventos"

    id = IntegerField()
    fundo = ForeignKeyField(Fundo, backref="proventos")
    data_base = DateField()
    data_pagamento = DateField()
    valor = FloatField()

class Cotacao(BaseModel):

    # Cotação

    class Meta:
        table_name = "cotacoes"

    id = DateField()
    fundo = ForeignKeyField(Fundo, backref="cotacoes")
    valor = FloatField()
    maior_cota = FloatField()
    menor_cota = FloatField()
    vol_medio = FloatField()
    num_cotas = IntegerField()
    valor_mercado = FloatField()

class Balanco(BaseModel):

    # Balanco Patrimonial

    class Meta:
        table_name = "balancos"

    id = DateField()
    fundo = ForeignKeyField(Fundo, backref="balancos")
    ativos = FloatField()
    patrimonio_liq = FloatField()

class Composicao(BaseModel):

    # Composicao

    class Meta:
        table_name = "composicoes"

    id = DateField()
    fundo = ForeignKeyField(Fundo, backref="balancos")
    cri = FloatField()
    fii = FloatField()
    acoes = FloatField()
    caixa = FloatField()
    imoveis = FloatField()

class Caracteristica(BaseModel):

    # Caracteristica do imovel

    class Meta:
        table_name = "caracteristicas"

    id = IntegerField()
    caracteristica = TextField()

class Imovel(BaseModel):

    # Imovel

    class Meta:
        table_name = "imoveis"

    id = IntegerField()
    fundo = ForeignKeyField(Fundo, backref="imoveis")
    caracteristica = ForeignKeyField(Caracteristica, backref="imoveis")
    nome = IntegerField()
    unidades = IntegerField()
    porcent_imoves = FloatField()
    area = FloatField()
    taxa_ocupacao = FloatField()
    preco_metro = FloatField()
    rate = FloatField()
    vacancia = FloatField()
    endereco = TextField()

DATABASE.connect()
DATABASE.create_tables([Fundo, Ativo, Segmento, Provento, Cotacao,
                  Balanco, Composicao, Caracteristica, Imovel])

cara = Caracteristica(id=10, caracteristica="papel")
cara.save()
