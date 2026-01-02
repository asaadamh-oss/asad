from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("اسم المستخدم", validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField("كلمة المرور", validators=[DataRequired()])
    submit = SubmitField("دخول")
