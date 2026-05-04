from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , SelectField
from wtforms.validators import DataRequired , URL

class AddingForm(FlaskForm):
    cafe_name = StringField('Cafe Name' , validators=[DataRequired()])
    location = StringField('Location' , validators=[DataRequired() , URL()])
    open = StringField('Opening Time' , validators=[DataRequired()])
    close = StringField('Closing Time' , validators=[DataRequired()])
    coffee = SelectField(
        'Coffee Ratings', 
        choices=[("☕️", "☕️"), ("☕️☕️", "☕☕"), ("☕️☕️☕️", "☕☕☕"), ("☕️☕️☕️☕️", "☕☕☕☕"), ("☕️☕️☕️☕️☕️", "☕☕☕☕☕")], 
        validators=[DataRequired()]
    ) 
    wifi = SelectField(
        'Wifi Ratings', 
        choices=[("✘", "✘"), ("💪", "💪"), ("💪💪", "💪💪"), ("💪💪💪", "💪💪💪"), ("💪💪💪💪", "💪💪💪💪"), ("💪💪💪💪💪", "💪💪💪💪💪")], 
        validators=[DataRequired()]
    ) 
    power = SelectField(
        'Power Ratings', 
        choices=[("✘", "✘"), ("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"), ("🔌🔌🔌🔌", "🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")], 
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')