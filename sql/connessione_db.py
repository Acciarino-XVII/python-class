import oracledb

#connessione al db local host
def connect_localhost():
    conn = oracledb.connect(
         user='SYS',
        password='airmax95', 
        dsn='localhost:1521/xe',
        mode=oracledb.AUTH_MODE_SYSDBA
        )

    print(conn)
    return conn

def close_localhost():
    connect_localhost().close()
    print("connessione chiusa")

#creare un cursore per poter eseguire comandi nel db
def cursore():
    cursor = connect_localhost().cursor()
    return cursor


# cursore = cursore()
# cursore.execute("""
#                 CREATE TABLE anagrafica( nome VARCHAR2(20), cognome VARCHAR2(20), data_nascita DATE) """)
# #ESITO CONNESSIONE
# print("tabella creata")

#chiudo òa cpnnessione al db
# connection.close()
cursore = oracledb.cursor()
#chiudo il cursore
close_localhost()


