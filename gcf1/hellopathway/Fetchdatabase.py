import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'DokumentWymiany123#',
    'host': '34.118.30.55',
    'database':'webscrap1',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'C:/Users/barna/OneDrive/Programowanie/Python/GCP/gcp/gcf1/hellopathway/ssl/server-ca.pem',
    'ssl_cert': 'C:/Users/barna/OneDrive/Programowanie/Python/GCP/gcp/gcf1/hellopathway/ssl/client-cert.pem',
    'ssl_key': 'C:/Users/barna/OneDrive/Programowanie/Python/GCP/gcp/gcf1/hellopathway/ssl/client-key.pem'
}
class Fetchingdata():
    def dataFetch(self,dlx):
        self.dlx = dlx
        if self.dlx == "dlxpjvo":
            self.id = 1
        elif self.dlx == "dlxpw5n":
            self.id = 2
        elif self.dlx == "dlxpfvo":
            self.id = 3
        elif self.dlx == "dlxph6u":
            self.id = 4
        elif self.dlx == "dlxpuwr":
            self.id = 5
        elif self.dlx == "dlxpfi7":
            self.id = 6
        elif self.dlx == "dlxp7e1":
            self.id = 7
        elif self.dlx == "dlxpajc":
            self.id = 8
        elif self.dlx == "dlxpuzx":
            self.id = 9
        elif self.dlx == "dlxppnd":
            self.id = 10
        elif self.dlx == "dlxpre7":
            self.id = 11
        elif self.dlx == "dlxpt9q":
            self.id = 12
        elif self.dlx == "dlxpr54":
            self.id = 13
        elif self.dlx == "dlx0":
            self.id = 14
        elif self.dlx == "dlxpggv":
            self.id = 15
        elif self.dlx == "dlxpq08":
            self.id = 16
        elif self.dlx == "dlx1":
            self.id = 17
        elif self.dlx == "dlxpw19":
            self.id = 18
        elif self.dlx == "dlxp3wd":
            self.id = 19
        elif self.dlx == "dlx2":
            self.id = 20
        else:
            self.id = 99
  
        # now we establish our connection
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()  # initialize connection cursor
        # cursor.execute('SELECT * FROM DLX')  # create a new 'testdb' database

        cursor.execute(f"SELECT dlx, Imie, Nazwisko, Bez_pol_imie, Bez_pol_nazwisko FROM DLX WHERE id={self.id};")
        row = cursor.fetchone()
        print(row)
        self.f_dlx = row[0]
        self.f_name = row[1]
        self.f_surname = row[2]  
        self.f_non_pol_name = row[3]
        self.f_non_pol_surname = row[4]
        cnxn.close()  # close connection because we will be reconnecting to testdb
