# Contribution Guidelines

**This** guideline assumes the reader has a basic understanding of open source and how to contribute to open source projects.  
If you are new to these topics, we recommend reading the general [Open Source Guide](https://opensource.guide/).

## Submitting issues

Bugs and enhancements are tracked in the [GitHub Issue](https://github.com/ctc-nt/NAGATO/issues) system. You are welcome to submit an issue even if you are unsure whether it is a bug or a feature worth implementing.

We encourage you to use the issue template to submit an issue. Also, before submitting a new issue, please check whether the same bug or enhancement has already been reported.  
If it has, add a comment to the existing issue instead of creating a new one.

### Reporting a bug

To help others understand and reproduce the bug you encountered, please provide the following information:

- Version information
  - Robot Framework version
  - Python interpreter version
  - Operating system and its version
- Steps to reproduce the issue
- Error messages and tracebacks

Please note that all information in GitHub Issues is public. Do not include any confidential information.

### Feature requests

When requesting a new feature, describe it and its use case in as much detail as possible. It is also valid to contribute code in the form of a pull request as described below, especially for larger enhancements.

Also consider whether this functionality might be better implemented as a separate tool outside of the core framework.

## Code contributions

If you fix a bug or implement an enhancement, you can contribute your changes through a GitHub pull request.  
This doesn't have to be limited to code, even just fixes or enhancements to documentation or tests can be very valuable.

Often, you probably already have a bug or enhancement in mind that you want to work on, but you can also look through GitHub Issues to find bugs and enhancements that other people have submitted.

Issues vary widely in terms of complexity and difficulty, so try to find one that matches your skill level and knowledge.

### Pull requests

Pull requests are the main way to submit code in GitHub. They facilitate discussions and reviews of code changes.  

The prerequisites for creating a pull request are that you have a GitHub account and that you have Git installed.  
GitHub has articles that explain how to set up Git, how to fork a repository, and how to use pull requests. We recommend that you read them.

In NAGATO, pull requests should be submitted to the `develop` branch.

### Coding conventions

#### General

NAGATO uses the common Python coding conventions defined in PEP 8. We also strive to ensure that all code follows the [SOLID principles](https://en.wikipedia.org/wiki/SOLID).

An important principle is that code should be clear enough that it does not need comments.  
All code, including tests, should be compatible with all supported Python interpreters and versions.
See README.md for supported Python versions.

### Documentation

#### Robot Framework Libraries

If the code is implemented as a Robot Framework library, it will have documentation generated from the docstrings using the Libdoc tool.  
The documentation uses Robot Framework's own documentation format. For information about the documentation format, see the "Documentation" section of Robot Framework's [CONTRIBUTING.rst](https://github.com/robotframework/robotframework/blob/master/CONTRIBUTING.rst#documentation).  
If you are creating a new Robot Framework library or updating an existing one, keep in mind that this libdoc will create your documentation.

### Testing

When you submit a pull request that includes a bug fix or feature, you should always include tests for your code changes. These tests prove that your code changes work, help prevent future bugs, and help document your changes.

Before submitting a pull request, run all your tests to make sure your code changes don't break anything.  
If possible, test in multiple environments and interpreters (e.g. Windows, Linux, macOS, different Python versions). Pull requests are also automatically tested with GitHub Actions.

#### Testing method

NAGATO uses [pytest](https://pypi.org/project/pytest/) for testing.  
After installing pytest, run tests on the `tests` directory.  

```shell
pytest tests/
```
