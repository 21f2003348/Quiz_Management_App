from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from master.student import Student

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        student = Student.query.filter_by(name=username_to_check.data).first()
        if student:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = Student.query.filter_by(username=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Email(), DataRequired()])
    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class SubjectForm(FlaskForm):
    name = StringField(label='Subject Name:', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField(label='Submit')

class ChapterForm(FlaskForm):
    chapter_name = StringField('Chapter Name', validators=[DataRequired()])
    subject = SelectField('Subject', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Chapter')

    def __init__(self, *args, **kwargs):
        super(ChapterForm, self).__init__(*args, **kwargs)


class QuizForm(FlaskForm):
    title = StringField('Quiz Title:', validators=[DataRequired()])
    subject = SelectField('Subject', coerce=int, validators=[DataRequired()])  # To be populated with subjects
    chapter = SelectField('Chapter', coerce=int, validators=[DataRequired()])  # To be populated with chapters
    submit = SubmitField('Add Quiz')


class QuestionForm(FlaskForm):
    chapter = SelectField('Chapter', coerce=int, validators=[DataRequired()])  # To be populated with chapters

    subject = SelectField('Subject', coerce=int, validators=[DataRequired()])  # To be populated with subjects

    text = TextAreaField(label='Question Text:', validators=[DataRequired()])
    answer = StringField(label='Correct Answer:', validators=[DataRequired()])
    quiz = SelectField('Quiz', coerce=int, validators=[DataRequired()])  # To be populated with quizzes
    submit = SubmitField(label='Submit')
