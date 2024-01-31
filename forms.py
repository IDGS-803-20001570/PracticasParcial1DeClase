from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField

class distanciaPuntos(Form):
    X1=IntegerField('X1')
    X2=IntegerField('X2')
    Y1=IntegerField('Y1')
    Y2=IntegerField('Y2')
