import ftplib


def ftp_operations():
    # Set the URL of the FTP server you want to connect to
    URL_FTP = "ftp.gnu.org"

    # Establish a connection to the FTP server
    ftp = ftplib.FTP(URL_FTP)
    # Login to the FTP server. By default, this uses anonymous login
    ftp.login()

    # Change the current working directory on the FTP server to "/video"
    ftp.cwd("/video")
    # Get a list of filenames in the current directory
    files = ftp.nlst()

    # Loop through each file in the list of filenames
    for file in files:
        # Check if the file name ends with ".webm"
        if file.endswith(".webm"):
            # Print the file name
            print(file)
            # Open a local file in write-binary mode to save the downloaded file
            with open("./img/" + file, "wb") as download_file:
                # Retrieve the file from the FTP server and write its contents to the local file
                ftp.retrbinary("RETR " + file, download_file.write)

    # Close the connection to the FTP server
    ftp.close()


if __name__ == "__main__":
    ftp_operations()
