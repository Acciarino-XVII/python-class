import oracledb
#connessione al db
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
    FROM TB_ESE4_ANAG
    WHERE table_name = :nome_tabella
""", nome_tabella=nome_tabella)


if cursore.fetchone()[0] == 0:  #controllo creazione tabella
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

values_anag = [
    (1, 'RUSSO', 'DIEGO', '23/01/1980', 'A01' ),
    (2, 'DE FAZI', 'PAOLO', '04-07-1977', 'A02'),
    (3, 'MAINO', 'ANDREA', '19-09-1975', 'A04'),
    (4 , 'CALIENDO', 'DAVIDE', '31-12-1978', 'A05'),
    (5, "DELLANNO", 'ALBERTO', '09-11-1967', 'A01')
]

cursore.executemany(query, values_anag)
cursore.commit()

print("tabella committata sul db")


#TOGLIE TUTTI GLI ELEMENTI DALLA TABELLA

#Aggiornare la tabella

query = "UPDATE TB_ESE4_ANAG SET COD_UFF = 'A01' WHERE EXTRACT(YEAR FROM DATA_NASC) BETWEEEN '1974' AND '1976')"
cursore.execute(query)
cursore.commit()

query = "UPDATE TB_ESE4_ANAG SET COD_UFF = 'A02' WHERE EXTRACT(YEAR FROM DATA_NASC) BETWEEEN '1978' AND '1979')"
cursore.execute(query)
cursore.commit()


#creazione della tabella TB_ESE4_PRODOTTI nel DB

nome_tabella = "TB_ESE4_PRODOTTI"

cursore.execute("""
    SELECT COUNT(*) 
    FROM TB_ESE4_PRODOTTI
    WHERE table_name = :nome_tabella
""", nome_tabella=nome_tabella)


if cursore.fetchone()[0] == 0:  #controllo creazione tabella
    cursore.execute("""
    CREATE TABLE TB_ESE4_PRODOTTI (
        COD_PROD NUMBER(10) NOT NULL,
        FORNITORE VARCHAR2(50) NOT NULL,
        P_IVA VARCHAR2(7) NOT NULL,
        LOTTO VARCHAR2(3) NOT NULL,
        DATA_ULTIMO_SCARICO DATE NOT NULL
    )
    """)

    print("tabella creata con successo! ")
else:
    print("la tabella esiste già!")
    
    values_tb_prod = [
    (1, "BARILLA", "IT00276", "24-08-2023", "A01"),
    (2, "NESTLE", "IT00496", "14-06-2024", "B02"),
    (3, "BAULI", "IT00866", "18-10-2022", "C04"),
    (4, "KELLOGS", "IT00127", "31-12-2023", "D05"),
    (5, "RANA", "IT00111", "29-04-2024", "E02")
]

query = "INSERT INTO TB_ESE4_ANAG (COD_PROD, FORNITORE, P_IVA, LOTTO, DATA_ULTIMO_SCARICO) VALUES (:1, :2, :3, TO_DATE(:4, 'DD-MM-YYYY'), :5 )"

cursore.executemany(query, values_tb_prod)
cursore.commit()


print("ora effettuo la select")

cursore.execute("""
                SELECT *
                FROM TB_ESE4_PROD
                """)

risultato= cursore.fetchall() # restuisce una lista

#aggiornare tabella
cursore.execute("""
                UPDATE TB_ESE4_PRODOTTI
                SET LOTTO = 'A00'
                WHERE NOME LIKE 'B%'
                """)


#truncate table
cursore.execute(f"TRUNCATE TABLE {nome_tabella}")