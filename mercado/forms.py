from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, PasswordField, SubmitField # type: ignore
from  wtforms.validators import Length, EqualTo, Email, DataRequired


class CadastroForm(FlaskForm):
    usuario = StringField(label='Username: ' , validators=[Length(min=4, max=30) , DataRequired( ) ])
    email = StringField(label = 'E-mail: ' , validators=[Email() ,DataRequired() ])
    senha1 = PasswordField(label='Senha: ', validators=[Length(min=6),DataRequired() ])
    senha2 = PasswordField(label='Confirmação de Senha: ' , validators=[EqualTo('senhal') ,DataRequired( ) ])
    submit=SubmitField(label='Cadastrar')
