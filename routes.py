from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from models import db
from models import Task

main = Blueprint("main", __name__)


# 一覧画面
@main.route("/")
def index():

    tasks = Task.query.order_by(
        Task.status.asc(),
        Task.priority.desc(),
        Task.due_date.is_(None),
        Task.due_date.asc(),
        Task.created_at.desc()
    ).all()

    return render_template("list.html", tasks=tasks)


# 新規作成画面
@main.route("/create")
def create():
    return render_template("create.html")


# 新規作成処理
@main.route("/create", methods=["POST"])
def create_post():

    title = request.form.get("title", "").strip()
    description = request.form.get("description")
    due_date = request.form.get("due_date")
    priority = request.form.get("priority", "2")

    # title validation
    if not title:
        flash("タイトルは必須です")
        return redirect(url_for("main.create"))

    if len(title) > 100:
        flash("タイトルは100文字以内です")
        return redirect(url_for("main.create"))

    # priority validation
    if priority not in ["1", "2", "3"]:
        flash("優先度が不正です")
        return redirect(url_for("main.create"))

    # due_date validation
    due = None
    if due_date:
        try:
            due = datetime.strptime(
                due_date, "%Y-%m-%d"
            ).date()
        except ValueError:
            flash("日付形式が不正です")
            return redirect(url_for("main.create"))

    task = Task(
        title=title,
        description=description,
        due_date=due,
        priority=int(priority)
    )

    db.session.add(task)
    db.session.commit()

    return redirect(url_for("main.index"))


# 編集画面
@main.route("/edit/<int:id>")
def edit(id):

    task = Task.query.get_or_404(id)

    return render_template("edit.html", task=task)


# 編集処理
@main.route("/edit/<int:id>", methods=["POST"])
def edit_post(id):

    task = Task.query.get_or_404(id)

    title = request.form.get("title", "").strip()
    description = request.form.get("description")
    due_date = request.form.get("due_date")
    priority = request.form.get("priority")
    status = request.form.get("status")

    # title validation
    if not title:
        flash("タイトルは必須です")
        return redirect(url_for("main.edit", id=id))

    if len(title) > 100:
        flash("タイトルは100文字以内です")
        return redirect(url_for("main.edit", id=id))

    # priority validation
    if priority not in ["1", "2", "3"]:
        flash("優先度が不正です")
        return redirect(url_for("main.edit", id=id))

    task.title = title
    task.description = description
    task.priority = int(priority)

    # due_date validation
    if due_date:
        try:
            task.due_date = datetime.strptime(
                due_date, "%Y-%m-%d"
            ).date()
        except ValueError:
            flash("日付形式が不正です")
            return redirect(url_for("main.edit", id=id))
    else:
        task.due_date = None

    # status control
    if status == "1":
        task.mark_complete()
    else:
        task.mark_incomplete()

    db.session.commit()

    return redirect(url_for("main.index"))


# 削除
@main.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("main.index"))
