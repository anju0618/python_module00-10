The Codex: Mastering Python's Import Mysteries

An alchemical laboratory project designed to explore and master the intricate mechanics of Python's packaging and import system. Developed with Python 3.10+, adhering to strict flake8 standards and mypy type annotations.

📂 Project Structure

.
├── elements.py                 # Root elements (Fire, Water)
├── ft_alembic_0.py             # Basic import verification
├── ft_alembic_1.py             # Basic 'from...import' verification
├── ft_alembic_2.py             # Nested import validation
├── ft_alembic_3.py             # Nested 'from...import' validation
├── ft_alembic_4.py             # Namespace encapsulation & intentional AttributeError
├── ft_alembic_5.py             # Namespace alias validation
├── ft_distillation_0.py        # Potion brewing with mixed elements
├── ft_distillation_1.py        # Package-level alias calling
├── ft_kaboom_0.py              # Light magic (Circular dependency avoided)
├── ft_kaboom_1.py              # Dark magic (Intentional circular dependency explosion)
├── ft_transmutation_0.py       # Direct transmutation script
├── ft_transmutation_1.py       # Sub-package routing verification
├── ft_transmutation_2.py       # Top-level routing verification
└── alchemy/                    # Base Package
    ├── __init__.py             # Public API Gateway for the alchemy package
    ├── elements.py             # Package elements (Earth, Air)
    ├── potions.py              # Brewing formulas with nested references
    ├── grimoire/               # Magic Spellbook Sub-package
    │   ├── __init__.py         # Gateway to Grimoire
    │   ├── dark_spellbook.py   # Circular import trigger
    │   ├── dark_validator.py   # Circular validator
    │   ├── light_spellbook.py  # Local import protection logic
    │   └── light_validator.py  # Light validator
    └── transmutation/          # Transmutation Sub-package
        ├── __init__.py         # Gateway to Transmutation
        └── recipes.py          # Absolute and Relative import mixes


🧪 Alchemical Mysteries Solved

1. Package Initialization & Encapsulation (Part I)

We control the public API of the alchemy package using __init__.py.

Elements like create_air are publicly exposed.

Elements like create_earth are hidden from the package root, intentionally raising an AttributeError when accessed incorrectly.

2. Nested Import & Namespace Aliasing (Part II)

Demonstrates pulling modules from different scopes (root and nested packages) and registering them under short, convenient aliases like alchemy.heal for better usability.

3. Absolute vs. Relative Pathing (Part III)

Features a combination of:

Absolute Import: from alchemy.potions import strength_potion (resolves relative to sys.path)

Relative Import: from ..elements import create_air (resolves relative to the module's path in the package)

4. Avoiding the Circular Dependency "Explosion" (Part IV)

Dark Magic (dark_spellbook): Triggers a fatal recursive loop by having both files import each other at the top-level during initial module loading.

Light Magic (light_spellbook): Avoids the recursive loop by utilizing Local Imports (importing within functions), deferring evaluation until the functions are called.

⚙️ How to Verify

1. Execute Test Suites

Run the verification scripts located in the root directory:

python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py  # Expected to crash on Attribute Error
python3 ft_alembic_5.py
python3 ft_distillation_0.py
python3 ft_distillation_1.py
python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py   # Expected to crash on ImportError


2. Quality and Standards Control

# Check syntax with Flake8
flake8 .

# Check static types with Mypy
mypy .
# Note: ft_alembic_4.py is expected to raise a single error on purpose (accessing a hidden attribute).


3. About # noqa Annotations

In some scripts (__init__.py files and ft_kaboom_1.py), we intentionally used # noqa comments.

In __init__.py, this is used to prevent flake8 from complaining about unused imports (F401), which is standard practice when exposing endpoints in package initialization files.

In ft_kaboom_1.py, we deferred importing to the end of the file to allow outputs to print first. # noqa: E402, F401, E501 is applied to bypass style guidelines for this deliberate showcase of tracebacks.

コーデックス: Pythonインポートの謎をマスターする

Pythonのパッケージング、名前空間、インポートシステムの深奥な仕組みを理解し、制御するために作られたアルケミー（錬金術）テーマの学習用プロジェクトです。Python 3.10+で構築され、厳格な flake8 コーディングスタイルおよび mypy 静的型注釈に準拠しています。

📂 プロジェクト構成

上記英語セクションの Project Structure を参照してください。すべてのスクリプト、パッケージ、ネストされたサブモジュールが配置されています。

🧪 解決された4つのインポートの謎

1. パッケージの初期化と隠蔽（Part I）

__init__.py を使用して alchemy パッケージの外部向けAPIをコントロールしています。

create_air などの関数は外部公開されます。

create_earth などの内部関数は意図的にパッケージトップレベルから隠蔽され、不適切なアクセスに対して AttributeError を発生させます。

2. ネストされたインポートとエイリアス登録（Part II）

プロジェクトルートのモジュールとパッケージ内のネストされたモジュールを呼び出すテクニックを学び、alchemy.heal のような、呼び出しやすく洗練されたパッケージレベルのエイリアス（別名）を構築します。

3. 絶対パス vs 相対パス（Part III）

プロジェクト内で以下の2つのインポートを混在させ、挙動の違いを理解します：

絶対インポート: from alchemy.potions import strength_potion (sys.path を起点として解決)

相対インポート: from ..elements import create_air (現在のモジュール位置を起点として解決)

4. 循環参照による「大爆発」の回避（Part IV）

闇の魔術 (dark_spellbook): 相互にモジュールのトップレベル（起動時）でインポートし合うことで無限ループを発生させ、意図的に ImportError を起こします。

光の魔術 (light_spellbook): 関数の中でインポートを行う 「ローカルインポート（関数内インポート）」 を活用し、評価を遅延させることでこの爆発を完璧に回避します。

⚙️ 検証方法

1. テストスクリプトの実行

ルートディレクトリから以下のスクリプトを個別に実行してください：

python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py  # 意図的にAttributeErrorでクラッシュします
python3 ft_alembic_5.py
python3 ft_distillation_0.py
python3 ft_distillation_1.py
python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py   # 意図的にImportErrorでクラッシュします


2. 規格チェック

# コーディングスタイルのチェック (flake8)
flake8 .

# 型注釈のチェック (mypy)
mypy .
# ※注意: ft_alembic_4.py は非公開の属性にアクセスするため、意図通り1つのエラーを報告します。


3. コード内にある # noqa について

プロジェクトの __init__.py および ft_kaboom_1.py で、意図的に # noqa コメントを使用しています。

各 __init__.py では、パッケージの仲介役としてインポートを行っているため、flake8 の未使用警告（F401）を無視させる必要があり、これはPythonパッケージ開発における一般的なプラクティスです。

ft_kaboom_1.py では、標準出力を画面に表示した後にクラッシュさせるという仕様を満たすため、コードの末尾でインポートを行っています。この意図的なフォーマットを許可するために # noqa: E402, F401, E501 を使用しています。