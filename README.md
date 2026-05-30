# 🐍 Python 3.10+: Module 03 (Data Quest)

This repository contains production-grade solutions for **Module 03: Mastering Python Collections**. The primary objective of this module is to transition from basic sequential arrays to advanced, memory-efficient data structures (Lists, Tuples, Sets, and Dictionaries) while writing resilient, fully type-hinted code in a simulated gaming environment.

---

## 🛠️ Strict Engineering Standards

All scripts contained within this project strictly adhere to the following enterprise-level constraints mandated by the evaluation guidelines:
1. **Coding Standard:** 100% compliance with `flake8` syntax and style checking (strict 79-character line limit / E501).
2. **Static Type Analysis:** Zero warnings under `mypy` strict type-checking across all functions and methods.
3. **Robustness:** Complete elimination of runtime crashes through proactive exception management (`try-except` blocks).
4. **I/O Constraints:** Zero File I/O operations allowed; all data processing occurs entirely in-memory or via `sys.argv`.

---

## 📂 Repository Structure & Project Summary

### 🎮 ex0: Command Quest (`ex0/ft_command_quest.py`)
* **Core Concept:** Low-level command-line argument manipulation via `sys.argv`.
* **Technical Highlights:** Implements slicing-free pointer operations to extract raw execution paths and isolate target arguments without causing unnecessary heap memory allocations.

### 📊 ex1: Score Cruncher (`ex1/ft_score_analytics.py`)
* **Core Concept:** Algorithmic data filtering and mathematical computing using `list`.
* **Technical Highlights:** Employs the EAFP (Easier to Ask for Forgiveness than Permission) approach via `try-except ValueError` blocks to cleanly split valid numeric game scores from human-input errors. Calculates mathematical variance and bounds in O(N) linear time.

### 📐 ex2: Position Tracker (`ex2/ft_coordinate_system.py`)
* **Core Concept:** Handling immutable data frames via `tuple`.
* **Technical Highlights:** Utilizes read-only 3-element float tuples to lock spatial variables (X, Y, Z), leveraging tuple unpacking features for clean mathematical processing using the Euclidean distance formula.

### 🏆 ex3: Achievement Hunter (`ex3/ft_achievement_tracker.py`)
* **Core Concept:** Set operations and relationship analysis via `set`.
* **Technical Highlights:** Harnesses underlying hash-tables to perform rapid unique matrix processing (`union`, `intersection`, `difference`) across multiple players' tracking profiles in O(1) average lookup complexity. Addresses the E501 linting constraint via implicit line continuation within brackets.

### 🎒 ex4: Inventory Master (`ex4/ft_inventory_system.py`)
* **Core Concept:** Fast lookup mapping via `dict` structures.
* **Technical Highlights:** Parses custom key-value pairs formatted as string arguments (`item:quantity`) into an active tracking structure. Implements an inline lambda expression (`key=lambda k: inventory[k]`) to guarantee structural int evaluation for min/max functions, completely bypassing type-inference bugs inside static checkers.

### 🧙‍♂️ ex5: Stream Wizard (`ex5/ft_data_stream.py`)
* **Core Concept:** Memory-isolated asynchronous streaming pipelines via `typing.Generator` and `yield`.
* **Technical Highlights:** Replaces standard buffer caching with state-preserving generator execution pipelines. Achieves a fixed O(1) spatial footprint by evaluating individual structural changes lazily. Showcases mutable pointer manipulation through the synchronized subtraction of references from an active array wrapper.

---

## 🧠 Core Defense Concepts & Architecture Q&A

