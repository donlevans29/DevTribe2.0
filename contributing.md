# Contributing to DevTribe 2.0

Thank you for your interest in contributing to the DevTribe 2.0 project! This document outlines the workflow and best practices for collaborating on this project.

---

## Workflow Overview

The contribution process follows these steps:
1. **Create a Feature Branch**: Work on a separate branch for each feature or task.
2. **Make Changes Locally**: Implement your changes and test them.
3. **Commit Changes**: Write clear and descriptive commit messages.
4. **Pull Latest Changes**: Sync your branch with the latest updates from the `main` branch.
5. **Push Changes**: Push your branch to the remote repository.
6. **Create a Pull Request (PR)**: Submit your changes for review.
7. **Review and Merge**: Collaborators review the PR, resolve conflicts if necessary, and merge it into the `main` branch.

---

## Detailed Steps

### Step 1: Create a Feature Branch
- Always create a new branch for your work to avoid conflicts with the `main` branch.
- Use a descriptive branch name:

  ```sh
  git checkout -b feature/your-feature-name

### Step 2: Create a Feature Branch

- Implement your changes in the appropriate files.
- Test your changes locally to ensure they work as expected.

### Step 3: Commit Changes

-stage your changes:

```
git add
git commit
```
- Commit your changes with a clear and descriptive message:
```
git commit -m "Add motivation section and target audience to README.md"
```

### Step 4: Pull Latest Changes
 - Before pushing, pull te lagest changes from te main branch to ensure your branch is up-to-date
 
 ```
 git pull origin main

 ```
### Step 5: Push Changes
- Push your feature branch to the remote repository:

```
git push origin feature/your-feature-name

```

### Step 6: Create a Pull Request (PR)
- Go to the repository on GitHub.
- Click Pull Requests > New Pull Request.
- Select your feature branch and compare it with the main branch.
- Add a title and description for your PR, explaining the changes you made.
- Request reviews from collaborators.

### Step 7: Review and Merge
- Collaborators review the PR and provide feedback.
- If there are conflicts, resolve them locally

```
git pull origin main
# Resolve conflicts in files
git add resolved-file
git commit -m "Resolve merge conflicts"
git push origin feature/your-feature-name

```
- Once approved, merge the PR into the main branch.

<hr>

### Best Practices

<b>Commit Messages</b>

- Use the imperative mood (e.g., "Add", "Fix", "Update").
- Keep the message concise but descriptive.

Example
```
git commit -m "Add list of target audience to README.md"

```

<b>Branch Naming </b>

- Use a consistent naming convention:
  - feature/feature-name for new features.
  - bugfix/bug-description for bug fixes.
  - docs/documentation-update for documentation changes.

<b>Pull Requests</b>
- Keep PRs small and focused on a single feature or task.
- Provide a clear description of the changes and their purpose.

<b>Testing</b>

- Test your changes locally before committing.
- If applicable, write automated tests to verify functionality.

<hr>

<b>Example Workflow </b>
Scenario: Adding a New Section to the README.md

1.Create a Branch:
```
git checkout -b feature/add-readme-section

```

2. Make Changes: Edit the README.md file to add the new section.


```
3. Commit Changes:

```
git add README.md
git commit -m "Add motivation section to README.md"

```

4. Pull Latest Changes:
```

git pull origin main

```

5. Push Changes:
```
git push origin feature/add-readme-section

```

6. Create a Pull Request:

Go to GitHub and create a PR for the <b>feature/add-readme-section</b> branch.
Add a description of the changes.

7. Review and Merge:
  - Collaborators review the PR.
  - Resolve any conflicts if necessary.
  - Merge the PR into the <b>main</b> branch.

<hr>

<b>Additional Notes</b>

- Sync Regularly: Frequently pull changes from the main branch to avoid conflicts.
- Use .gitignore: Exclude unnecessary files (e.g., logs, temporary files) from the repository.
- Communicate: Use comments in PRs or team communication tools to explain your changes.
<hr>

By following this workflow, you can ensure smooth collaboration and maintain a clean, organized repository. Thank you for contributing to DevTribe 2.0!