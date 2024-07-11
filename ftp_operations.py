import ftplib


def ftp_operations():
    URL_FTP = "ftp.gnu.org"

    ftp = ftplib.FTP(URL_FTP)
    ftp.login()

    ftp.cwd("/video")
    files = ftp.nlst()

    for file in files:
        if file.endswith(".webm"):
            print(file)
            with open("./img/" + file, "wb") as download_file:
                ftp.retrbinary("RETR " + file, download_file.write)

    ftp.close()


if __name__ == "__main__":
    ftp_operations()
