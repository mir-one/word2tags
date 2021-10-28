import io
import setuptools

with io.open("README.md", mode="r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="word2tags",
    version="0.0.1",
    author="Roman Inozemtsev",
    author_email="dao@mir.one",
    description="Russian morphology",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mir-one/word2tags",
    packages=setuptools.find_packages(),
    package_data={'word2tags': ['*.dat', '*.db']},
    include_package_data=True,
)
