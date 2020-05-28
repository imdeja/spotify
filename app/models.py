# import packages
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Data(db.Model):
    track_key = db.Column(db.BigInteger, primary_key=True)
    artist_name = db.Column(db.String)
    track_id = db.Column(db.String)
    track_name = db.Column(db.String)
    track_id = db.Column(db.String)


def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records