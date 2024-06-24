from typing import Union

from fastapi import FastAPI

app = FastAPI()

vendas={
    1:{'item':'lata', 'preco_uni':2.50, 'quantidade':5},
    2:{'item':'chinelo', 'preco_uni':35.50, 'quantidade':1},
    3:{'item':'lata', 'preco_uni':2.50, 'quantidade':80},
    4:{'item':'garrafa', 'preco_uni':8, 'quantidade':4},
    5:{'item':'lata', 'preco_uni':2.50, 'quantidade':30},
    6:{'item':'lata', 'preco_uni':2.50, 'quantidade':30},
}

@app.get('/')
def home():
    return {"qtd_vendas":len(vendas), "info_vendas":vendas}


@app.get('/vendas/{id_venda}')
def get_venda(id_venda:int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {'erro':f'id da venda é inexistente.tente números entre 1 e {len(vendas)}'}