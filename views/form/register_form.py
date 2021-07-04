from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('username ', validators=[DataRequired(message='用户名不能为空')])
    # 此条变量赋值语句加入了密码格式验证器，缺陷系统中使用下面相应的变量赋值，修改缺陷只需要调换注释位置即可。
    # password = PasswordField('password ', validators=[DataRequired(message='密码不能为空'),
    #                                                   Regexp('^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{8,16}$',
    #                                                          message='密码不符合要求，需要8-16位且包含大小写字母和数字')])
    password = PasswordField('password ', validators=[DataRequired(message='密码不能为空')])
    repwd = PasswordField('repeat your password ',
                          validators=[DataRequired(message='密码不能为空'), EqualTo('password', message='两次输入的密码不相同')])
    register = SubmitField('register')
