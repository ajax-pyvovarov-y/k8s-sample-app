Add ssh key:
```shell
argocd repocreds add git@github.com:ajax-pyvovarov-y/k8s-sample-app.git --ssh-private-key-path ~/.ssh/id_ed25519_argocd_test
```

Add application:
```shell
kubectl apply -n argocd -f argoproj.yaml
```
