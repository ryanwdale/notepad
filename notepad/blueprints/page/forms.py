from flask import Flask, make_response, render_template, session
from flask_wtf import Form, csrf
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField
from lib.util_wtforms import ModelForm


class PostForm(ModelForm):
    title = StringField('Title')
    body = CKEditorField('Body')
    save = SubmitField('Save')
    save_evernote = SubmitField('Save To Evernote')
