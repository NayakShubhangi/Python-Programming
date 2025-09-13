GitOps - GitHub Development Test Operational with Full Support of CI/CD:

    GitHub Actions is a CI/CD platform that allows you to automate workflows like building, testing, and deploying code directly from your GitHub repository.
    GitHub Actions is an advanced replacement for Jenkins in almost all aspects.

NOTE:

    The first time we run a new workflow, it MUST reside in the DEFAULT branch of the repository,
    otherwise, it won't be displayed in the 'Actions' tab.


Core Concepts:

    1. Workflow: A YAML file that defines automation (./.github/workflows/).
    2. Job: A set of steps that run the same virtual machine.
    3. Step: Individual tasks- run a command, check out the code.
    4. Runner: The machine that executes the workflow (GitHub-Hosted or Self-Hosted).


Triggers:

    1. Workflow Dispatch: Manual Build
    2. On: Push, Pull, or Merge requests, among others (All GitHub events)
    3. Schedule: Cron (Only UTC time zone)
    4. Workflow Call: Reusable workflow to call in another workflow


Environments, Secrets, and Variables:

    Secrets can be three types:
        - 1. Environment Secrets (Bottom Level)
                - Specific to the (ONE) environment and its permissions.
        - 2. Repository Secrets (Middle level)
                - Specific to the (ONE) repository and accessible by all of its branches along with its permissions
        - 3. Organizational Secrets (Top Level)
                - Specific to the organization and accessible by ALL of the repositories within the organization
    
    Environment Secrets/Variables will overwrite Repository Secrets/Variables if they have the same name.

    When using an Environment Secret/Variable, the workflow will need access to run in the environment the Secret/Variable belongs to, which can only be approved to deploy by up to 6 'Reviewers.' It will only run the job that requires the environment if it gets deployed. Otherwise, that job won't run. Jobs that don't need an environment will run without any trouble.


Artifacts:

    1. Artifacts (reusable objects) can be stored between multiple jobs within a workflow through Uploading and Downloading.
    2. GitHub Environment can be accessible within multiple steps in a single job inside a workflow.
    3. GitHub Output can be accessible within multiple jobs in a single workflow.
    (Workflow >> Jobs >> Steps)


Reusable Workflow versus Action:

    Reusable Workflows can be compared to Python Classes, as Python Classes have multiple methods within it. Similarly, Reusable Workflows can have multiple actions within it.
    Actions can be compared to Python Functions, as they can be used multiple times within a workflow.