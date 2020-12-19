# NGINX guideline <!-- omit in toc -->

Configuring NGINX in Ubuntu

- [Cheathseet](#cheathseet)
    - [Location](#location)
    - [Show status](#show-status)
    - [Start, stop, restart](#start-stop-restart)
    - [View logs](#view-logs)
- [Configuration files](#configuration-files)
    - [Reverse proxy](#reverse-proxy)
    - [Generate CSR files](#generate-csr-files)
- [Sources](#sources)

## Cheathseet

#### Location
```
/etc/nginx
```

#### Show status
```
systemctl status nginx
```

#### Start, stop, restart
```
systemctl stop nginx
systemctl start nginx
systemctl restart nginx
```

#### View logs
```
journalctl -u nginx
```

## Configuration files

#### Reverse proxy
```
http {
    server {
        listen 0.0.0.0:80;
        listen [::]:80;

        server_name mydomain.com;

        location / {
            proxy_pass http://localhost:9999/;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

#### Generate CSR files

```
openssl req -new -newkey rsa:2048 -nodes -keyout <yourdomain>.key -out <yourdomain>.csr
```

## Sources
- https://www.devdungeon.com/content/nginx-tutorial
- https://www.nginx.com/resources/wiki/start/
- https://www.thesslstore.com/knowledgebase/ssl-install/nginx-ssl-installation/
- https://medium.com/@munteanu210/how-to-install-an-ssl-certificate-on-nginx-b1dd39a4628d