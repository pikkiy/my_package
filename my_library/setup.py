from setuptools import setup, find_packages

setup(
    name="my_package",  # パッケージ名
    version="1.0.1",  # バージョン番号
    author="Your Name",  # 作者名
    author_email="your.email@example.com",  # 作者のメールアドレス
    description="A simple example package",  # パッケージの説明
    url="https://github.com/yourusername/my_package",  # パッケージのURL（GitHubリポジトリなど）
    packages=find_packages()  # パッケージを自動的に見つける
)