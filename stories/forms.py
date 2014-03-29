import calendar
from django import forms
from stories.models import Story
from crispy_forms import helper, layout
from ckeditor.widgets import CKEditorWidget
from crispy_forms.bootstrap import PrependedText
from crispy_forms.layout import Fieldset, Field, ButtonHolder, Button, Submit

NONE_TEXT = ' ---'

class StoryForm(forms.ModelForm):

    project = forms.CharField(required=False,
        label="Project Name or Description",
        help_text="The first project you contributed to.",
    )
    project_description = forms.CharField(required=False,
        help_text="Just a quick description, in case the project isn't famous."
    )
    vcs = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(), choices = Story.CHOICES_VCS,
        required=False, label="Version Control Used",
    )
    comms = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(), choices = Story.CHOICES_COMMS,
        required=False, label="Communication Methods",
    )
    vcs_other = forms.CharField(required=False, label='',
        widget=forms.TextInput(attrs={'placeholder': "Other: SCCS, RSC"})
    )
    comms_other = forms.CharField(required=False, label='',
        widget=forms.TextInput(attrs={'placeholder': "Other"})
    )
    year = forms.ChoiceField(required=False, help_text="&nbsp;",
        choices = [('', NONE_TEXT)]+[(year, year) for year in xrange(2013, 1959, -1)],
    )
    month = forms.ChoiceField(required=False, help_text="&nbsp;",
        choices = [('', NONE_TEXT)]+zip(xrange(0,13), list(calendar.month_name)),
    )
    experience = forms.CharField(required=False,
        #placeholder="Why? How much work? Who did you talk to?",
        widget=CKEditorWidget()
    )
    skill_professional = forms.ChoiceField(required=False,
        label = "Professional",
        choices = [('', NONE_TEXT)]+Story.CHOICES_ASSESS,
        help_text = "Professional experience",
    )
    skill_language = forms.ChoiceField(required=False,
        label = "Technical",
        choices = [('', NONE_TEXT)]+Story.CHOICES_ASSESS,
        help_text = "Ability with skills required"
    )
    skill_vcs = forms.ChoiceField(required=False,
        label = "Version Control",
        choices = [('', NONE_TEXT)]+Story.CHOICES_ASSESS,
        help_text = "Knowledge of VCS used",
    )

    preferred_name = forms.CharField(required=False)
    full_name = forms.CharField(required=False)
    github = forms.CharField(required=False, label=' ')
    twitter = forms.CharField(required=False, label=' ')
    website = forms.URLField(required=False)
    other = forms.URLField(required=False,
        label = "Another URL",
    )
    known_as_1 = forms.CharField(required=False, label="Known as",
        widget=forms.TextInput(attrs={'placeholder': "BDFL, core, contributor"})
    )
    for_project_1 = forms.CharField(required=False, label="for Project/s")
    known_as_2 = forms.CharField(required=False, label="Known as",
        widget=forms.TextInput(attrs={'placeholder': "BDFL, core, contributor"})
    )
    for_project_2 = forms.CharField(required=False, label="for Project/s")

    class Meta:
        model = Story

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.helper = helper.FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = layout.Layout(
            Fieldset('What year did you make your first contribution? (approximately)',
                Field('year'),
                Field('month'),
                #layout.HTML('<br /><br />'),
                Field('project', css_class='part-width'),
                #Field('project_description', css_class='full-width'),
            # ),
            # Fieldset('What form of Version Control did you use?',
                layout.HTML('<br />'),
                Field('vcs'),
                Field('comms'),
                layout.HTML('<br />'),
                Field('vcs_other'),
                Field('comms_other'),
                layout.HTML('<br /><br />'),
                # 'vcs_other',
            ),
            Fieldset('About you',
                layout.HTML('''<p><strong>All fields are optional.</strong> No information provided here will be redistributed or used for any other purpose than displaying on this website.<br />Although your story nearly certainly won't pass moderation if you don't give us an idea of who you are.</p>'''),
                Field('preferred_name', css_class='part-width'),
                Field('full_name', css_class='part-width'),
                layout.HTML('<br />'),
                PrependedText('github', 'github/', placeholder="[username]"),
                PrependedText('twitter', '@', placeholder="twitter"),
                layout.HTML('<div>&nbsp;</div>'),
                Field('website', css_class='full-width'),
                Field('other', css_class='full-width'),
                # ),
                # Fieldset(' ',
                layout.HTML('<div>&nbsp;</div>'),
                Field('known_as_1', placeholder="BDFL, core, contributor"),
                Field('for_project_1', placeholder="for Project/s"),
                layout.HTML('<br />'),
                'known_as_2',
                'for_project_2',
                layout.HTML('<br /><br /><br />'),
            ),
            Fieldset('"Self Assessed" skill level the first time you contributed to Free Software:',
                Field('skill_language'),
                Field('skill_professional'),
                Field('skill_vcs'),
                layout.HTML('<br /><br />'),
            ),
            Fieldset('Story about the experience',
                layout.HTML('<p><strong>Why</strong> did you get involved? How much work was involved (hopefully not much for your first commit!)?<br>'),
                layout.HTML('How did you get in contact with the project? Who was involved? Did anything interesting happen?<br>'),
                layout.HTML('Why did you keep contributing?</p>'),
                'experience',
            ),
            ButtonHolder(
                Button('preview', 'Preview', css_class='preview btn btn-primary'),
                Submit('submit', 'Submit', css_class='btn btn-primary'),
                Button('reset', 'Cancel', css_class='btn')
            )
        )


    def clean(self, *args, **kwargs):
        clean_data = super(StoryForm, self).clean(*args, **kwargs)
        for k,v in clean_data.iteritems():
            if v == u'':
                clean_data[k] = None
                #raise Exception(clean_data)

        if clean_data['vcs']:
            clean_data['vcs'] = ', '.join(clean_data['vcs'])

        if clean_data['comms']:
            clean_data['comms'] = ', '.join(clean_data['comms'])

        return clean_data


    #     # check name unique
    #     name = clean_data.get('name')
    #     person = Person.objects.filter(name=name)
    #     if person:
    #         raise forms.ValidationError('Yo, that name is taken ~')

    #     # check event exists
    #     event = Event.objects.filter(current=True)
    #     if not event:
    #         raise forms.ValidationError("Hey! There aren't any current events. Go tell an organiser to activate an event.")
    #     return clean_data
