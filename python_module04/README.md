# Cyber Archives - Digital Preservation System

Welcome to the **Cyber Archives** repository. In the year 2087, humanity's most precious treasure is data. This project implements a series of robust, pythonic file operation utilities designed by a Data Archivist to recover, transform, and securely store fragile digital knowledge before it vanishes into the digital void.

## Project Overview
This repository contains four progressive exercises focused on mastering Python's low-level and high-level file operations, stream management, and safe resource handling under strict standard requirements.

### Standard Requirements
All implementations strictly adhere to the following digital preservation guidelines:
* **Python 3.10+** syntax and features.
* **Flake8** linter standards compliance for clean, readable code.
* Strict **mypy** type hint verification across all methods and functions.
* Graceful exception handling to prevent runtime system crashes.

---

## Directory & Exercise Structure

.
├── ex0/
│   └── ft_ancient_text.py       # Ancient Text Recovery Utility
├── ex1/
│   └── ft_archive_creation.py   # 2087-Compatible Protocol Encoder
├── ex2/
│   └── ft_stream_management.py  # Sacred Channels Management System
└── ex3/
    └── ft_vault_security.py     # Secure Context Manager Vault

### Exercise 0: Ancient Text Recovery (ex0/)
* **Objective:** Emulate the core functionality of the system `cat` command to access and retrieve data from legacy storage vaults.
* **Key Concept:** Manual resource management (`open()`, `read()`, `close()`) enclosed within comprehensive `try-finally` blocks to prevent resource leaks. It answers the core archivist question: `open()` in text mode returns an instance of `io.TextIOWrapper` (aliased as `typing.TextIO`).

### Exercise 1: Archive Creation (ex1/)
* **Objective:** Extract recovered text records, process the structure, and transition them into a 2087-compatible protocol by appending a specialized `#` marker to each line.
* **Key Concept:** Functional separation. Segregating the data restoration process from the interactive storage prompt (`input()`), with automated data truncation/overwrite (`"w"` mode) options.

### Exercise 2: Stream Management (ex2/)
* **Objective:** Direct interaction with the three foundational standard system streams without utilizing generic high-level builtins.
* **Key Concept:** System routing. Standard input is read directly via `sys.stdin.readline().rstrip('\n')`, while all system exceptions and error logs are properly piped into the standard error stream (`sys.stderr`) using a distinct `[STDERR]` prefix to guarantee monitoring visibility.

### Exercise 3: Vault Security (ex3/)
* **Objective:** Design an airtight, atomic file-access API called `secure_archive()` using advanced Python guardrails.
* **Key Concept:** **Context Managers (`with` statement)**. The function enforces parameter selection for `"read"` or `"write"` actions, safely abstracting away potential `OSError` states into a clean status tuple: `(bool, content_or_error)`.

---

## Technical Defense Cheat Sheet
During the evaluation defense, be prepared to demonstrate and explain:
1. **The `with` Statement Advantage:** It implements the RAII (Resource Acquisition Is Initialization) pattern. Even if an exception triggers mid-operation, the context manager guarantees the file descriptor is implicitly closed, eliminating data corruption risks.
2. **Stream Separation:** Keeping `stdout` and `stderr` separated ensures that administrative diagnostic errors do not contaminate the pristine stream of recovered archive data.

***

# サイバーアーカイブ - デジタル保存システム

**サイバーアーカイブ（Cyber Archives）** リポジトリへようこそ。西暦2087年、人類の最大の宝はデータです。本プロジェクトは、データアーキビストとして、脆弱な digital 知識がデジタルの虚無へと消え去る前に、それらを復旧・加工・安全に保護するための堅牢なファイル操作ユーティリティ群をPythonで実装したものです。

## プロジェクト概要
本リポジトリは、Pythonにおける低級・高級ファイル操作、ストリーム管理、そして厳格な標準要件下での安全なリソースハンドリングをマスターするための4つの段階的な演習で構成されています。

### 共通コーディング規約
すべての実装は、以下のデジタル保存ガイドラインに厳格に準拠しています：
* **Python 3.10以上**の構文および機能の使用。
* クリーンで読みやすいコードを維持するための **flake8** リンター基準の遵守。
* すべての方法と関数に対する、**mypy** による厳格な型ヒントの検証。
* システムの強制終了を防ぎ、優雅にエラーを処理する例外ハンドリング。

---

## ディレクトリと演習構造

.
├── ex0/
│   └── ft_ancient_text.py       # 古代テキスト復旧ユーティリティ
├── ex1/
│   └── ft_archive_creation.py   # 2087互換プロトコルエンコーダー
├── ex2/
│   └── ft_stream_management.py  # 聖なるデータチャネル管理システム
└── ex3/
    └── ft_vault_security.py     # セキュリティ・コンテキストマネージャー・ヴォルト

### Exercise 0: Ancient Text Recovery (古代テキストの復旧) (ex0/)
* **目的:** システムの `cat` コマンドのコア機能をエミュレートし、遺されたストレージヴォルトからデータにアクセスして復旧します。
* **重要概念:** リソースの手動管理（`open()`, `read()`, `close()`）を包括的な `try-finally` ブロックで囲み、リソースリークを完全に防ぎます。なお、テキストモードにおける `open()` の返り値の型は `io.TextIOWrapper`（`typing.TextIO`）です。

### Exercise 1: Archive Creation (アーカイブの作成) (ex1/)
* **目的:** 復旧したテキストレコードを抽出し、各行の末尾に特殊な `#` マーカーを付与して2087年互換のプロトコルへと変換・保存します。
* **重要概念:** 関数の役割の分離。データ復旧プロセスと、インタラクティブな保存先入力（`input()`）のロジックを分離し、既存ファイルの自動上書き・置換（`"w"` モード）に対応させます。

### Exercise 2: Stream Management (ストリーム管理) (ex2/)
* **目的:** 汎用的な組み込み関数（`input`など）を使わずに、システムの根幹である3つの標準データチャネルを直接制御します。
* **重要概念:** システムルーティング。標準入力は `sys.stdin.readline().rstrip('\n')` から直接読み込み、システム例外やエラーログは明確に `[STDERR]` プレフィックスを付与して標準エラー出力（`sys.stderr`）へとパイプライン出力することで、システムの監視性を保証します。

### Exercise 3: Vault Security (ヴォルトのセキュリティ) (ex3/)
* **目的:** Pythonの高度な安全装置を利用し、気密性の高いアトミックなファイルアクセスAPI `secure_archive()` を設計します。
* **重要概念:** **コンテキストマネージャー（`with` 文）**。この関数は、開発者に `"read"` または `"write"` のアクション選択を強制し、発生し得るすべての `OSError` を安全にキャッチして、クリーンなステータスタプル `(bool, 戻り値文字列またはエラー内容)` として返します。

---

## ディフェンス（口頭試問）対策チェックシート
評価（ディフェンス）の際は、以下の概念を自信を持って説明できるようにしてください：
1. **`with` 文の優位性について:** これは RAII（Resource Acquisition Is Initialization）パターンを実装したものです。ブロックの途中でどのような例外が発生しようとも、コンテキストマネージャーがファイル記述子を暗黙的かつ確実に閉じることを保証するため、データの破損リスクを排除できます。
2. **ストリーム分離の意義:** `stdout` と `stderr` を分離しておくことで、管理用の診断エラーログが、復旧された純粋なアーカイブデータのストリームを汚染することを防ぐことができます。
