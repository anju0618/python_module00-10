The Matrix: Data Engineering Basics

Welcome to the real world of data engineering. This project covers the fundamental tools and practices every data engineer needs to build robust, isolated, and secure data systems.

Overview

This repository contains practical exercises focused on setting up proper Python development environments, managing dependencies, and securely handling configurations.

Exercises

Exercise 0: The Construct

A script (construct.py) that demonstrates the concept of virtual environments. It detects whether it is running inside an isolated virtual environment or the global system, illustrating the importance of environment separation.

Exercise 1: Loading Programs

A data analysis program (loading.py) that showcases dependency management using both pip (requirements.txt) and Poetry (pyproject.toml). It uses numpy, pandas, and matplotlib to generate and visualize simulated Matrix data, highlighting how to handle external libraries safely.

Exercise 2: Accessing the Mainframe

A configuration management script (oracle.py) that teaches the use of environment variables and .env files via python-dotenv. It demonstrates how to handle sensitive information (like API keys and database URLs) and switch between development and production modes without hardcoding secrets.

Requirements

Python 3.10+

flake8 for linting

mypy for static type checking

The Matrix: データエンジニアリングの基礎

データエンジニアリングの「現実世界」へようこそ。このプロジェクトでは、堅牢で分離された安全なデータシステムを構築するために必要な、基本的なツールと実践的な手法を学びます。

概要

このリポジトリには、適切なPython開発環境の構築、パッケージの依存関係管理、そして設定値の安全な取り扱いに焦点を当てた実践的な課題が含まれています。

課題内容

Exercise 0: The Construct (仮想環境)

仮想環境の概念を理解するためのスクリプト（construct.py）です。プログラムが隔離された仮想環境で実行されているか、グローバルのシステム環境で実行されているかを検知し、環境を分離することの重要性を示します。

Exercise 1: Loading Programs (依存関係管理)

pip（requirements.txt）とPoetry（pyproject.toml）の両方を使用した依存関係管理を実践するデータ分析プログラム（loading.py）です。numpy、pandas、matplotlibを使用してシミュレーションデータを生成・可視化し、外部ライブラリを安全に扱う方法を学びます。

Exercise 2: Accessing the Mainframe (環境変数と設定)

環境変数と.envファイル（python-dotenvを利用）の扱い方を学ぶスクリプト（oracle.py）です。APIキーやデータベースURLなどの機密情報をソースコードに直書き（ハードコード）せず、開発環境と本番環境を安全に切り替える手法を実装しています。

要件

Python 3.10以上

flake8 (静的コード解析)

mypy (静的型チェック)
