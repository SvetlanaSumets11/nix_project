from sqlalchemy import exc
from ..application import db


class Setting:
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
