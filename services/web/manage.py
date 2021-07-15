"""
Management file
"""
from flask.cli import FlaskGroup
from project import db, app


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db() -> None:
    """
    Database creation function
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("drop_db")
def drop_db() -> None:
    """
    Database delete function
    """
    db.drop_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
