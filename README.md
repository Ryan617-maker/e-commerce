# projeto flask
pastas 
mercado.db dentro da pasta instance
dentro da pasta mercado:initi.py,mercado.py e routes.py
ainda dentro da pasta mercado tem o templates tem:base.html,home.html e produtos.html


MERCADO.PY

from mercado import db
from mercado import app
app.app_context().push()
db.create_all()

Para criar o banco de dados de acordo com o codigo de
mercado.py executar esse comando no terminal do
vscode

python
from mercado import db
from mercado import app
app.app_contexto().push()
db.create_all()

proximo passo

>>> from mercado import app
>>> from mercado import db
>>> app.app_context().push()
>>> from mercado.models import User, Item

Criando agora os registro para cada uma das tabelas do nosso programa, entao abrindo o terminal
execute python e logo apos os comando a seguir


INTERAGINDO COM AS TABELAS

>>> user1 = User(usuario="fulano", email="fulano@@email.com", senha="123456", valor=1000)
>>> db.session.add(user1)
>>> db.session.commit()

Criando os registros

>>> i1 = Item(nome="Churrasqueira Elétrica", preco=300, cod_barra="43354353", descricao="Objeto muito bom")
>>> db.session.add(i1)
>>> db.session.commit()
>>> import os
>>> os.system('cls')

link abaixo do slide completo pra fazer o projeto

https://docs.google.com/presentation/d/1YwZO3e7W_PHHsrPcuNSf8nh9VCbc_rhl1ZyeeHAw_6I/edit?usp=classroom_web&authuser=0
https://drive.google.com/file/d/1eGmOait_vfgfPgiwZIctIjb7X7Xmp7iW/view?usp=classroom_web&authuser=0
