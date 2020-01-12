# biometrics_personal

#python setup
use python 3
sudo apt install python3-pip sqlite3
sudo python3 -pip install pysqlite3


# ssh setup
PC = host
android = client

Setup up DHCP reservation for the client's IP in your router's settings

client:
    install termux
    pkg upgrade
    pkg install tsu openssh
    $PREFIX/etc/ssh/sshd_config=
        PrintMotd no
        PasswordAuthentication yes
        PubkeyAcceptedKeyTypes +ssh-dss
        Subsystem sftp /data/data/com.termux/files/usr/libexec/sftp-server
    set password with passwd

host:
    cd ~/.ssh && ssh-keygen -t rsa -b 2048 -f id_rsa
    ssh-copy-id -p 8022 -i id_rsa CLIENT_IP

client:
    run pkill sshd
    run sshd

#
