from setuptools import setup, find_packages

setup(
    name="google_backup_checker",
    version="0.0.1",
    description="Triggers Kuma on GDrive backup",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)
