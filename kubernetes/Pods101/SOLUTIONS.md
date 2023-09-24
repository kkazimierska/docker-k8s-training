1. Create configuration file of the webserver
```
kubectl run webserver --image=nginx --dry-run=client -o yaml > exercise1_0.yaml
```
Run webserver 
```
kubectl apply -f exercise1_0.yaml
```
Get ip address of the pod
```
kubectl get pod webserver -o wide
```

Run sh shell on crawler
```
kubectl run -it crawler --image=alpine/curl /bin/sh
```

Use curl command inside crawler pod
```
$ curl http://172.17.0.3

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
```

Clean up pods
```
kubectl delete pod webserver
kubectl delete pod crawler
```
2. 
Create initial yaml configuration
```
kubectl run producer_consumer --image=busybox --dry-run=client -o yaml > producer_consumer.yaml
```

Update specs to use the shared volume and run commands
```
spec:
  volumes:
  - name: log
    emptyDir: {}
  containers:
  - image: busybox
    name: producer
    command: ["/bin/sh", "-c"]
    args:
      - while true; do
          echo "hello" >> /var/logs/hello.txt;
          sleep 2;
        done
    resources: {}
    volumeMounts:
    - name: log
      mountPath: /var/logs/
  - image: busybox
    name: consumer
    command: ["tail", "-f", "/var/logs/hello.txt"]
    volumeMounts:
    - name: log
      mountPath: /var/logs/
    resources: {}
```
