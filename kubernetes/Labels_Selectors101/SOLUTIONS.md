1. Create 2 pods with names nginx1,nginx2. All of them should have the label app=v1

```
kubectl run nginx1 --image=nginx --restart=Never --labels=app=v1
kubectl run nginx2 --image=nginx --restart=Never --labels=app=v1
```

2. Change the labels of pod 'nginx2' to be app=v2
```
kubectl label po nginx2 app=v2 --overwrite
```

3. Get only the 'app=v2' pods
```
kubectl get po -l app=v2
# or
kubectl get po -l 'app in (v2)'
# or
kubectl get po --selector=app=v2
```

4. Add a new label tier=web to all pods having 'app=v2' or 'app=v1' labels
```
kubectl label po -l "app in(v1,v2)" tier=web
```

5. Remove the 'tier' label from the pods we created before
```
kubectl label po nginx1 nginx2 tier-
# or
kubectl label po nginx{1..2} tier-
# or
kubectl label po -l tier tier-
```


