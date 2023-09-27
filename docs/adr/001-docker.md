# ADR-001 - docker

## Context and Problem Statement

With a machine that can run different projects, an each of them have their own
dependencies. Installing locally every dependency can be a mess, hard
to debug and maintain. Can cause to malfunction other projects, and breaking
compatibility.

## Solution

In order to have a clean environment for each project, and to avoid issues with
different versions of libraries and other dependencies, I am going to use
docker.

I am using docker since long time, and it is the perfect tool to keep tidy your
workspace. It allows to generate entire projects, running multiple services at
the same time connected between them. Installation is straight forward, as main
instructions are code inside docker files. Only requirement is to have installed
docker and docker compose, and with two simple commands, a project can be up and
running.

It minimize the risk of having different starting issues, as developers will run
the same instructions to start the project, and will end up with a clean
environment. Similar instructions can be enrich and used in testing and
production environment, so the code will run exactly the same way.

## Other Solution Considered

- poetry: easy to install with pip, is an alternative to even simpler projects
  that won't need docker. Keeps dependencies in one place, and can be used to
  generate virtual environments. Nice command line interface to manage
  libraries.
- virtualenvs: tool to keep dependencies in one place. Easy to install, and
  allows to have different environments for different projects. It is not as
  powerful as docker, as it only allows to have different environments, but not
  to run different services at the same time. Currently there are better
  solutions.

Creation Date: 27/09/2023
