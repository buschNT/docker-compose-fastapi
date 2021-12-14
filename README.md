# docker-compose-fastapi

Docker compose setup with Uvicorn for FastAPI web applications in Python 3.9 with Poetry.

## Description

This docker compose setup includes a Docker image for creating APIs with FastAPI. The FastAPI docker image is based on an `alpine` python image, however you may want to switch to a `slim` image if you have trouble installing other required dependencies for your project. Poetry is used for package and dependency management.

FastAPI is a Python web framework, based on and powered by Starlette, with one of the best performances. It can achieve speeds comparable (or even superior to) to Go and Node.js frameworks.

This repository is mainly used as a template for other projects.

## Links

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Poetry](https://python-poetry.org/)
