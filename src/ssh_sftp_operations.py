import paramiko


def ssh_sftp_operations():
    # Define SSH connection details
    hostname = "35.183.15.191"
    username = "ec2-user"
    port = 22
    key_filename = "DEMO_key.pem"

    # Load the private key for SSH authentication
    pkey = paramiko.RSAKey.from_private_key_file(key_filename)

    # Open an SFTP session over the SSH connection
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, pkey)
    sftp_client = client.open_sftp()

    # Create a new directory on the remote server
    sftp_client.mkdir("comp216")

    # Upload a local file to the newly created directory on the remote server
    sftp_client.put("sample.txt", "comp216/sample.txt")

    # Close the SSH connection
    sftp_client.close()
    client.close()


# If this script is executed directly, call the ssh_sftp_operations function
if __name__ == "__main__":
    ssh_sftp_operations()
