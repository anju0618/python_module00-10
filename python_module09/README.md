# 🌌 Cosmic Data Observatory - Pydantic Data Validation

This repository contains a series of data validation exercises focused on handling cosmic data streams using Python 3.10\_+ and **Pydantic v2.x**.

---

## 🚀 Project Overview

The Cosmic Data Observatory processes vital statistics, alien contact reports, and crew configurations across the universe. The core mission is to ensure data integrity using modern Python data validation techniques.

### 📋 Requirements & Coding Standards
* **Python Version:** 3.10 or later 
* **Coding Standard:** `flake8` compliance 
* **Type Annotations:** Comprehensive strict type checking verified via `mypy` 
* **Package Manager:** `pip` within virtual environments (`venv`, `virtualenv`, or `conda`) 
* **Validation Library:** Pydantic 2.x (utilizing `@model_validator` instead of the deprecated `@validator`) 

---

## 📁 Repository Structure

```text
.
├── ex0/
│   └── space_station.py
├── ex1/
│   └── alien_contact.py
└── ex2/
    └── space_crew.py
```

## 🛠️ Exercises Detail

### Exercise 0: Space Station Data (`ex0/`)
* **Objective:** Basic Pydantic model creation with `BaseModel` and `Field` validation.
* **Fields Validated:** `station_id` (3\-10 chars), `name` (1\-50 chars), `crew_size` (1\-20), `power_level` (0.0\-100.0%), `oxygen_level` (0.0\-100.0%), `last_maintenance` (DateTime), `is_operational` (Boolean, default: True), and `notes` (Optional, max 200 chars).

### Exercise 1: Alien Contact Logs (`ex1/`)
* **Objective:** Master custom multi-field validation using `@model_validator(mode='after')`.
* **Enums:** `ContactType` (`radio`, `visual`, `physical`, `telepathic`).
* **Custom Business Rules Implemented:**
  * `contact_id` must start with `"AC"`
  * Physical contact reports must be verified (`is_verified = True`)
  * Telepathic contact requires at least 3 witnesses
  * Strong signals ($>7.0$) must include a received message

### Exercise 2: Space Crew Management (`ex2/`)
* **Objective:** Master nested Pydantic models and complex safety logic.
* **Enums:** `Rank` (`cadet`, `officer`, `lieutenant`, `captain`, `commander`).
* **Custom Safety Rules Implemented:**
  * Mission ID must start with `"M"`
  * Must have at least one Commander or Captain on board
  * Long missions ($> 365$ days) require at least 50\% experienced crew members ($\ge 5$ years of experience)
  * All assigned crew members must be currently active

---
---

# 🛠️ 各課題の詳細

### Exercise 0: Space Station Data (`ex0/`)
* **目的:** `BaseModel` と `Field` バリデーションを用いた基本的な Pydantic モデル作成の習得。
* **検証対象:** `station_id` (3\-10文字), `name` (1\-50文字), `crew_size` (1\-20人), `power_level` (0.0\-100.0%), `oxygen_level` (0.0\-100.0%), `last_maintenance` (日時情報), `is_operational` (真偽値, デフォルト: True), `notes` (任意項目, 最大200文字)。

### Exercise 1: Alien Contact Logs (`ex1/`)
* **目的:** `@model_validator(mode='after')` を用いた、複数フィールドにまたがるカスタムビジネスロジックの検証。
* **列挙型 (Enum):** `ContactType` (`radio`, `visual`, `physical`, `telepathic`)。
* **実装したカスタムルール:**
  * `contact_id` は必ず `"AC"` で始まること
  * 物理的接触（`physical`）の報告は、必ず検証済み（`is_verified = True`）であること
  * テレパシーによる接触（`telepathic`）には、最低3人以上の目撃者が必要
  * 強力な信号（$>7.0$）を受信した場合は、メッセージ内容が必須

### Exercise 2: Space Crew Management (`ex2/`)
* **目的:** ネストされた Pydantic モデルの検証と、複雑な安全要件バリデーションの習得。
* **列挙型 (Enum):** `Rank` (`cadet`, `officer`, `lieutenant`, `captain`, `commander`)。
* **実装したカスタム安全ルール:**
  * ミッションIDは必ず `"M"` で始まること
  * 船内に最低1名以上の 統括者（Commander）または 船長（Captain）が搭乗していること
  * 長期ミッション（$> 365$日）では、経験年数5年以上のベテラン乗組員が全体の 50\% 以上を占めること
  * アサインされたすべての乗組員が活動状態（`is_active = True`）であること