from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Book

class BookFrom(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['id', 'slug', 'published','created','updated']

    def __init__(self, *args, **kwargs):
        super(BookFrom, self).__init__(*args, **kwargs)
        self.fields['code'].error_messages = {
            'required':'Please enter book code',
        }
        self.fields['name'].error_messages = {
            'required':'Please enter book name',
        }
        self.fields['price'].error_messages = {
            'required':'Please enter book price',
            'invalid':'please enter a valid book price'
        }

    def clean(self):
        cd = super(BookFrom, self).clean()
        if not cd.get('category'):
            self.add_error('category', 'Please select category name')

        if not cd.get('author'):
            self.add_error('author', 'Please select author name')