### Q1: Why prioritize implicit line continuation over explicit backslashes (`\`) for PEP 8 compliance?
Explicit backslashes (`\`) create brittle code states; accidental trailing spaces immediately trigger invalid syntax exceptions. Utilizing open block boundaries (such as inside round or square brackets) signals the PVM to safely process logical code segments across lines without adding unsafe escape characters.

### Q2: What explains the memory advantage of `yield` over standard arrays?
Standard list compositions allocate large contiguous memory buffers upfront to house all elements simultaneously. In contrast, `yield` structures return custom generator objects that freeze runtime states, local scopes, and execution pointers on the stack. The function runs only when actively polled via a `next()` trigger, evaluating a single isolated object before returning to a paused state.

### Q3: How do lists and tuples behave differently during parameter passing?
In Python, lists are mutable wrappers passed by reference; altering the structure inside a nested routine directly modifies the underlying memory block in the parent scope. Conversely, tuples act as read-only constants; their structural dimensions and indices are sealed at creation, preventing unauthorized modification during runtime operations.

---
<br>

# 🐍 Python 3.10+: Module 03 (Data Quest)

このリポジトリには、**Module 03: Mastering Python Collections** のすべての課題に対する完全なソリューションが含まれています。本モジュールの主な目的は、単純なシーケンシャル配列から、メモリ効率に優れた高度なデータ構造（リスト、タプル、集合、辞書）への移行を理解し、ゲーム分析環境を模した堅牢で型ヒントが完全なコードを構築することにあります。

---

## 🛠️ 厳格なコーディング基準

本プロジェクトに含まれるすべてのスクリプトは、評価ガイドラインで義務付けられている以下のエンタープライズレベルの制約に完全に準拠しています。
1. **コーディング標準:** `flake8` による構文およびスタイルのチェックに100%準拠（厳格な79文字制限 / E501）。
2. **静的型解析:** すべての関数とメソッドにおいて、`mypy` の厳格な型チェックによる警告がゼロであること。
3. **堅牢性:** `try-except` ブロックによる予防的な例外管理を通じて、ランタイムクラッシュを完全に排除。
4. **I/O 制約:** ファイルのI/O操作は一切禁止。すべてのデータ処理はメモリ内、または `sys.argv` 経由で行われます。

---

## 📂 リポジトリ構造 & プロジェクト概要

### 🎮 ex0: Command Quest (`ex0/ft_command_quest.py`)
* **コア概念:** `sys.argv` を用いた低レイヤのコマンドライン引数操作。
* **技術的特徴:** スライスによる新たなメモリ確保を行わず、インデックス参照を用いて実行パスの抽出と対象引数の分離を $O(1)$ で行い、不要なヒープメモリの割り当てを防いでいます。

### 📊 ex1: Score Cruncher (`ex1/ft_score_analytics.py`)
* **コア概念:** `list` を用いたアルゴリズムによるデータフィルタリングと統計計算。
* **技術的特徴:** `try-except ValueError` ブロックを用いた EAFP（許可を求めるより許しを請う方が簡単）アプローチを採用。人間の入力ミスから有効な数値ゲームスコアを綺麗に分離し、計算量 $O(N)$ の線形時間で統計値を算出します。

### 📐 ex2: Position Tracker (`ex2/ft_coordinate_system.py`)
* **コア概念:** `tuple` を用いた不変データフレームのハンドリング。
* **技術的特徴:** 空間変数（X, Y, Z）を固定するために読み取り専用の3要素フローティングタプルを利用。タプルのアンパック代入機能を活かし、ユークリッド距離の数式をクリーンに処理します。

### 🏆 ex3: Achievement Hunter (`ex3/ft_achievement_tracker.py`)
* **コア概念:** `set` 構造を用いた集合演算と関係性分析。
* **技術的特徴:** ハッシュテーブルを裏側に持つ集合を活用し、複数プレイヤーの実績プロファイル間でのユニークマトリックス処理（`union`, `intersection`, `difference`）を平均計算量 $O(1)$ で高速に処理します。丸括弧内での暗黙の行継続により、E501規約をクリアしています。

### 🎒 ex4: Inventory Master (`ex4/ft_inventory_system.py`)
* **コア概念:** `dict` 構造による高速ルックアップマッピング。
* **技術的特徴:** `item:quantity` 形式の文字列引数を有効な追跡用辞書にパース。`key=lambda k: inventory[k]` というインラインラムダ式を実装することで、`max/min` 関数において `int` としての構造的な評価を保証し、静的解析器の型推論バグを完全にバイパスしています。

### 🧙‍♂️ ex5: Stream Wizard (`ex5/ft_data_stream.py`)
* **コア概念:** `typing.Generator` と `yield` によるメモリ分離型の非同期ストリーミングパイプライン。
* **技術的特徴:** 標準的なバッファキャッシュを排除し、状態を保持するジェネレータ実行パイプラインに置き換えています。各変更要素を遅延評価（Lazy Evaluation）することで、メモリ計算量 $O(1)$ の固定フットプリントを達成。また、関数に渡された可変オブジェクトの参照（ポインタ）から要素を直接 `remove` していく、破壊的な同期処理の実証を行っています。

---

## 🧠 ディフェンス（査定）対策：アーキテクチャ Q&A

### Q1: PEP 8準拠において、なぜ明示的なバックスラッシュ（`\`）よりも暗黙の行継続を優先するのか？
明示的なバックスラッシュ（`\`）は、その直後に偶発的なスペースが混入するだけで `SyntaxError` を引き起こす脆弱なコード状態を作ります。一方で、丸括弧 `()` や角括弧 `[]` などのブロック境界を開いた状態にすることは、PVM（Python仮想マシン）に安全な論理行の継続を伝えるシグナルとなり、危険なエスケープ文字を排除できるためです。

### Q2: 標準的なリスト配列に対する `yield` のメモリ的な優位性とは？
通常のリスト内包表記などは、全要素を同時に格納するために巨大な連続メモリバッファを事前に確保します。これに対し、`yield` を用いたジェネレータ構造は、関数の実行状態、ローカルスコープ、スタック上の実行ポインタを凍結したカスタムオブジェクトを返します。関数は `next()` トリガーによってアクティブに要求された時のみ動作し、1つの孤立したオブジェクトを評価して再び一時停止（フリーズ）するため、メモリを一切圧迫しません。

### Q3: 引数として渡される際、リストとタプルはどのように挙動が異なるか？
Pythonにおいて、リストは可変（Mutable）オブジェクトであり「参照渡し（アドレスの受け渡し）」が行われます。そのため、入れ子になったルーチン内部で構造を変更すると、親スコープの基盤にあるメモリブロックが直接書き換わります。対照的に、タプルは不変（Immutable）の定数として振る舞い、生成時にその構造的次元とインデックスが完全にシールドされるため、実行中の予期せぬ改ざんを防ぐことができます。
