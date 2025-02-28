import oracledb

conn = oracledb.connect(
    user='SYS',
    password='airmax95', 
    dsn='localhost:1521/xe',
    mode=oracledb.SYSDBA
    )

cursore = conn.cursor()

# Nome della tabella da verificare
nome_tabella = "TB_ESE4_ANAG"

# Verifica se la tabella esiste
cursore.execute("""
    SELECT COUNT(*) 
    FROM user_tables 
    WHERE table_name = :nome_tabella
""", nome_tabella=nome_tabella)


if cursore.fetchone()[0] == 0:
    cursore.execute("""
        CREATE TABLE TB_ESE4_ANAG(
                    COD_DIP NUMBER(10) NOT NULL,
                    COGNOME VARCHAR2(50) NOT NULL,
                    NOME VARCHAR2(50) NOT NULL,
                    DATA_NASC DATE NOT NULL,
                    COD_UFF CHAR(3) NOT NULL)
                    """)

    print("tabella creata con successo! ")
else:
    print("la tabella esiste già!")


query = "INSERT INTO TB_ESE4_ANAG (COD_DIP, COGNOME, NOME, DATA_NASC, COD_UFF) VALUES (:1, :2, :3, TO_DATE(:4, 'DD-MM-YYYY'), :5 )"

valori = [
    (1, 'RUSSO', 'DIEGO', '23/01/1980', 'A01' ),
    (2, 'DE FAZI', 'PAOLO', '04-07-1977', 'A02'),
    (3, 'MAINO', 'ANDREA', '19-09-1975', 'A04'),
    (4 , 'CALIENDO', 'DAVIDE', '31-12-1978', 'A05'),
    (5, "DELLANNO", 'ALBERTO', '09-11-1967', 'A01')
]

cursore.executemany(query, valori)
print("daje de pe foh")
cursore.commit()

cursore.execute(f"TRUNCATE TABLE {nome_tabella}")