from wtforms import Form
from wtforms import StringField,SelectField,RadioField,EmailField,IntegerField
from wtforms import validators

class diccionarioDatos(Form):
    palabraIngles= StringField('palabraIngles',[
        validators.DataRequired(message='Es necesario ingresar una palabra')
    ])
    palabraEspañol= StringField('palabraEspañol',[
        validators.DataRequired(message='Es necesario ingresar una palabra')
    ])
class diccionarioDatosResp(Form):
    palabraBuscada= StringField('palabraBuscada',[
        validators.DataRequired(message='Es necesario ingresar una palabra')
    ])
    idioma = RadioField('idioma', choices=[(1, 'Ingles'), (2, 'Español')])


class distanciaPuntos(Form):
    X1=IntegerField('X1')
    X2=IntegerField('X2')
    Y1=IntegerField('Y1')
    Y2=IntegerField('Y2')

class horoscopoChino(Form):
    ANIO=StringField('ANIO')

class signoZodiacal(Form):
    dia=StringField('dia')
    mes = SelectField('Mes',
    choices=[
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre')
    ])


class calculaResistencias(Form):
    color1=SelectField('color1',
    choices=[
        ('0','Negro'),
        ('1','Cafe'),
        ('2','Rojo'),
        ('3','Naranja'),
        ('4','Amarillo'),
        ('5','Verde'),
        ('6','Azul'),
        ('7','Violeta'),
        ('8','Gris'),
        ('9','Blanco')
    ])  
    
    color2=SelectField('color2',
    choices=[
        ('0','Negro'),
        ('1','Cafe'),
        ('2','Rojo'),
        ('3','Naranja'),
        ('4','Amarillo'),
        ('5','Verde'),
        ('6','Azul'),
        ('7','Violeta'),
        ('8','Gris'),
        ('9','Blanco')
    ])
    color3=SelectField('color3',
    choices=[
        ('1','Negro'),
        ('10','Cafe'),
        ('100','Rojo'),
        ('1000','Naranja'),
        ('10000','Amarillo'),
        ('100000','Verde'),
        ('1000000','Azul'),
        ('10000000','Violeta'),
        ('100000000','Gris'),
        ('1000000000','Blanco')
    ])    
    