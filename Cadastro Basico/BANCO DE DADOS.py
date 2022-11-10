#create_db.py
import sqlite3
conn = sqlite3.connect ('clientes.db')




# create_schema.py
import sqlite3

conn= sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    CPF VARCHAR(11) NOT NULL,
    primeiro nome TEXT NOT NULL,
    nome do meio TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    idade INT,
    conta INT,
    criado_em DATE NOT NULL
);
""") 

print('tabela criada com sucesso.')

conn.close()

# create_data_nrecords.py
import sqlite3 
conn = sqlite3.connect('clientes.db')
cursos = conn.cursor()

lista = [
        
    ('125.421.431-61', 'Yudagufe' ,'Conujfafe','Xowehihe', '73', '0'),
    ('473.978.578-92', 'Vibugudagibo' ,'vazio', 'Kulolic', '116', '1'),
    ('293.541.970-86', 'Wedovu' ,'vazio', 'Zezanuwoziw', '36', '2'),
    ('175.090.731-20', 'Fabhuhuboqu', 'vazio', 'Feketueb', '27', '3'),
    ('731.416.865-72', 'Xeluhedelaya' ,'vazio', 'Layvu', '113', '4',),
    ('642.375.674-51','Zegiyaci', 'vazio', 'Zovequteyi', '87', '5'),
    ('298.921.503-17', 'Bucenaqui', 'vazio', 'Voj', '37', '6'),
    ('030.293.700-70', 'Zoskexaqui', 'vazio', 'Kuliko', '23', '7'),
    ('028.844.121-66','Quavanenau', 'vazio', 'Xidixacixi', '41','8'),
    ('158.123.787-03','Vakaxu', 'vazio' ,'Gani' ,'37', '9'),
    ('531.815.168-30', 'Kodeba','vazio', 'Giwe' ,'31', '10'),
    ('575.964.832-67', 'Quiko' ,'vazio' ,'Mulu' ,'36' ,'11'),
    ('537.811.900-99', 'Dafidfkuto', 'vazio', 'Laqxaloxiyi', '80', '12'),
    ('526.275.698-56', 'Cici', 'vazio' ,'Equima', '35', '13'),
    ('856.543.480-35', 'Wucibxzevi', 'vazio', 'Dud', '38', '14'),
    ('992.347.662-53', 'Duta', 'vazio', 'Ninibanobo', '48', '15'),
    ('824.776.970-05', 'Voo', 'vazio', 'Zeko', '35', '16'),
    ('538.643.202-40', 'Yelivhaque', 'vazio', 'Cumu', '41', '17'),
    ('409.372.682-32', 'Guyiona', 'vazio', 'Miqua', '83', '18'),
    ('437.200.007-02', 'Lebuque', 'vazio', 'Eceghuvey', '86', '19'),
    ('540.381.079-57', 'Xehuhonkozo', 'vazio', 'Yeyeggu', '56', '20'),
    ('892.326.356-23', 'Xuquehubida', 'vazio', 'Yecelaxun','21', '25'),
    ('237.599.259-60', 'Lolovaf', 'vazio', 'Velugagileyi' ,'38', '26'),
    ('085.428.968-15', 'Huwihuewwe', 'vazio', 'Zixanixezi', '35', '27'),
    ('728.955.598-99', 'Bene', 'vazio', 'Cemo', '51', '28'),
    ('288.177.937-44', 'Cuho','vazio', 'Yeyuqui', '116', '29'),
    ('837.819.612-06', 'Mikbeiho', 'vazio', 'Zeco', '35', '30'),
    ('463.711.414-06', 'Cane', 'vazio', 'Dielegical', '111', '31'),
    ('376.683.123-90', 'Mikebifecode', 'vazio', 'Lozoneheteo', '89', '32'),
    ('692.156.001-16', 'Botiqueglole', 'vazio', 'Tiquavwao', '76', '33'),
    ('320.719.131-16', 'Beebikhi', 'vazio', 'Lonun', '117', '34'),
    ('700.212.708-13', 'Wuwienaza', 'vazio', 'Noximagi','47', '35'),
    ('894.922.557-07', 'Zeno', 'vazio', 'Tulwej', '110', '36'),
    ('485.520.763-57', 'Cefive', 'vazio', 'Lehi', '76', '37'),
    ('739.559.728-01', 'Yoj', 'vazio', 'Mezimudefa', '40','38'),
    ('564.334.403-39', 'Totacuyagi', 'vazio', 'Yahohafoha', '101', '39'),
    ('259.766.232-71', 'Luy', 'vazio','Quitocuya', '72', '40'),
    ('045.397.473-63', 'Fateya', 'vazio', 'Zewaoloku', '71', '41'),
    ('936.839.094-80', 'Kaehebabana', 'vazio', 'Yicifi', '62', '42'),
    ('620.478.832-45', 'Vumoc','vazio', 'Yonifefuku', '68', '43'),
    ('801.436.494-26', 'Wugijduque', 'vazio', 'Vedulemewe', '102', '44'),
    ('024.810.465-95', 'Tinoto', 'vazio', 'Yivo', '45', '45'),
    ('351.642.333-63', 'Qutu', 'vazio', 'Wobekolemue', '108', '46'),
    ('315.731.264-89', 'Zayodiquigi', 'vazio' ,'Leem', '88', '47'),
    ('743.151.892-19', 'Guwohaza', 'vazio','Bekobeda', '81', '48'),
    ('828.387.471-42', 'Xoktelobfe', 'vazio', 'Nuwabuen', '119', '49'),
    ('175.751.598-27', 'Xawoyejbavu', 'vazio', 'Zamufowwezo', '111', '50'),
    ('509.391.350-78', 'Ziexugefiti', 'vazio', 'Yuquahevina', '63', '51'),
    ('554.301.680-76', 'Iquika', 'vazio', 'Dugiquayu', '59', '52'),
    ('734.390.093-43', 'Hofihe', 'vazio', 'Lajyafaxi', '73', '53'),
    ('611.138.736-20', 'Uvecuziboo', 'vazio', 'Hojnece', '35', '54'),
    ('937.071.704-03', 'Mavimaheque','vazio', 'Tugo', '104', '55'),

]


cursor.executemany("""
insert INTO Clientes (CPF, primeironome, nomedomeio, sobrenome, idade, conta, 
VALUES(?,?,?,?,?,?,?)
""", lista)

conn.commit()
print('dados inseridos com sucesso.')
conn.close()

# read_data.py
import sqlite3


conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)

    conn.close()

# update_data.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

id_cliente = 1 
novo_CPF = '070.857.484-84'
novo_criado_em = '2022-03-11'

cursor.execute("""
 UPDATE clientes 
 SET fone = ?, criado_em = ? 
 WHERE id = ?
 """, (novo_CPF, novo_criado_em, id_cliente))

conn.commit()

print('dados atualizados com sucesso.')
conn.close()

#delete_data.py

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

id_clientes = 8 

cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

conn.commit()

print('registro excluido com sucesso.')

conn.close()

# inserir_nova_coluna.py

import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE clientes 
ADD COLUMN bloqueado BOOLEAN;
""" )

