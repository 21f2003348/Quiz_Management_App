from master import app
from master.forms import ChapterForm  # Import the ChapterForm

from flask import render_template, redirect, url_for, flash, request, abort, jsonify

from master.student import Student, Admin
from master.forms import RegisterForm, LoginForm, SubjectForm, ChapterForm, QuizForm, QuestionForm
from master.subject import Subject, Chapter, Quiz, Question
from master import db
from flask_login import current_user
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function

from flask_login import login_user, logout_user, login_required, current_user

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Student(username=form.username.data,
                              name=form.name.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('student_dashboard'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_student = Student.query.filter_by(username=form.username.data).first()
        attempted_admin = Admin.query.filter_by(username=form.username.data).first()
        if attempted_student and attempted_student.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_student)
            flash(f'Success! You are logged in as: {attempted_student.username}', category='success')
            return redirect(url_for('student_dashboard'))
        elif attempted_admin and attempted_admin.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_admin)
            flash(f'Success! You are logged in as: {attempted_admin.username}', category='success')
            return redirect(url_for('admin_dashboard'))  
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/admin/create_subject', methods=['GET', 'POST'])
def create_subject():
    form = SubjectForm()
    if form.validate_on_submit():
        subject = Subject(name=form.name.data)
        db.session.add(subject)
        db.session.commit()
        flash('Subject created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('create_subject.html', form=form)

@app.route('/admin/create_chapter', methods=['GET', 'POST'])
def create_chapter():
    form = ChapterForm()
    
    # Populate subject choices
    subjects = Subject.query.all()
    form.subject.choices = [(subject.id, subject.name) for subject in subjects]
    
    if form.validate_on_submit():

        chapter = Chapter(
            name=form.chapter_name.data,
            subject_id=form.subject.data
        )
        db.session.add(chapter)
        db.session.commit()
        flash('Chapter created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
        
    return render_template('create_chapter.html', form=form)

@app.route('/admin/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    form = QuizForm()

    # # Populate subject choices
    # subjects = Subject.query.all()
    # form.subject.choices = [(subject.id, subject.name) for subject in subjects]

    # Fetch all chapters for the chapter dropdown
    chapters = Chapter.query.all()
    form.chapter.choices = [(chapter.id, chapter.name) for chapter in chapters]

    if form.validate_on_submit():
        quiz = Quiz(
            title=form.title.data, 
            chapter_id=form.chapter.data
        )
        db.session.add(quiz)
        db.session.commit()

        flash('Quiz created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('create_quiz.html', form=form)

@app.route('/admin/create_question', methods=['GET', 'POST'])
def create_question():
    form = QuestionForm()
    
    # Populate subject choices
    subjects = Subject.query.all()
    form.subject.choices = [(subject.id, subject.name) for subject in subjects]

        # Fetch chapters based on selected subject
    chapters = Chapter.query.all()
    form.chapter.choices = [(chapter.id, chapter.name) for chapter in chapters]


    # Populate quiz choices based on selected chapter
    if form.subject.data:
        chapters = Chapter.query.filter_by(subject_id=form.subject.data).all()
        form.chapter.choices = [(chapter.id, chapter.name) for chapter in chapters]
        
        quizzes = Quiz.query.all()
        form.quiz.choices = [(quiz.id, quiz.title) for quiz in quizzes]

        if form.chapter.data:
            print(1)
            quizzes = Quiz.query.filter_by(chapter_id=form.chapter.data).all()
            form.quiz.choices = [(quiz.id, quiz.title) for quiz in quizzes]
        else:
            form.quiz.choices = []  # Clear quiz choices if no chapter is selected


    # Populate chapter choices based on selected subject
    if form.validate_on_submit():
        chapters = Chapter.query.filter_by(subject_id=form.subject.data).all()
        form.chapter.choices = [(chapter.id, chapter.name) for chapter in chapters]

        question = Question(
            text=form.text.data,
            answer=form.answer.data,
            quiz_id=form.quiz.data,
            option1=form.option1.data,
            option2=form.option2.data,
            option3=form.option3.data,
            option4=form.option4.data
        )

        db.session.add(question)
        db.session.commit()
        flash('Question created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('create_question.html', form=form)

@app.route('/get_chapters/<int:subject_id>', methods=['GET'])
def get_chapters(subject_id):
    chapters = Chapter.query.filter_by(subject_id=subject_id).all()
    return jsonify([(chapter.id, chapter.name) for chapter in chapters])

@app.route('/get_quizzes/<int:chapter_id>', methods=['GET'])
def get_quizzes(chapter_id):
    quizzes = Quiz.query.filter_by(chapter_id=chapter_id).all()
    return jsonify([(quiz.id, quiz.title) for quiz in quizzes])
