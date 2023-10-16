* Add ssh key:
```shell
flux create secret git sample-app --url="ssh://git@github.com/ajax-pyvovarov-y/k8s-sample-app.git" --private-key-file=/Users/pyvovarov.y/.ssh/id_ed25519_argocd_test
```

* Add application:
```shell
cd ~/repos/flux-cd-test/fluxcd/apps/sample-app
kubectl apply -n flux-system -f repo.yaml
```
