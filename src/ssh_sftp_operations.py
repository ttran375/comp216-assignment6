import paramiko


def ssh_sftp_operations():
    # Define the hostname (IP address of the server)
    hostname = "35.183.15.191"
    # Define the username to use for SSH connection
    username = "ec2-user"
    # Define the port for SSH connection (default SSH port is 22)
    port = 22
    # Specify the path to the private key file for authentication
    key_filename = "DEMO_key.pem"

    # Load the private key from the specified file
    pkey = paramiko.RSAKey.from_private_key_file(key_filename)

    # Create an SSH client object
    client = paramiko.SSHClient()
    # Set the policy to add the server's SSH key automatically if it's missing
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Establish an SSH connection to the server
    client.connect(hostname, port, username, pkey)

    # Open an SFTP session over the established SSH connection
    sftp_client = client.open_sftp()
    # Create a new directory on the remote server
    sftp_client.mkdir("comp216")
    # Upload a file from the local system to the newly created directory on the remote server
    sftp_client.put("sample.txt", "comp216/sample.txt")

    # Close the SFTP session
    sftp_client.close()
    # Close the SSH connection
    client.close()


# Execute the ssh_sftp_operations function if this script is run directly
if __name__ == "__main__":
    ssh_sftp_operations()
