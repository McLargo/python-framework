# ADR-003 - Type Hint

## Context and Problem Statement

The project should always include the best tools to keep the code clean. For
python type hints are not mandatory, but recommended. Also, review which tools
can review the code and ensure type hints is added consistently in the code.

## Solution

[Pyrefly](https://pyrefly.org) is a type checked made in python. It is fast in
compare to other tools like mypy, and it provides pre-commit and github actions
integration, which are currently used in this project.

## Other Solution Considered

- mypy: it was the initial tool considered for type checking, but it was
  replaced by Pyrefly due to performance and integration advantages.

Creation Date: 21/09/2026
Status: Accepted