conn.commit()

print('novo campo adicionado com sucesso.')

conn.close()

#view_tabela_info.py 
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
nome_tabela = 'clientes'

cursor.execute('PRAGMA table_info({})'.format(nome_tabela))

colunas = [tupla[1] for tupla in cursor.fetchall()]
print('colunas:', colunas)

cursor.execute("""
SELECT nome FROM sqlite_master WHERE type='table' ORDER BY nome 
""")

print('tabelas:')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

    cursor.execute("""
    SELECT sql FROM sqlite_master WHERE type='table' AND namee=?
    """, (nome_tabela,))

    print('schema:')
    for schema in cursor.fetchall():
        print("%s" % (schema))

        conn.close()

conn.close()


#create_db.py
import sqlite3
conn = sqlite3.connect ('conta.db')


# create_schema.py
import sqlite3

conn= sqlite3.connect('conta.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE conta (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    agencia  VARCHAR(11) NOT NULL,
    numero INT,
    saldo  INT, 
    gerente TEXT NOT NULL,
    titular TEXT NOT NULL,
);
""") 

print('tabela criada com sucesso.')

conn.close()

# create_data_nrecords.py 
import sqlite3 
conn = sqlite3.connect('conta.db')
cursos = conn.cursor()

lista = [

    ('8725-2', '94710-3', '1951263.61', '651', '0'),
    ('2579-5', '90521-5', '2317241.77', '1299', '1'),
    ('6064-8', '88052-9', '3660008.36', '498', '2'),
    ('8896-0', '31308-9', '6519218.53', '694', '3'),
    ('4652-5', '12874-0', '4700472.37', '887', '4'),
    ('7837-3', '45293-5', '3645410.01', '518', '5'),
    ('1648-6', '08385-2', '917172.29',  '285', '6'),
    ('3180-3', '83881-2', '8724734.86', '1396', '7'),
    ('1587-8', '88719-7', '5308101.05', '1108', '8'),
    ('1202-2', '21287-3', '5390638.92', '1408', '9'),
    ('5597-3', '62386-7', '1108190.64', '1495', '10'),
    ('3576-6', '77918-2', '8040499.31', '1267', '11'),
    ('5851-2', '29090-4', '9952517.75', '1445', '12'),
    ('0810-6', '74568-2', '3186744.09', '1134', '13'),
    ('1975-4', '48067-5', '1677826.49', '643', '14'),
    ('5467-1', '67138-2', '4281225.55', '1202', '15'),
    ('1956-4', '49756-1', '5431389.44', '8', '16'),
    ('3420-8', '20770-0', '9787425.48', '1315', '17'),
    ('8159-9', '22237-0', '7121779.21', '526', '18'),
    ('6175-7', '07600-2', '3250917.85', '1016', '19'),
    ('4219-5', '64149-3', '5480497.51', '508', '20'),
    ('2914-5', '42471-1', '1403363.24', '735', '21'),
    ('8786-8', '01266-7', '9534659.43', '1045', '22'),
    ('0272-7', '67201-3', '2576019.57', '849', '23'),
    ('4911-5', '82957-0', '5452475.52', '1191', '24'),
    ('1164-7', '53208-6', '6112063.88', '1309', '25'),
    ('6678-1', '41094-1', '5844912.25', '678', '26'),
    ('3872-7', '99816-5', '5341102.93', '1040', '27'),
    ('4645-4', '84314-2', '1082454.38', '1136', '28'),
    ('6980-2', '83540-4', '3752742.92', '329', '29'),
    ('3283-7', '48326-2', '9961831.62', '664', '30'),
    ('4448-4', '32836-2', '580832.52', '666', '31'),
    ('8544-5', '67185-9', '9229239.17', '371', '32'),
    ('4715-9', '26062-1', '2042526.85', '357', '33'),
    ('2090-3', '87702-4', '1071512.11', '852', '34'),
    ('6291-9', '42665-6', '9970801.91', '274', '35'),
    ('6331-3', '20802-1', '5154231.07', '920', '36'),
    ('3524-0', '70395-8', '9081197.43', '725', '37'),
    ('8341-9', '60865-1', '3146724.05', '552', '38'),
    ('2757-5', '81164-4', '1375148.12', '747', '39'),
    ('6619-8', '11987-4', '6122244.03', '1282', '40'),
    ('2631-2', '37962-5', '5584609.29', '827', '41'),
    ('0341-5', '21438-9', '4987267.12', '235', '42'),
    ('0378-3', '72816-2', '5436777.46', '739', '43'),
    ('8251-4', '51681-8', '7423358.86', '1181', '44'),
    ('3560-2', '53878-1', '6456818.84', '1310', '45'),
    ('9600-0', '91768-6', '5690226.21', '281', '46'),
    ('8606-6', '22758-7', '1776962.94', '847', '47'),
    ('1192-6', '05336-5', '5774104.35', '462', '48'),
    ('8483-4', '68436-2', '8310137.39', '690', '49'),
    ('0553-6', '63952-4', '7678302.09',  '1', '50'),
    ('7011-8', '46421-0', '269124.41', '1054', '51'),
    ('1378-5', '26809-2', '9845509.86', '768', '52'),
    ('0964-4', '44521-7', '3608151.73', '1034', '53'),
    ('5082-7', '04652-0', '9943127.02', '279', '54'),
    ('0182-0', '36162-7', '7236201.97', '1049', '55'),
]
    
    
cursor.executemany("""
    insert INTO Conta (agencia, numero, saldo, gerente, titular)
