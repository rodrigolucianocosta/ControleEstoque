# ControleEstoque
controle de estoque web

 problema encontrado: Mudanca da base de SQLite para mysql

solução
Upgrade pip version
sudo pip install pip --upgrade

Construção das dependencias para python-mysqldb libraries
sudo apt-get build dep python-mysqldb

Instalação Python Mysql Libraires
sudo pip install MySQl-python

criação da database controleEstoque01

create user 'usuario' by 'password'

grant all  on nomebase.* to usuario'@'%';

flush privileges; 

