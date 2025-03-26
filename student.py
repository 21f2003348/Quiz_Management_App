from master import db, login_manager
from master import bcrypt
from flask_login import UserMixin
from master import app
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    def __repr__(self):
        return f'Admin {self.name}'

    @property
    def password(self):
        return self.password

    def check_password_correction(self, attempted_password):
        return (self.password_hash == attempted_password)
    # def buy(self, user):
    #     self.owner = user.id
    #     user.budget -= self.price
    #     db.session.commit()

    # def sell(self, user):
    #     self.owner = None
    #     user.budget += self.price
    #     db.session.commit()

# with app.app_context():