VALUES(?,?,?,?,?,?,?)
""",lista)

conn.commit()
print('dados inseridos com sucesso.')

conn.close()
 
# read_data.py
import sqlite3


conn = sqlite3.connect('conta.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM conta;
""")

for linha in cursor.fetchall():
    print(linha)

    conn.close()

# update_data.py
import sqlite3

conn = sqlite3.connect('conta.db')
cursor = conn.cursor()

id_conta = 1 
novo_titular = 'luis victor'
novo_criado_em = '2022-03-11'

cursor.execute("""
 UPDATE conta 
 SET fone = ?, criado_em = ? 
 WHERE id = ?
 """, (novo_titular, novo_criado_em, id_conta))

conn.commit()

print('dados atualizados com sucesso.')
conn.close()

#delete_data.py

import sqlite3

conn = sqlite3.connect('conta.db')
cursor = conn.cursor()

id_conta = 8 

cursor.execute("""
DELETE FROM conta
WHERE id = ?
""", (id_conta,))

conn.commit()

print('registro excluido com sucesso.')

conn.close()

# inserir_nova_coluna.py

import sqlite3

conn = sqlite3.connect('conta.db')
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE conta 
ADD COLUMN bloqueado BOOLEAN;
""" )

conn.commit()

print('novo campo adicionado com sucesso.')

conn.close()

#view_tabela_info.py 
import sqlite3

conn = sqlite3.connect('conta.db')
cursor = conn.cursor()
nome_tabela = 'conta'

cursor.execute('PRAGMA table_info({})'.format(nome_tabela))

colunas = [tupla[1] for tupla in cursor.fetchall()]
print('colunas:', colunas)

cursor.execute("""
SELECT nome FROM sqlite_master WHERE type='table' ORDER BY nome 
""")

print('tabelas:')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

    cursor.execute("""
    SELECT sql FROM sqlite_master WHERE type='table' AND namee=?
    """, (nome_tabela,))

    print('schema:')
    for schema in cursor.fetchall():
        print("%s" % (schema))

        conn.close()

conn.close()

