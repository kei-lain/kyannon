# import setuptools

# with open("README.md", "r", encoding="utf-8") as fhand:
#     long_description = fhand.read()

# setuptools.setup(
#     name="Kyannon-a double encryption sftp script",
#     version="0.0.1",
#     author="Lainey Tubbs",
#     author_email="Laineytubbs@protonmail.com",
#     description=("This cli script allows encrypts files via AES-256 prior to sending it over SFTP then decrypts it on the other side. This prevents sensitive files from being suceptible to packet capturing"),
#     long_description=("This cli script allows encrypts files via AES-256 prior to sending it over SFTP then decrypts it on the other side. This prevents sensitive files from being suceptible to packet capturing"),
#     long_description_content_type="text/markdown",
#     url="https://github.com/kei-lain/kyannon",
#     project_urls={
#         # "Bug Tracker": 
#     classifiers==[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     install_requires==["setuptools",
#     "bcrypt==4.0.1",
#     "cffi==1.15.1",
#     "cryptography==41.0.4",
#     "paramiko==3.3.1",
#     "pycparser==2.21",
#     "pycryptodome==3.19.0",
#     "pycryptodomex==3.19.0",
#     "PyNaCl==1.5.0",
#     "python-aes256==1.0.5",
#     "python-dotenv==1.0.0",
#     "scp==0.14.5"
#     ],
#     packages=setuptools.find_packages(),
#     python_requires=">=3.6",
#     entry_points={
#         "console_scripts": [
#             "kyannon = kyannon",
#             "remotedecypt = remotedecrypt",
#         ]
#     }
#     }
# )

import setuptools

# with open("README.md", "r", encoding="utf-8") as fhand:
#     long_description = fhand.read()

setuptools.setup(
    name="kyannon",
    version="0.0.1",
    author="Lainey Tubbs",
    author_email="Laineytubbs@protonmail.com",
    description=("This CLI script encrypts files via AES-256 before sending them over SFTP and decrypts them on the other side. This prevents sensitive files from being susceptible to packet capturing."),
    long_description=("This CLI script encrypts files via AES-256 before sending them over SFTP and decrypts them on the other side. This prevents sensitive files from being susceptible to packet capturing."),
    long_description_content_type="text/markdown",
    url="https://github.com/kei-lain/kyannon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "bcrypt==4.0.1",
        "cffi==1.15.1",
        "cryptography==41.0.4",
        "paramiko==3.3.1",
        "pycparser==2.21",
        "pycryptodome==3.19.0",
        "pycryptodomex==3.19.0",
        "PyNaCl==1.5.0",
        "python-aes256==1.0.5",
        "python-dotenv==1.0.0",
        "scp==0.14.5"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "kyannon = kyannon",  # Replace kyannon with the name of your main script
            "remotedecrypt = remotedecrypt"  # Replace remotedecrypt with the name of your main script
        ]
    }
)

