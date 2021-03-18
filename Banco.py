import pyodbc 

# Some other example server values are
server = '.\sqlexpress' # for a named instance

database = 'gui' 
username = 'sa' 
password = '123456'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#FUNÇÕES DO BD E CONEXÃO
#######
def insert(self,nome,preco,estoque,disponibilidade):
    #Insert no banco
   count = cursor.execute("""
  INSERT INTO produto (Nome, Preco, estoque, disponibilidade) 
 VALUES ('{}',{},{},{})""".format(nome,preco,estoque,disponibilidade)).rowcount
   cnxn.commit()
   print('Rows inserted: ' + str(count))

def selectid(id_prod):
    #Select por ID
    cursor.execute("select * from produto where id_prod = {}".format(id_prod))
    row = cursor.fetchone()
    if row:
        print("ID = " + str(row[0]) + " Nome="+ str(row[1]), " Preco= " + str(row[2]), "Disponibilidade = " + str(row[4]))


def select():
      #Select da tabela Produto completa
    cursor.execute("SELECT * from produto") 
    row = cursor.fetchone() 
    while row: 
       print("ID = " + str(row[0]) + " Nome="+ str(row[1]), " Preco= " + str(row[2]), "Disponibilidade = " + str(row[4]))
       row = cursor.fetchone()


def alterPlus(id_prod, quantidade):
      #Soma de produtos comprados ao sistema    
    soma = cursor.execute('Select estoque from produto where id_prod = {}'.format(id_prod)).fetchone()
    quantFim = int(quantidade) + int(soma[0])
    cursor.execute("UPDATE produto SET estoque = {} WHERE id_prod ={};".format(quantFim, id_prod)).rowcount
    cnxn.commit()
    


def alter(id_prod, quantidade):
      #Subtração de produtos vendidos do sistema
    soma = cursor.execute('Select estoque from produto where id_prod = {}'.format(id_prod)).fetchone()
    quantidade = int(soma[0]) - int(quantidade) 
    cursor.execute("UPDATE produto SET estoque= {} WHERE id_prod={};".format(quantidade, id_prod))
    cnxn.commit()
