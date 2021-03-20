from setuptools import setup, find_packages

setup(
    name="hankify_pw",
    version="1.0.0",
    description="Generate Hank Preston-y passwords",
    url="https://gitlab.systems.cll.cloud/jclarke/hankify-pw",
    entry_points={"console_scripts": ["hankify-pw=hankify_pw:hanky_pass"]},
    author="Joe Clarke",
    author_email="jclarke@cisco.com",
    license="MIT",
    setup_requires=["wheel"],
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    keywords=["Elemental"],
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)