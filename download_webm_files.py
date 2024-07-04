from ftplib import FTP
import os

# Define FTP server and directory
ftp_server = "ftp.gnu.org"
ftp_directory = "/video/"

# Connect to the FTP server
ftp = FTP(ftp_server)
ftp.login()  # Anonymous login

# Navigate to the specified directory
ftp.cwd(ftp_directory)

# List files in the directory
files = ftp.nlst()

# Filter for .webm files
webm_files = [file for file in files if file.endswith(".webm")]

# Create a local directory to save the files
local_directory = "downloaded_files"
os.makedirs(local_directory, exist_ok=True)

# Download each .webm file
for file in webm_files:
    local_file_path = os.path.join(local_directory, file)
    with open(local_file_path, "wb") as local_file:
        ftp.retrbinary("RETR " + file, local_file.write)

# Close the FTP connection
ftp.quit()

print(f"Downloaded {len(webm_files)} .webm files to {local_directory}")
