from inventory import app
from flask import render_template,request,redirect,url_for
from inventory import db
from inventory.models import Item
from inventory.forms import DeleteItemForm,UnDeleteItemForm
from inventory.forms import AddForm
from inventory.forms import EditForm


@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route("/inventory", methods = ['GET', 'POST'])
def view_inventory():
    delete_form = DeleteItemForm()
    edit_form = EditForm()
    undelete_form = UnDeleteItemForm()

    if request.method == "POST":
        #Delete Item Logic
        deleted_item = request.form.get('deleted_item')
        delete_comment = request.form.get('d_comment')
        d_item_object = Item.query.filter_by(name=deleted_item).first()
        if d_item_object:
            d_item_object.isDeleted = True
            if delete_comment:
                d_item_object.delete_comment = delete_comment
            db.session.commit()

        #Undelete Item Logic
        undelete_item = request.form.get('undelete_item')
        ud_item_object = Item.query.filter_by(name = undelete_item).first()
        if ud_item_object:
            ud_item_object.isDeleted = False
            ud_item_object.delete_comment = None
            db.session.commit()

        #Edit Item Logic
        edited_item = request.form.get('edited_item')
        edited_object = Item.query.filter_by(name = edited_item).first()
        if edited_object:
            new_name = request.form.get('new-name')
            new_stock = request.form.get('new-stock')
            new_description = request.form.get('new-description')

            if new_name:
                edited_object.name = new_name
            if new_stock:
                edited_object.stock = new_stock
            if new_description:
                edited_object.description = new_description
            db.session.commit()

        return redirect(url_for('view_inventory'))

    if request.method =="GET":
        items = Item.query.filter_by(isDeleted=False)
        d_items = Item.query.filter_by(isDeleted=True)
        return render_template('inventory.html', items=items, delete_form=delete_form,d_items = d_items, undelete_form = undelete_form, edit_form = edit_form)

@app.route('/additem',methods = ['GET', 'POST'])
def add_item():
    form = AddForm()
    if form.validate_on_submit():
        print('yo')
        item_to_create = Item(name = form.name.data, description = form.description.data)
        db.session.add(item_to_create)
        db.session.commit()
        return redirect(url_for('view_inventory'))

    return render_template('add_item.html', form=form)
