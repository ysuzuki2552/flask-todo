# Flask ToDo App

Flaskで作成したシンプルな個人用ToDo管理アプリです。
AI駆動開発の学習目的として設計・実装しました。

---

# 概要

シンプルなToDo管理機能を提供するWebアプリです。

以下の機能を備えています：

* タスク作成
* タスク編集
* タスク削除
* 完了管理
* 優先度設定
* 期限設定
* 並び順制御

個人利用を想定したMVP構成です。

---

# 使用技術

* Python
* Flask
* SQLite
* SQLAlchemy
* HTML / CSS

---

# ディレクトリ構成

```
flask-todo
│
├── README.md
├── app.py
├── models.py
├── routes.py
│
├── templates
│   ├── base.html
│   ├── list.html
│   ├── create.html
│   └── edit.html
│
└── static
    └── style.css
```

---

# 機能一覧

## タスク管理

* タスク作成
* タスク編集
* タスク削除
* 完了/未完了管理

## タスク属性

* タイトル
* 説明
* 期限
* 優先度

---

# 並び順ロジック

以下の優先順位で並び替え

1. 未完了優先
2. 優先度（高→低）
3. 期限あり優先
4. 期限昇順
5. 作成日時降順

---

# バリデーション

| 項目   | 条件           |
| ---- | ------------ |
| タイトル | 必須           |
| タイトル | 100文字以内      |
| 優先度  | 1〜3          |
| 期限   | YYYY-MM-DD形式 |

---

# 環境構築

## 1. リポジトリクローン

```
git clone https://github.com/ysuzuki2552/flask-todo.git
cd flask-todo
```

---

## 2. 仮想環境作成

Windows

```
python -m venv venv
venv\Scripts\activate
```

Mac / Linux

```
python -m venv venv
source venv/bin/activate
```

---

## 3. 必要ライブラリインストール

```
pip install flask flask_sqlalchemy
```

---

## 4. アプリ起動

```
python app.py
```

---

## 5. ブラウザアクセス

```
http://127.0.0.1:5000
```

---

# DBについて

SQLiteを使用しています。
初回起動時に自動生成されます。

```
tasks.db
```

---

# テーブル定義

tasks

| カラム          | 型        |
| ------------ | -------- |
| id           | Integer  |
| title        | String   |
| description  | Text     |
| due_date     | Date     |
| priority     | Integer  |
| status       | Integer  |
| created_at   | DateTime |
| updated_at   | DateTime |
| completed_at | DateTime |

---

# 今後の改善予定

* ログイン機能
* タグ機能
* 検索機能
* ページネーション
* UI改善

---

# 学習ポイント

このアプリで学習した内容

* Flaskアプリ構成
* SQLAlchemy
* CRUD実装
* MVC設計
* バリデーション
* GitHub運用

---

# License

MIT License

---

# Author

AI駆動開発学習用として作成
