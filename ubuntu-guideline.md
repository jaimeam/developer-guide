# Ubuntu guideline <!-- omit in toc -->

- [UFW (Uncomplicated firewall)](#ufw-uncomplicated-firewall)
- [Nohup](#nohup)
- [List active processes](#list-active-processes)
- [Symbolic link](#symbolic-link)
- [Copy files via SSH command](#copy-files-via-ssh-command)

#### UFW (Uncomplicated firewall)
```
sudo ufw status
```

#### Nohup
```
nohup command-with-options &
```
Example running a Python Streamlit app
```
nohup streamlit run /usr/jaime/Project/app.py --server.port 80 > /usr/jaime/Project/app.log &
```

#### List active processes
```
ps ax
ps ax | grep <search-item>
```

#### Symbolic link
```
ln -s <source> <destination>
```

#### Copy files via SSH command
```
scp -rp <local-directory> root@<ip>:<remote-path>
```