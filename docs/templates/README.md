# Project name

Small description of the project.

## User Experience

What is the output expected.

## Requirements

What are the requirements of the project.

## Description

Large description of the project, where user experience and requirements met together.

## Getting started

This is an example of how you may give instructions on setting up your project
locally. To get a local copy up and running follow these simple example steps.

For this project, you will need to have
[docker](https://docs.docker.com/get-docker/) and
[docker compose](https://docs.docker.com/compose/install/) installed. Please
install in your machine using the instructions provided in the links.

For this project, you will need to have [pip](https://pip.pypa.io/en/stable/)
and [poetry](https://python-poetry.org/) installed. Please install in your
machine using the instructions provided in the links.

### docker & docker compose utils

If you are new to docker compose, and love to use the terminal like me, please
see below some of the most used commands:

- build images: `docker compose build`
- start containers: `docker compose up -d <name>`
- remove containers: `docker compose down`
- list all containers: `docker compose ps`
- stop containers: `docker compose stop <name>`
- enter inside the container: `docker exec -it <container_id> bash`
- to see the logs in real time: `docker logs -f <container_id>`
- list all images: `docker images`
- remove an image: `docker rmi <image_id>`

### poetry

If you are new to poetry, see below some of the most used commands:

- `poetry --help`: to see all the commands available
- `poetry init`: to create a new project
- `poetry install`: to install all the dependencies
- `poetry add <package_name>`: to add a new package to the project
- `poetry remove <package_name>`: to remove a package from the project
- `poetry run <command>`: to run a command inside the virtual environment
- `poetry shell`: to enter inside the virtual environment

### Installation and usage

- step 1: `docker compose build`
- step 2: `docker compose up -d`
- step 3: go to your browser and open
  [http://localhost:8000/docs](http://localhost:8000/docs). If not opening,
  `docker logs -f <container_id>` to see the logs for errors.
- step 4: start coding

## Architecture Decision Record

A decision record is a document that captures an important architectural
decision made along with its context and consequences.

Below is a list of the ADRs for this project:

- [ADR-000](../../docs/templates/adr.md) - ADR template

## Flows

Flows of the project. Always keeping documentation close to code.

## Contribution

Use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) to
your commit messages.

Trunk-based development vs Gitflow.

.pre-commit-config.yaml to include automatic tools to review code.

## Testing

Unit testing, functional testing, e2e testing...

Go inside docker container:

- `pytest` -> run all tests.
- `pytest --cov-report=html` -> run all tests and generate a coverage report in
  html format.

## Security

If applicable.

## CI/CD

What is the CI/CD pipeline.

## Monitoring

What is the monitoring strategy and tools. Liveness endpoint, tracing and log
systems...

## Troubleshooting

Most common errors you can find when running the project.

## License

If applicable.
