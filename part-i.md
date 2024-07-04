# Lab 6 – Interacting with a Remote System

It is important for networking to interact with remote systems.

## Exercise – Download files via FTP

Write a Python script to use FTP to download files to a local drive. The
remote ftp site is [ftp.gnu.org](ftp://ftp.gnu.org) and develop an
efficient manner to find and retrieve all .webm files from the
[Video](ftp://ftp.gnu.org/video/) directory.

**Exercise – SSH with Cloud Services:**

As a preliminary exercise to explore cloud computing (Amazon Web
Services – AWS), create an AWS account, then configure and run a Virtual
Machine (VM) on AWS Lightsail. Follow the following tutorial: [Launch a
Linux VM with Amazon
Lightsail](https://aws.amazon.com/getting-started/hands-on/launch-a-virtual-machine/).
Ensure to create and download the SSH Key Pair during the configuration.

Write a Python script to use SSH and SFTP to create a Document directory
and upload a sample text file to the AWS Lightsail VM. Note: The
implementation requires the [Paramiko
library](https://www.paramiko.org/) and SSH Key Pair configuration
between the AWS Lightsail VM and the local machine.

For additional information, please refer to:

- [Manage SSH key pairs and connect to your Lightsail
    instances](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-ssh-in-amazon-lightsail.html)

- [Connect to your Lightsail Linux/Unix-based instance using the SSH
    command](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-ssh-using-terminal.html)

- [Connect to your Lightsail Linux instance using
    SFTP](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-connecting-to-linux-unix-instance-using-sftp.html)

Upload a recording demonstrating the SSH connectivity and file transfer.

**Due:**

See course shell.

***Submission***

1. You must use only the libraries that are available in the standard
    Python distribution (unless specified by the instructor).

2. Your code file will be named
    group\_«your_group_number»\_remote_systems.py e.g., group_1\_
    remote_systems.py.

3. Must be uploaded to course dropbox before the deadline.

4. See schedule for due date.

***Rubrics***

See requirements above.
