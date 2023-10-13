* Run locally:
```shell
docker buildx build --platform linux/amd64,linux/arm64 . -t ajaxpyvovarovy/k8s-sample-app:0.0.1 --push
docker run -it --rm -p 8080:5000 --mount type=bind,source="$(pwd)"/file.txt,target=/app/file.txt ajaxpyvovarovy/k8s-sample-app:0.0.1
```
