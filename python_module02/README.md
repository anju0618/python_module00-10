# Garden Guardian - Data Engineering for Smart Agriculture (Version 2.0)

Welcome to **Garden Guardian**, a project focused on building resilient data pipelines for smart agricultural monitoring systems. This repository demonstrates how to design fault-tolerant systems using Python's exception handling mechanisms to manage sensor anomalies, data corruption, and infrastructure failures in a digital greenhouse environment.

Additionally, this version includes a comprehensive guide on **Markdown Special Characters Escaping**, which is crucial for writing precise documentation (README) and engineering solid AI prompts without unexpected rendering bugs.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Exercises Summary](#exercises-summary)
- [Requirements & Standards](#requirements--standards)
- [How to Run](#how-to-run)
- [Core Concepts & Defense Insights](#core-concepts--defense-insights)
- [Special Guide: Markdown & Prompt Special Characters Escaping](#special-guide-markdown--prompt-special-characters-escaping)

---

## Project Overview
In modern smart farming, data streams continuously from IoT sensors monitoring soil pH, temperature, and greenhouse humidity. However, sensors fail, networks drop, and corrupted readings occur. This project moves beyond basic programming into agricultural data engineering, ensuring data integrity and system resilience so that unexpected errors never crash the entire infrastructure.

## Directory Structure
```text
py02/
├── ex0/
│   └── ft_first_exception.py
├── ex1/
│   └── ft_raise_exception.py
├── ex2/
│   └── ft_different_errors.py
├── ex3/
│   └── ft_custom_errors.py
└── ex4/
    └── ft_finally_block.py
```

## Exercises Summary

### Exercise 0: Agricultural Data Validation (`ex0/`)
- **File:** `ft_first_exception.py`
- **Concept:** Basic data validation and catching exceptions.
- **Description:** Implements an `input_temperature` function that converts string sensor inputs into integers. The test suite demonstrates catching a `ValueError` when invalid data (like `"abc"`) is supplied, ensuring the application handles the anomaly gracefully without crashing.

### Exercise 1: Agricultural Data Validation Pipeline (`ex1/`)
- **File:** `ft_raise_exception.py`
- **Concept:** Raising exceptions manually using `raise`.
- **Description:** Enhances the validation layer by checking if the temperature falls within a realistic botanical threshold (0°C to 40°C, limits included). If a reading is outside bounds, it raises a `ValueError` with custom warnings (`too hot` / `too cold`) to be handled by the caller.

### Exercise 2: Different Types of Problems (`ex2/`)
- **File:** `ft_different_errors.py`
- **Concept:** Handling multiple distinct exception types.
- **Description:** Demonstrates the generation and containment of 4 core built-in exception types: `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, and `TypeError`. Shows how to map errors individually and catch them collectively inside a single tuple block.

### Exercise 3: Making Your Own Error Types (`ex3/`)
- **File:** `ft_custom_errors.py`
- **Concept:** Object-Oriented Exception Hierarchy & Domain-Specific Errors.
- **Description:** Defines custom exception classes using inheritance: `GardenError` (Base) -> `PlantError` and `WaterError` (Derived). Demonstrates polymorphism by catching multiple domain errors via their shared parent class type.

### Exercise 4: Finally Block - Always Clean Up (`ex4/`)
- **File:** `ft_finally_block.py`
- **Concept:** Resource management and the `finally` block mechanics.
- **Description:** Simulates an automated plant watering routine that requires strict initialization and shutdown cycles. Proves that the `finally` block guarantees resource cleanup (closing the water valves) even when an operation triggers a `PlantError` and prematurely invokes a `return` statement.

---

## Requirements & Standards
- **Runtime:** Python 3.10+
- **Linter:** Strict conformance to `flake8` standards.
- **Type Hints:** Explicit type annotations for all functions and parameters, verified using `mypy`.
- **Robustness:** Programs must handle exceptions cleanly; unexpected crashes are strictly disallowed.

## How to Run

Give execution permissions to the scripts and run them directly:
```bash
chmod +x ex*/*.py

# Run individual modules
./ex0/ft_first_exception.py
./ex1/ft_raise_exception.py
./ex2/ft_different_errors.py
./ex3/ft_custom_errors.py
./ex4/ft_finally_block.py
```

To verify code quality and static typing:
```bash
flake8 .
mypy .
```

---

## Core Concepts & Defense Insights

### 1. Why use Domain-Specific Custom Errors?
Using generic errors like `ValueError` globally makes it hard to pinpoint the true source of an issue. Creating custom structures like `WaterError` prevents false positive error captures and makes logs self-explanatory during real-world automated farming monitoring.

### 2. The Mechanics of the `finally` Block and PVM Interception
When a `return` or `break` statement is reached inside a `try` or `except` block, the Python Virtual Machine (PVM) does not immediately destroy the frame. It hoards the return value on its temporary stack, pauses the execution context switch, jumps into the `finally` suite to run cleanups (e.g., locking hardware switches or closing file descriptors), and only then resumes the termination path.

---

## Special Guide: Markdown & Prompt Special Characters Escaping

When documenting technical architectures or crafting precise AI prompts, special characters (Markdown syntaxes) can inadvertently trigger rendering or logic bugs. Prefixing these characters with a backslash (`\`) neutralizes their behavior, ensuring they display as literal text.

### Special Characters Escaping Reference

| Character | Meaning / Markdown Use | Escaped Syntax | Mitigation / Common Bug |
| :---: | :--- | :--- | :--- |
| **`#`** | Heading / Header level | `\#` | Prevents lines from turning into massive text headers when used at the start. |
| **`*`** | Emphasis (Bold/Italic), Lists | `\*` | Prevents text from italicizing or converting into a bullet point. |
| **`_`** | Emphasis (Bold/Italic) | `\_` | **Critical for Python:** Multiple underscores like `__init__` will break and turn text bold if not escaped. |
| **`` ` ``** | Inline Code / Code Block | `\`` | Blocks text from turning into a monospace code block format. |
| **`-`** | Bulleted List / Dash | `\-` | Prevents negative signs or dividers from generating unintended lists. |
| **`>`** | Blockquote | `\>` | Prevents lines from being trapped inside a gray blockquote container. |
| **`!`** | Image designation | `\!` | Stops the parser from treating combination with `[]` as an image asset. |
| **`[]`** | Link Text / Arrays | `\[` & `\]` | Avoids triggering unintended hyperlinking structures. |
| **`()`** | Link URL / Function Arguments | `\(` & `\)` | Prevents argument lists from accidentally linking out. |

### Practical Example (Python Context)
- **Problem:** Writing `__init__ method utilizes _ variable` unescaped will accidentally render as: **init** method utilizes *variable* (hiding the syntax).
- **Solution:** Writing `\_\_init\_\_ method utilizes \_ variable` enforces clean literal text output.

<br>
<br>

---
---

# Garden Guardian - スマート農業のためのデータエンジニアリング (Version 2.0)

**Garden Guardian** へようこそ！本プロジェクトは、スマート農業におけるデータ監視システムの構築を想定し、障害に強い（フォールトトレラントな）データパイプラインを設計するためのモジュールです。Pythonの例外処理を駆使し、IoTセンサーの異常、データの破損、インフラの不具合に直面してもクラッシュしないデジタル温室システムの実装を学びます。

また、このバージョン2.0では、テクニカルドキュメント（README）の執筆や、AIへの正確な指示出し（プロンプトエンジニアリング）において表示崩れや誤動作を防ぐために必須となる**「Markdown特殊文字のエスケープガイド」**を統合しています。

---

## 目次
- [プロジェクト概要](#プロジェクト概要-1)
- [ディレクトリ構造](#ディレクトリ構造-1)
- [課題（Exercise）一覧](#課題exercise一覧)
- [共通規約・検証ツール](#共通規約検証ツール)
- [実行方法](#実行方法-1)
- [核心概念とディフェンス対策](#核心概念とディフェンス対策-1)
- [特別ガイド: Markdown＆プロンプト特殊文字のエスケープ](#特別ガイド-markdownプロンプト特殊文字のエスケープ)

---

## プロジェクト概要
近代的なスマートファームでは、土壌pH、温度、湿度を測定するIoTセンサーから絶え間なくデータがストリームされます。しかし、現場ではセンサーの故障、ネットワークの切断、不正な入力値などの問題が日常茶飯事です。本プロジェクトでは、単に動くコードを書くだけでなく、想定外の事態をエレガントに受け流し、システム全体のクラッシュを防ぐデータエンジニアリングの本質を習得します。

## ディレクトリ構造
```text
py02/
├── ex0/
│   └── ft_first_exception.py
├── ex1/
│   └── ft_raise_exception.py
├── ex2/
│   └── ft_different_errors.py
├── ex3/
│   └── ft_custom_errors.py
└── ex4/
    └── ft_finally_block.py
```

## 課題（Exercise）一覧

### Exercise 0: Agricultural Data Validation (農業データの検証) (`ex0/`)
- **ファイル:** `ft_first_exception.py`
- **概念:** 例外処理の基礎、`try/except` によるキャッチ。
- **内容:** 文字列として受信したセンサーデータを整数型に変換する `input_temperature` を実装。 `"abc"` などの不正なデータが混入した際に発生する `ValueError` を捕捉し、クラッシュを回避する基礎を学びます。

### Exercise 1: Agricultural Data Validation Pipeline (データ検証パイプライン) (`ex1/`)
- **ファイル:** `ft_raise_exception.py`
- **概念:** `raise` キーワードを用いた意図的な例外の発生。
- **内容:** 前回のデータ変換に加え、植物の生育に適した温度（0°C 〜 40°C、上限・下限含む）の範囲チェックを追加。しきい値を超えた異常値を検出した際、自ら `ValueError` を発生させて呼び出し元に安全に通知します。

### Exercise 2: Different Types of Problems (多様なエラーへの対応) (`ex2/`)
- **ファイル:** `ft_different_errors.py`
- **概念:** 複数の異なる例外型の識別と一括処理。
- **内容:** システム内で起きうる4つの代表的なエラー（`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `TypeError`）を意図的に発生させます。それぞれを個別に識別してログを吐き出す処理と、タプルを用いて一括でキャッチする手法を実装します。

### Exercise 3: Making Your Own Error Types (独自例外の作成) (`ex3/`)
- **ファイル:** `ft_custom_errors.py`
- **概念:** オブジェクト指向（OOP）の継承関係を利用した例外の階層化。
- **内容:** 組み込みエラーに頼らず、ドメイン専用の例外 `GardenError`（親クラス）、およびそれを継承した `PlantError`, `WaterError`（子クラス）を定義します。親クラスの網を仕掛けることで、配下の子クラスエラーをポリモーフィズム（多態性）によって一括回収する挙動を実証します。

### Exercise 4: Finally Block - Always Clean Up (確実なリソースクリーンアップ) (`ex4/`)
- **ファイル:** `ft_finally_block.py`
- **概念:** `finally` ブロックによる実行保証メカニズム。
- **内容:** 散水システムの初期化とシャットダウンをシミュレートします。関数内部のループ処理中にエラーが起きて即座に `return` で関数を抜け出そうとした場合でも、`finally` ブロックが割り込んで必ずシステムの終了処理（バルブの閉鎖）を実行することを確認します。

---

## 共通規約・検証ツール
- **言語環境:** Python 3.10以上
- **スタイル規約:** `flake8` 標準規約への完全準拠。
- **型ヒント:** すべての関数・メソッドの引数および戻り値に対する型ヒントの義務化（`mypy` による検証）。
- **堅牢性:** どのような異常データが入力されてもプログラムが途中で異常終了しないこと。

## 実行方法

スクリプトに実行権限を付与し、直接実行してください。
```bash
chmod +x ex*/*.py

# 各モジュールの実行
./ex0/ft_first_exception.py
./ex1/ft_raise_exception.py
./ex2/ft_different_errors.py
./ex3/ft_custom_errors.py
./ex4/ft_finally_block.py
```

コード品質および型ヒントのチェックを行う場合：
```bash
flake8 .
mypy .
```

---
