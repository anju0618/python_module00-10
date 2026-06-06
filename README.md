# The Codex: Mastering Python's Import System
This project is a practical laboratory designed to explore and master Python's packaging, namespace scoping, and import system. Developed with Python 3.10+, it fully complies with strict flake8 standards and mypy type annotations.

📂 Project Structure
```
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
├── ft_kaboom_0.py              # Circular dependency resolved (Local import)
├── ft_kaboom_1.py              # Circular dependency exception test
├── ft_transmutation_0.py       # Direct transmutation script
├── ft_transmutation_1.py       # Sub-package routing verification
├── ft_transmutation_2.py       # Top-level routing verification
└── alchemy/                    # Base Package
├── init.py             # Public API Gateway for the alchemy package
├── elements.py             # Package elements (Earth, Air)
├── potions.py              # Brewing formulas with nested references
├── grimoire/               # Sub-package (Imports handling)
│   ├── init.py         # Gateway to Grimoire
│   ├── dark_spellbook.py   # Circular import simulator
│   ├── dark_validator.py   # Circular validator
│   ├── light_spellbook.py  # Local import protection logic
│   └── light_validator.py  # Light validator
└── transmutation/          # Transmutation Sub-package
├── init.py         # Gateway to Transmutation
└── recipes.py          # Absolute and Relative import integration
```

🧪 Technical Concepts Implemented
1. Package Namespace Encapsulation (Part I)
Controlled the public interface of the alchemy package using init.py.

create_air is exposed to the public API.

create_earth remains encapsulated within the package submodule, raising an intentional AttributeError when external direct access is attempted.

2. Nested Imports & Namespace Aliasing (Part II)
Resolved scopes by importing modules from the root and nested packages. It exposes custom, clean entrypoints under the package level (e.g., alchemy.heal aliasing healing_potion).

3. Absolute vs. Relative Imports (Part III)
Demonstrated proper configuration of path resolution:

Absolute Import: from alchemy.potions import strength_potion (resolves relative to sys.path)

Relative Import: from ..elements import create_air (resolves relative to the current module's position within the package structure)

4. Resolving Circular Dependencies (Part IV)
Dark Package (dark_spellbook): Simulates a circular import collision. Both scripts reference each other at the module's root, causing an unresolvable initialization loop on import.

Light Package (light_spellbook): Resolves the loop using Local Imports inside functions, delaying the resolution of dependencies until execution time.

⚙️ Execution & Verification
1. Running the Test Suites
Validate the behavior of each module by executing the scripts in the root directory:

python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py  # Expected behavior: raises AttributeError on hidden element
python3 ft_alembic_5.py
python3 ft_distillation_0.py
python3 ft_distillation_1.py
python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py   # Expected behavior: raises ImportError due to circular dependency

2. Linter & Static Analysis
Check syntax and style with Flake8
flake8 .

Check static typing with Mypy
mypy .

Note: ft_alembic_4.py is expected to report a single attribute error on purpose.
3. Usage of # noqa Comments
In init.py files: Used # noqa: F401 (Unused Import) to expose subpackage modules at the package level without triggering unused variable warnings. This aligns with standard Python packaging practices.

In ft_kaboom_1.py: Utilized # noqa: E402, F401, E501` to safely load the module at the bottom of the script. This ensures the descriptive terminal logs print correctly before the planned import crash occurs.

コーデックス: Pythonインポートシステムの完全理解
本プロジェクトは、Pythonにおけるパッケージ化、名前空間のスコープ、およびインポートシステムの挙動を徹底検証するための開発環境です。Python 3.10以上で実装され、flake8 によるスタイル規約および mypy による厳格な静的型チェックをすべてパスしています。

📂 プロジェクト構成
上記英語セクションの Project Structure を参照してください。すべての検証用スクリプト、パッケージ、内部モジュールが破綻なく配置されています。

🧪 実装された技術的アプローチ
1. パッケージにおける名前空間のカプセル化 (Part I)
init.py を利用して、alchemy パッケージのパブリックインターフェースを厳格に制御。

create_air を外部APIとして公開。

create_earth をパッケージ内部にカプセル化し、外部からの不正な直接アクセスに対しては意図的に AttributeError を発生させます。

2. ネストされたインポートとエイリアスの定義 (Part II)
異なるスコープ（ルートディレクトリとネストされたパッケージ内）からモジュールを収集。パッケージレベルで利用可能な簡潔なショートカットエイリアス（例: alchemy.heal による healing_potion のバインド）を構築します。

3. 絶対パス vs 相対パス (Part III)
Pythonにおけるパス解決の挙動を正しく設計：

絶対インポート: from alchemy.potions import strength_potion (sys.path を起点として解決)

相対インポート: from ..elements import create_air (現在のモジュール位置を起点として解決)

4. 循環参照の回避手法 (Part IV)
Darkパッケージ (dark_spellbook): 相互インポートの衝突を検証。モジュールのトップレベルで互いを参照し合うことで、インポート処理時に強制的に初期化の無限ループ（ImportError）を引き起こします。

Lightパッケージ (light_spellbook): 関数内部でインポートを解決する ローカルインポート（関数内インポート） を採用。依存関係の解決を実行時まで遅延させ、循環参照の衝突を完全に回避します。

⚙️ 検証手順
1. テストスクリプトの実行
ルートディレクトリにある各検証用スクリプトを実行して挙動を確認します：

python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py  # 仕様：非公開関数へのアクセスのため AttributeError で終了
python3 ft_alembic_5.py
python3 ft_distillation_0.py
python3 ft_distillation_1.py
python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py   # 仕様：循環参照のインポートのため ImportError で終了

2. コード品質・静的解析の実行
Flake8によるコーディングスタイル検証
flake8 .

Mypyによる静的型検証
mypy .

※注意: ft_alembic_4.py は非公開属性へ直接アクセスするため、仕様として1つのエラーを検出します。
3. # noqa コメントに関する技術的背景
各 init.py ファイル: パッケージ全体の統合的なインポート（公開設定）を担うため、flake8 の未使用インポート警告（F401）を無効化しています。これはPythonにおける標準的なパッケージング設計です。

ft_kaboom_1.py: 例外でクラッシュする前に指定されたメッセージを画面に出力させるため、コードの最下部でインポートを実行。この意図的な制御のために # noqa: E402, F401, E501 を付与して検証をパスさせています。