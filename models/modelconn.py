from app import app
from flask_mysqldb import MySQL

mysql = MySQL(app)


class ClienteModel():

    def cadastrarUser():
        name = 'Livia Alves'
        email = 'liviaalves@impacta.com'
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO clientes (nome, email, telefone) VALUES(%s,%s)''',(name,email))
        mysql.connection.commit()
        cursor.close()

        return 'User cadastrado com sucesso!'