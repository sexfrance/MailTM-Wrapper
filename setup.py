from setuptools import setup, find_packages

setup(
    name="MailTmWrapper",                   
    version="0.0.6",                           
    packages=find_packages(),               
    install_requires=["requests"],           
    author="Sexfrance",                     
    author_email="bwuuuuu@gmail.com",
    description="A Python wrapper for the Mail.tm API",   
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sexfrance/MailTM-Wrapper", 
    classifiers=[                          
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Email"
    ],
    python_requires=">=3.6",
)