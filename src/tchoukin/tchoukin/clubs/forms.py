from django import forms
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit, Button, Hidden, Div, HTML
from crispy_forms.bootstrap import FormActions, AppendedText, PrependedAppendedText
from models import Club


class ClubForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'add-form ajax-form'
        self.helper.form_action = reverse('save_club')
        self.helper.layout = Layout(
            Fieldset(
                _(u'Add your TchoukPoint'),
                Field('name'),
                Field('website'),
                Field('email'),
                Field('address_address', readonly='readonly', css_class='addresspicker_address', placeholder='drag the flag on the map'),
            ),
            Fieldset(
                _(u'Localization'),
                Field('address_lat', readonly='readonly', css_class='addresspicker_lat'),
                Field('address_lon', readonly='readonly', css_class='addresspicker_lng'),
                Field('address_country', css_class='addresspicker_country'),
                Field('address_locality', css_class='addresspicker_locality'),
                Field('address_province', css_class='addresspicker_administrative_area_level_2'),
                Field('address_postal_code', css_class='addresspicker_postal_code'),
                Field('address_address_without_number', css_class='addresspicker_route'),
                Field('address_address_number', css_class='addresspicker_street_number'),
                css_class='hide',
            ),
            FormActions(
                Submit('save-and-continue', 'Save'),
            )
        )
        return super(ClubForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Club
        fields = [
            'name',
            'website',
            'email',
            'address_address',
            'address_lat',
            'address_lon',
            'address_country',
            'address_locality',
            'address_province',
            'address_postal_code',
            'address_address_without_number',
            'address_address_number',
        ]
