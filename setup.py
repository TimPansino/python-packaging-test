GITHUB_URL = "https://github.com/TimPansino/python-packaging-test"
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: Implementation :: CPython",
]


if __name__ == "__main__":
    from setuptools import setup
    setup(
        name="packaging-test-482c583e907c",
        description="Testing packaging with setuptools-scm.",
        long_description=open("README.md").read(),
        url=GITHUB_URL,
        project_urls={"Source": GITHUB_URL},
        author="Tim Pansino",
        author_email="tpansino@newrelic.com",
        maintainer="Tim Pansino",
        maintainer_email="tpansino@newrelic.com",
        license="MIT",
        zip_safe=False,
        classifiers=CLASSIFIERS,
        python_requires=">=3.7",
        setup_requires=["setuptools>=45", "setuptools_scm[toml]>=6.2"],
        use_scm_version={
            "write_to": "packaging-test-482c583e907c/_version.py",
        },
    )
