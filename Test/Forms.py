#coding:utf-8

from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='账号', max_length=256,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password = forms.CharField(label='', widget=forms.TextInput())
    password = forms.CharField(label='口令', widget=forms.TextInput(attrs={'class': 'form-control','type': 'password'}))

class RegistForm(forms.Form):
    username = forms.CharField(label='账号', max_length=256, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='口令', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    confirm_password = forms.CharField(label='确认', max_length=256, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
