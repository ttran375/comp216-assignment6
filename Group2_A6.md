# Lab 6

## Introduction

## Setting Up SSH Connection

1. **Open Terminal and Navigate to Key File Location**
2. **Show SSH Key File**
3. **Initiate SSH Connection**

```python
import paramiko

hostname = "35.183.15.191"
username = "ec2-user"
port = 22
key_filename = "DEMO_key.pem"

pkey = paramiko.RSAKey.from_private_key_file(key_filename)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("ssh connecting")
client.connect(hostname=hostname, port=port, username=username, pkey=pkey)
print("ssh connected")
```

    ssh connecting
    ssh connected

5. **Verify SSH Connection**

```python
stdin, stdout, stderr = client.exec_command("ls")
print(stdout.readlines())
```

    ['comp216\n']

## Creating Directory and File Transfer Using SFTP

1. **Open SFTP Client**
2. **Create a Directory**
3. **Verify Directory Creation**

```python
sftp_client = client.open_sftp()
print(sftp_client.listdir())
```

    ['.bash_logout', '.bash_profile', '.bashrc', '.ssh', '.viminfo', '.bash_history']

```python
sftp_client.mkdir('comp216')
```

```python
print(sftp_client.listdir())
```

    ['.bash_logout', '.bash_profile', '.bashrc', '.ssh', '.viminfo', '.bash_history', 'comp216']

4. **Upload a File**

```python
localFilePath = 'sample.txt'
remoteFilePath = 'comp216/sample.txt'

try:
      sftp_client.put(localFilePath, remoteFilePath)
except FileNotFoundError as err:
      print(f"File {localFilePath} was not found on the local system")
```

5. **Verify File Upload**

```python
print(sftp_client.listdir('comp216'))
```

    ['sample.txt']

6. **Close SFTP and SSH Connections**

```python
sftp_client.close()
client.close()
```
