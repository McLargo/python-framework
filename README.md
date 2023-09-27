# python-frawework

This is my python framework for new code challenges that requires to develop an
API or small projects that requires to have a minimal API service. It is based
on FastAPI, and it is dockerized. Also supports a minimal frontend, based on
nodejs & vite.

From here, you can start to develop your own API, and add new endpoints, or new
services. It acts as a boilerplate, and it is ready to be used in any
environment. See some of the features:

- README.md template
- Docker & docker compose
- FastAPI & pydantic implementation
- fixed code structure
- fixed docs structure
- pytest & coverage

## User Experience

This is a boilerplate, so it is not intended to be used as a final product. It
is intended to be used as a starting point for new projects. It should support a
backend by default, and a frontend if needed.

## Requirements

Backend is based on FastAPI, as it provides by default with swagger, so endpoint
documentation is ready to be used. Also, it provides with a lot of features,
like security. Very is easy to develop.

## Description

My personal boilerplate for new projects. It is based on FastAPI, using docker
to build in any machine without any issues.

My goal with this project is to gather in one place all the knowledge I have
regarding a python project, and to have a starting point for new projects, which
sometimes can be a little bit overwhelming. It provides a starting point, with a
fixed structure that can be improve at any time, to have a standard way of
developing new projects. I keep all my knowledge in one place, and it is the
perfect playground for new features that can be included in the future.

TODO: explain folder structure
Aside from `app.py` file, which is mandatory to start application, I've created
two extra folders One to manage and gather other python files related to the
application, and another folder for tests
TODO: explain folder structure

## Getting started

For this project, you will need to have
[docker](https://docs.docker.com/get-docker/) and
[docker compose](https://docs.docker.com/compose/install/) installed. Please
install in your machine using the instructions provided in the links.

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

- [ADR-001](docs/adr/001-docker.md) - Docker

## Contribution

Use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) to
your commit messages.

As only one developer (myself) is expected to work at the same time in this
project and frontend, every commit goes to **master** (Trunk-based development).
No need to create new branches and make pull-request (unless breaking changes
are introduced, such as new contracts to the app, big refactors...).

Install pre-commit hooks to include automatic tools to review code:

## Testing

I do believe that unit test are the most important part of a project, to keep
the code clean, and avoid breaking code that is working. A good coverage of the
application indicates that services are robust. [TDD Test-Driven Development](
https://www.guru99.com/test-driven-development.html) is my ideal development
methodology.

Unit testing and functional is available. E2E testing is not yet available.

Go inside docker container:

- `pytest` -> run all tests.
- `pytest --cov-report=html` -> run all tests and generate a coverage report in
  html format.

## CI/CD

Not completed.

## Monitoring

Not completed.

## Troubleshooting

Not completed.

## License

Not completed.
