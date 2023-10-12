* Run locally:
```shell
docker build . -t k8s-sample-app
docker run -it --rm -p 8080:5000 --mount type=bind,source="$(pwd)"/file.txt,target=/app/file.txt k8s-sample-app
```
