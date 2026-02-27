from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField # type: ignore
from  wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User

class CadastroForm(FlaskForm):
    def validate_username(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro nome de usuário")

    def validate_email(self, check_email):
        email = User.query.filter_by(usuario=check_email.data).first()
        if email:
            raise ValidationError("E-mail já existe! Cadastre outro E-mail")

    def validate_senha(self, check_senha):
        senha = User.query.filter_by(usuario=check_senha.data).first()
        if senha:
            raise ValidationError("senha já existe! Cadastre outra senha")

    usuario = StringField(label='Username: ' , validators=[Length(min=4, max=30) , DataRequired( ) ])
    email = StringField(label = 'E-mail: ' , validators=[Email() ,DataRequired() ])
    senha1 = PasswordField(label='Senha: ', validators=[Length(min=6),DataRequired() ])
    senha2 = PasswordField(label='Confirmação de Senha: ' , validators=[EqualTo('senhal') ,DataRequired( ) ])
    submit=SubmitField(label='Cadastrar')

