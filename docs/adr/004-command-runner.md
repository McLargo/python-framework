# ADR-004 - Command Runner

## Context and Problem Statement

As the project grows, there are multiple commands that you may need to run
often, such as tests, linting, docker commands... A command runner can help to
centralize and simplify the execution of these commands.

## Solution

[Taskfile](https://taskfile.dev) is a task runner build in go. It allows to
define a file that contains all the commands and variables required to execute
simple (or more complex) tasks. It also allows to define dependencies between
tasks, making it easier to manage complex workflows.

## Other Solution Considered

- Makefile: a simple tool to define and execute tasks, but it is less powerful
  and flexible compared to Taskfile, especially for managing complex workflows
  with dependencies.
- [just](https://just.systems/man/en/): a command runner made in Rust. A totally
  valid alternative worth to explore, but at first sight, seems more complex and
  less intuitive compared to Taskfile.

Creation Date: 21/09/2026
Status: Accepted
