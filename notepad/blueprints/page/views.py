from flask import request, Blueprint, render_template, redirect
from notepad.blueprints.page.forms import PostForm
from flask_login import current_user
from notepad.blueprints.user.models import Notes, db, User
from evernote.api.client import EvernoteClient
from evernote.edam.type import ttypes
from instance.settings import DEV_TOKEN

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/', methods=['GET', 'POST'])
def home():
    form = PostForm()
    if form.validate_on_submit() and form.save_evernote:
        db.drop_all()
        db.create_all()

    elif form.validate_on_submit():
        n = Notes(title=form.title.data, body=form.body.data, user_id=current_user.id)
        n.save()
        db.session.add(n)
        db.session.commit()
        if form.save_evernote:
            client = EvernoteClient(token=DEV_TOKEN)

            noteStore = client.get_note_store()
            note = ttypes.Note()
            nBody = '<?xml version="1.0" encoding="UTF-8"?>'
            nBody += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
            nBody += '<en-note>%s</en-note>' % form.body.data
            note.title = form.title.data
            note.content = nBody
            noteStore.createNote(DEV_TOKEN, note)


    return render_template('page/home.html', form=form)

