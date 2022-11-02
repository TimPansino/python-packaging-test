# Python Packaging Test

A demo of packaging with setuptools scm.

## Potential Bug

To install this package from **Test PyPi** and view the potential bug on ARM Macs, install with the following command.

**Note: Using a virtual environment seems to prevent this bug from occuring for unknown reasons.**

```bash
pip install -i https://test.pypi.org/simple --extra-index-url https://pypi.org/simple packaging-test-482c583e907c==0.1.6
```

```
  WARNING: Requested packaging-test-482c583e907c==0.1.6 from https://test-files.pythonhosted.org/packages/3f/78/cdef55b6743f195ba41808320b273e4b5cf8c60a924d7781f9951cf83813/packaging-test-482c583e907c-0.1.6.tar.gz, but installing version 0.0.0
Discarding https://test-files.pythonhosted.org/packages/3f/78/cdef55b6743f195ba41808320b273e4b5cf8c60a924d7781f9951cf83813/packaging-test-482c583e907c-0.1.6.tar.gz (from https://test.pypi.org/simple/packaging-test-482c583e907c/) (requires-python:>=3.7): Requested packaging-test-482c583e907c==0.1.6 from https://test-files.pythonhosted.org/packages/3f/78/cdef55b6743f195ba41808320b273e4b5cf8c60a924d7781f9951cf83813/packaging-test-482c583e907c-0.1.6.tar.gz has inconsistent version: expected '0.1.6', but metadata has '0.0.0'
ERROR: Could not find a version that satisfies the requirement packaging-test-482c583e907c==0.1.6 (from versions: 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5, 0.1.6)
ERROR: No matching distribution found for packaging-test-482c583e907c==0.1.6
```
