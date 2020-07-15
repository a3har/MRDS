docker build -t rajhosp .
docker run -ti --rm -v $(pwd):/usr/src -p 8000:8000 rajhosp