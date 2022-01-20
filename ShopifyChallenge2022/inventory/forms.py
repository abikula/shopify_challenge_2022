from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField




class DeleteItemForm(FlaskForm):
    submit = SubmitField(label='Delete Item')

class EditForm(FlaskForm):
    submit = SubmitField(label = 'Finished Editing')

class UnDeleteItemForm(FlaskForm):
    submit = SubmitField(label='Undelete Item')


class AddForm(FlaskForm):
    name = StringField(label='Name:')
    description = StringField(label='Description:')
    submit = SubmitField(label='Add Item to Inventory')
