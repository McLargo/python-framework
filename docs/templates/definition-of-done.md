# Definition of DONE

JIRA is our issue tracking tool. It is responsibility of entire team to keep it
updated :wink:

## Before starting development

- Read carefully what the ticket is about.
- Review the acceptance criteria. If you don't understand something, ask for
  clarification. Don't hesitate to ask any questions.
- Make sure the testing plan is in place. Ask any of your colleagues to review
  it.
- Assign the ticket to yourself if it is not already, and move to **In
  Progress** status.

## Development

- Gitflow
  - Create a new branch from `develop` branch, remember to pull for latest
    changes. Name it as the ticket key, with prefix **feat/fix/bug/docs**,
    depending on the ticket's type. Example: `feat/ABC-1234`.
- Trunk-based development
  - All developers work in the same **master** branch. No need to create new
    branches or make pull-request (unless breaking changes are introduced).
- Do your commits to accomplish the required code changes. Commit message must
  follow [Conventional commit](https://www.conventionalcommits.org/en/v1.0.0/)
  and include the ID of the ticket at the beginning of the message. Example:
  `feat: ABC-1234: Add new feature`.
- Implement unit tests.
- Raise PR towards master. Then, you can move the ticket to **Code Review**
  status.
- Document carefully if code contain breaking changes, new environment
  variables, configuration changes, migration that DevOps/QA team needs to take
  into account once feature is deployed to staging/production.

## Code Review

- Be kind with others. We are all humans.
- Don't be afraid to suggest better ways to do it. We learn from each other.
- Mind business logic. Does it meet the acceptance criteria in the User Story?
- Mind performance.
- Re-usability and readability of the code
- Does it implement new unit/functional tests?
- Does it have any impact on the documentation?
- Does it met the code guidelines?
- Does it breaks any existing functionality?

## Deployment

- Once the PR is approved, it can be merged to `development` branch.
- After that, it can be deployed to the staging environment automatically by
  CI/CDE pipeline.
- Is there any variable that needs to be updated in the environment? If so,
  update it.
- The ticket can be moved to **Ready for QA** status.

## QA

- Read acceptance criteria and testing plan.
- Implement corresponding testing plan.
- Raise any issues found in the ticket.
- Response to the ticket with the results of the testing, either screenshots,
  postman collection, logs, etc.
- In case of any issues found, the ticket can be moved back to **In Progress**
  status.

## DONE

- Once the ticket is approved by QA, Product Owner can review if ticket met the
  accepted criteria. If yes, move ticket to **Done** status.
