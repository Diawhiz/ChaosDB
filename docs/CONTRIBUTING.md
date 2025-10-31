# Contributing to ChaosDB

Thank you for your interest in contributing to ChaosDB! We welcome all contributions and aim to foster an open, respectful, and collaborative environment. This document outlines the process and best practices for contributing to this project.

---

## Code of Conduct

We follow the [Contributor Covenant v2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/) to ensure a welcoming and respectful community. **Please read and adhere to it.**

---

## How to Contribute

1. **Fork the Repository**
    - Click the "Fork" button on [https://github.com/Diawhiz/ChaosDB](https://github.com/Diawhiz/ChaosDB) to create your own copy.

2. **Clone Your Fork**
    ```bash
    git clone https://github.com/diawhiz/ChaosDB.git
    cd ChaosDB
    ```

3. **Set Up the Environment**
    - Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```
    - Run tests to ensure everything works:
      ```bash
      pytest tests/
      ```

4. **Create a Branch**
    - Use a descriptive branch name (e.g., `feature/add-backup` or `bugfix/fix-typo`):
      ```bash
      git checkout -b feature/add-backup
      ```

5. **Make Changes**
    - Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for coding style.
    - Comment your code where necessary.
    - Update or add tests in the `tests/` directory.
    - Add or update documentation as needed.

6. **Commit Changes**
    - Write clear, concise commit messages that describe your changes:
      ```bash
      git commit -m "Add backup feature with automated scheduling"
      ```

7. **Push to Your Fork**
    ```bash
    git push origin feature/add-backup
    ```

8. **Submit a Pull Request (PR)**
    - Open a PR from your branch to the main repository's `main` branch.
    - Provide a clear description of your changes, link relevant issues, and explain any design decisions.

---

## Reporting Issues

- Use the [GitHub Issues page](https://github.com/Diawhiz/ChaosDB/issues) to report bugs or suggest features.
- Provide:
    - Steps to reproduce the issue
    - Expected vs. actual behavior
    - Any relevant logs, error messages, or screenshots

---

## Pull Request Guidelines

- Ensure all tests pass before submitting your PR.
- Update the `README.md` or other documentation if your changes require it.
- Get at least one approval from a maintainer before merging.
- Address feedback in follow-up commits.
- Keep PRs focused—avoid bundling unrelated changes.

---

## Development Guidelines

- Use **Python 3.8+**.
- Write unit tests for new features or bug fixes.
- Avoid breaking existing functionality unless necessary and justified.
- Document new APIs or changes in `docs/`.

---

## Community & Support

- Join discussions on the [GitHub Discussions page](https://github.com/Diawhiz/ChaosDB/discussions).
- For urgent matters, contact the maintainer: [igbemisola53@gmail.com](mailto:igbemisola53@gmail.com).

---

We’re excited to see your contributions to ChaosDB!  
**Happy coding!**
