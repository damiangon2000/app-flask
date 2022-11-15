from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    user = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    send = SubmitField('Iniciar sesión', render_kw={'class': 'btn btn-dark'})


class PersonForm(FlaskForm):
    first_name = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    last_name = StringField('Apellido', validators=[DataRequired('Este campo es requerido')])
    phone = StringField('Telefono', validators=[])
    send = SubmitField('Guardar', render_kw={'class': 'btn btn-dark'})
    cancel = SubmitField('Cancelar', render_kw={'class': 'btn btn-danger', 'formnovalidate': 'True'})

