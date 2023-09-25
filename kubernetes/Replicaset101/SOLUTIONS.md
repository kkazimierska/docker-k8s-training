1. Run command 
```
kubectl autoscale rs web --max=5 --min=3 --cpu-percent=50
```

Verify the results
```
kubectl get horizontalpodautoscalers.autoscaling
```

2. Modify the replicaset.yaml
```
containers:
- name: testnginx
image: nginx
livenessProbe:
    exec:
        command:
            - curl
            - http://localhost
    initialDelaySeconds: 10
    periodSeconds: 5
```
