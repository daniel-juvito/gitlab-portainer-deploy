from setuptools import setup

setup(
    name="gitlab-portainer-deploy",
    version="0.1",
    packages=["deploy", ],
    zip_safe=False,
    install_requires=[
        "click",
        "requests",
        "urllib3==1.26.15",
    ],
    entry_points="""
        [console_scripts]
        deploy=deploy.cli:main
    """
)
