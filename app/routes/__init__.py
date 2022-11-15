from flask import render_template, redirect, url_for, session, flash, request
from app.auth import login_required
from app import app
from app.forms import LoginForm, PersonForm
from app.handlers import delete_person, get_person_by_id, user_validate, get_all_persons, add_person


@app.route('/')
@app.route('/index')
@login_required
def index():
    if request.method == 'GET' and request.args.get('delete'):
        delete_person(request.args.get('delete'))
        flash('Se ha eliminado el empleado', 'success')
    return render_template('index.html', titulo="Inicio", persons=get_all_persons())


@app.route('/add', methods=['GET'])
@login_required
def get_add_person():
    person_form = PersonForm()
    return render_template('add_persona.html', titulo="Agregar persona", person_form=person_form)


@app.route('/add', methods=['POST'])
@login_required
def post_add_person():
    person_form = PersonForm(data={})
    if person_form.cancel.data:
        return redirect(url_for('index'))
    if person_form.validate_on_submit():
        new_person = {'first_name': person_form.first_name.data, 'last_name': person_form.last_name.data,
                      'phone': person_form.phone.data}
        add_person(new_person)
        flash('Se ha agregado una nueva persona', 'success')
        return redirect(url_for('index'))


@app.route('/edit-person/<int:person_id>', methods=['GET'])
@login_required
def get_edit_person(person_id):
    person_form = PersonForm(data=get_person_by_id(person_id))
    return render_template('edit_person.html', titulo="Persona editar", person_form=person_form)


@app.route('/edit-person/<int:person_id>', methods=['POST'])
@login_required
def post_edit_person(person_id):
    person_form = PersonForm(data=get_person_by_id(person_id))
    if person_form.cancel.data:
        return redirect(url_for('index'))
    if person_form.validate_on_submit():
        person_data = {'first_name': person_form.first_name.data, 'last_name': person_form.last_name.data,
                       'phone': person_form.phone.data}
        delete_person(person_id)
        add_person(person_data)
        flash('Se ha editado exitosamente la persona', 'success')
        return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = login_form.user.data
        password = login_form.password.data
        if user_validate(user, password):
            session['user'] = user
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Ops! credenciales icorrectas!', 'danger')
    return render_template('login.html', titulo="Login", login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
