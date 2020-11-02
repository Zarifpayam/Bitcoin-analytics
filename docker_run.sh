
docker container rm aidin-starter
docker run -d -it --name aidin-starter -v "$PWD/src:/src" -v "$PWD/data:/data" aidin-starter

