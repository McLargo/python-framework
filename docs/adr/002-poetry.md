# ADR-002 - poetry installation

## Context and Problem Statement

This project is mean to be a collaborative project, and it is important to have
a properly configured environment, so everyone can run the project without any
issues or inconsistencies.

## Solution

In order to have a clean environment for this project, and to avoid issues with
different versions of libraries and other dependencies, I am going to use poetry.

Poetry helps to keep dependencies in one place, in a separated virtual
environment. As it uses pyproject.toml to keep the versions of the libraries, it
is easy to install and keep track of the dependencies.

## Other Solution Considered

- docker: as this project is simple enough, and there is only 1 service required,
  docker is not needed. It is a good solution for more complex projects, but it
  is not needed here.
- virtualenvs: tool to keep dependencies in one place. Easy to install, and
  allows to have different environments for different projects. But poetry makes
  easier to install and maintain dependencies.

Creation Date: 04/10/2023
Status: Accepted
