# 🇬🇧 English Version

# Growing Code: Python Fundamentals Through Garden Data

Discover Python's fundamental syntax and semantics by analyzing community garden data. This project introduces core programming concepts—expressions, variables, functions, and control flow—through practical, real-world scenarios related to sustainable community initiatives. 

## 🛠 Prerequisites and Requirements

* **Python Version:** Python 3.10 or higher is required.
* **Linter:** All code must strictly respect `flake8` standards.
* **Type Checking:** Type hints are recommended for exercises 0-6 and strictly required for Exercise 7. Use `mypy` to check typing.
* **Structure:** Each exercise must be located in its specific directory (e.g., `ex0/`, `ex1/`) and each file must contain *only* the requested function.
* **Execution:** Do not write `if __name__ == "__main__":` blocks or global code. Use the provided `main.py` helper script to test the functions.

## 📂 Project Structure & Exercises

| Directory | File(s) to Submit | Description |
| :--- | :--- | :--- |
| `ex0/` | `ft_hello_garden.py` | A basic function `ft_hello_garden()` that prints a welcome message to the garden community: "Hello, Garden Community!". |
| `ex1/` | `ft_garden_name.py` | Function `ft_garden_name()` that prompts for a garden name and prints it alongside a fixed status message: "Status: Growing well!". |
| `ex2/` | `ft_plot_area.py` | Function `ft_plot_area()` that calculates a rectangular plot's area by asking for the length and width inputs. |
| `ex3/` | `ft_harvest_total.py` | Function `ft_harvest_total()` that calculates the total weight of vegetables harvested over three separate days. |
| `ex4/` | `ft_plant_age.py` | Function `ft_plant_age()` that checks if a plant is ready for harvest (strictly more than 60 days old). |
| `ex5/` | `ft_water_reminder.py` | Function `ft_water_reminder()` that prints "Water the plants!" if it has been more than 2 days since the last watering, otherwise "Plants are fine". |
| `ex6/` | `ft_count_harvest_iterative.py`<br>`ft_count_harvest_recursive.py` | Two functions that count from 1 to a given number of days until harvest, implementing both iterative and recursive approaches. |
| `ex7/` | `ft_seed_inventory.py` | Function `ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:` that manages seed inventory. It formats the seed type with a capital letter and handles specific units (`packets`, `grams`, `area`). |

## 🚀 How to Test

Since the submitted files contain only functions and no main program loops, a helper tool is required for testing. 

1. Place the provided `main.py` file in your working directory.
2. Ensure your exercise files are in the same folder or structured correctly.
3. Run the helper script in your terminal:
   ```bash
   python3 main.py
   ```
   This helper will automatically import your functions and allow you to test them easily.

# Growing Code: 庭園データで学ぶPythonの基礎

コミュニティガーデンのデータを分析しながら、Pythonの基本的な構文とセマンティクス（意味論）を学ぶプロジェクトです。持続可能なコミュニティ活動という現実的なテーマを通して、式、変数、関数、制御フローなどのプログラミングのコアコンセプトを習得します。

## 🛠 前提条件と要件

* Pythonバージョン: Python 3.10以上が必要です。
* リンター: すべてのコードは `flake8` の基準に厳格に従う必要があります。
* 型チェック: 課題0〜6では型ヒントの記述が推奨されており、課題7では必須要件となります。型チェックには `mypy` を使用します。
* ディレクトリ構成: 各課題は指定されたディレクトリ（例: `ex0/`、`ex1/`）に配置し、各ファイルには要求された関数のみを記述する必要があります。
* 実行について: ファイル内に `if name == "main":` ブロックや関数外のコードを書いてはいけません。テストには、配布されている `main.py` を使用してください。

## 📂 プロジェクト構成と課題一覧

| ディレクトリ | 提出ファイル | 概要 |
| :--- | :--- | :--- |
| `ex0/` | `ft_hello_garden.py` | ガーデンコミュニティへの歓迎メッセージ（"Hello, Garden Community!"）を出力する基本関数 `ft_hello_garden()` を作成します。 |
| `ex1/` | `ft_garden_name.py` | 庭園名を入力させ、指定されたステータスメッセージ（"Status: Growing well!"）とともに表示する関数 `ft_garden_name()` を作成します。 |
| `ex2/` | `ft_plot_area.py` | 縦と横の長さを入力させ、長方形の区画の面積を計算する関数 `ft_plot_area()` を作成します。 |
| `ex3/` | `ft_harvest_total.py` | 3日間の野菜の収穫量をそれぞれ入力させ、合計の重量を計算する関数 `ft_harvest_total()` を作成します。 |
| `ex4/` | `ft_plant_age.py` | 植物の日齢を入力させ、収穫可能（60日より大きい）かどうかを判定する関数 `ft_plant_age()` を作成します。 |
| `ex5/` | `ft_water_reminder.py` | 前回水やりをしてからの日数を受け取り、2日を超えていれば "Water the plants!"、そうでなければ "Plants are fine" と出力する関数 `ft_water_reminder()` を作成します。 |
| `ex6/` | `ft_count_harvest_iterative.py`


`ft_count_harvest_recursive.py` | 収穫までの日数を1からカウントアップする関数を、反復処理（Iterative）と再帰処理（Recursive）の両方のアプローチで作成します。 |
| `ex7/` | `ft_seed_inventory.py` | 種子の在庫を管理する関数 `ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:` を作成します。種子の種類は大文字から始め、特定の単位（`packets`, `grams`, `area`）のみを処理します。 |

## 🚀 テスト方法

提出するファイルには関数のみが含まれており、メインプログラムの実行ブロックは含まれません。そのため、テストには専用のヘルパーツールが必要です。

1. 配布された `main.py` ファイルを作業ディレクトリに配置します。
2. 課題のファイルが `main.py` と同じフォルダ内に正しく配置されていることを確認します。
3. ターミナルで以下のコマンドを実行してヘルパースクリプトを起動します：
`python3 main.py`

このヘルパーが自動的に関数をインポートするため、簡単にコードのテストを行うことができます。
