from django import forms
from .store import Store

store = Store()


class MenuForm(forms.Form):
    options = forms.ChoiceField(required=True,
                                widget=forms.RadioSelect(
                                    attrs={'class': 'Radio'}),
                                choices=(('1', "Print Items in store"),
                                         ('2', "Print Items in Cart"),
                                         ('3', "Add Item to Cart"),
                                         ('4', "Remove Item from Cart"),
                                         ('5', "Checkout"),))


class AddForm(forms.Form):
    items = store.items
    items = forms.ChoiceField(required=True,
                              widget=forms.RadioSelect(
                                  attrs={'class': 'Radio'}),
                              choices=(('1', str(items[0].name) + ': ' + str(items[0].description) + ' $' +
                                        str(items[0].price)),
                                       ('2', str(items[1].name) + ': ' + str(items[1].description) + ' $' +
                                        str(items[1].price)),
                                       ('3', str(items[2].name) + ': ' + str(items[2].description) + ' $' +
                                        str(items[2].price)),
                                       ('4', str(items[3].name) + ': ' + str(items[3].description) + ' $' +
                                        str(items[3].price)),))
    quantity = forms.IntegerField(required=True)


class RemoveForm(forms.Form):
    items = store.items
    items = forms.ChoiceField(required=True,
                              widget=forms.RadioSelect(
                                  attrs={'class': 'Radio'}),
                              choices=(('1', str(items[0].name) + ': ' + str(items[0].description) + ' $' +
                                        str(items[0].price)),
                                       ('2', str(items[1].name) + ': ' + str(items[1].description) + ' $' +
                                        str(items[1].price)),
                                       ('3', str(items[2].name) + ': ' + str(items[2].description) + ' $' +
                                        str(items[2].price)),
                                       ('4', str(items[3].name) + ': ' + str(items[3].description) + ' $' +
                                        str(items[3].price)),))
    quantity = forms.IntegerField(required=True)
