# pod-reader

Simple python script that uses the Kubernetes ServiceAccount to query pod information of a specified namespace.

After building the container, the intended usage is as follows:

```bash
$ kubectl run pod-explorer --image=pod-explorer:1.0 -- <target namespace>
$ kubectl logs pod-explorer
```

A handy way to test with this container is create an alias for exploring pods with these commands (assumes `default` namespace):

```bash
$ alias reader='kubectl run pod-explorer --image=pod-explorer:1.0 -- default ; \
                sleep 5 ; kubectl logs pod-explorer ; \
                kubectl delete pod pod-explorer'
```
