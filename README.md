## cicd-in-action
Learning for cicd


## End to End flow of development to production
- Developer develop code locally and commit to dev branch
- Once developer commit dev branch build pipeline get activated and build starts
  - during build code complie happens
  - unit test run happens


## 🧪 Running Tests Locally
Run all tests:
```bash
pytest
```
Run tests with verbose output:
```bash
pytest -v
```
Run tests with coverage:
```bash
pytest --cov=src --cov-report=term-missing
```
Run tests with coverage and verbose:
```bash
pytest -v --cov=src --cov-report=term-missing
```
Run a specific test file:
```bash
pytest tests/test_example.py
```


## CI CD setup

To continue your CI/CD, here are the next steps you can take:

- Add a requirements.txt file
    - List all dependencies (e.g., pytest, streamlit, pytest-cov) so your CI pipeline can install them.

- Set up a CI workflow
    - Use a CI service like GitHub Actions, GitLab CI, or similar. For GitHub Actions, create a workflow file at .github/workflows/ci.yml to automate:

- Installing dependencies
    - Running tests
    - Checking code coverage
    - Add code quality checks
    - Integrate tools like flake8 or black for linting and formatting.

- Configure coverage reporting
    - Optionally, upload coverage reports to a service like Codecov.


- Push to GitHub and observe the CI pipeline
