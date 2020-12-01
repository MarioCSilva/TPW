from django import forms


class BookQueryForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=100)


class AuthorQueryForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=100)


class AutPubQueryForm(forms.Form):
    aut = forms.CharField(label='Search Book by Author:', max_length=100, required=False)
    pub = forms.CharField(label='Search Book by Publisher:', max_length=100, required=False)


class login(forms.Form):
    aut = forms.CharField(label='Search Book by Author:', max_length=100, required=False)
    pub = forms.CharField(label='Search Book by Publisher:', max_length=100, required=False)
