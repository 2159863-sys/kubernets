# Docker & Container Orchestration – School Assignments

My assignments for the Docker and DevOps module of the Software Developer course (MBO niveau 4). They cover running containers, Docker Compose, building my own images and a Docker Swarm cluster.

## What is in this repository

| Folder / file | What it is |
|---------------|------------|
| `docker-compose.yml` | Two services with Docker Compose: an nginx web server and a small HTTP echo API |
| `opdracht 3/` | A Flask app in its own Docker image. It shows which container handled the request and simulates slow and fast requests, to see load balancing across replicas |
| `opdracht 4/version-api/` | A Flask REST API with `/version` and `/health` endpoints. The version comes from an environment variable, used to practise rolling updates |
| `dind-docker-swarm-lab/` | A Docker Swarm lab with one manager and two workers, running as Docker-in-Docker containers |
| `*.docx`, screenshots | My write-ups and results for each assignment |

## Built with

- Docker and Docker Compose
- Docker Swarm
- Python and Flask
- nginx

## Try it

Run the Compose example:

```bash
docker compose up -d
```

The web server is on http://localhost:8080 and the API on http://localhost:5678.

Build and run the version API:

```bash
cd "opdracht 4/version-api"
docker build -t version-api .
docker run -p 5000:5000 -e APP_VERSION=1.0.0 version-api
```

Then open http://localhost:5000/version.
