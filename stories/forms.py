import calendar
from django import forms
from stories.models import Story
from crispy_forms import helper, layout
from ckeditor.widgets import CKEditorWidget
from crispy_forms.bootstrap import PrependedText
from crispy_forms.layout import Fieldset, Field


class StoryForm(forms.ModelForm):

    project = forms.CharField(required=False, label="Project Name or Description",
        help_text="The first project you contributed to.",
    )
    project_description = forms.CharField(required=False,
        help_text="Just a quick description, in case the project isn't famous."
    )
    vcs = forms.ChoiceField(required=False, label="Version Control Used",
        choices = [('', '-')]+Story.CHOICES_VCS,
    )
    year = forms.ChoiceField(required=False, help_text="(approximately)",
        choices = [('', '-')]+[(year, year) for year in xrange(2013, 1959, -1)],
    )
    month = forms.ChoiceField(required=False, help_text="&nbsp;",
        choices = [('', '-')]+zip(xrange(0,13), list(calendar.month_name)),
    )
    experience = forms.CharField(
        #placeholder="Why? How much work? Who did you talk to?",
        widget=CKEditorWidget()
    )
    skill_professional = forms.ChoiceField(required=False,
        label = "Professional",
        choices = [('', '-')]+Story.CHOICES_ASSESS,
        help_text = "Professional experience",
    )
    skill_language = forms.ChoiceField(required=False,
        label = "Technical",
        choices = [('', '-')]+Story.CHOICES_ASSESS,
        help_text = "Ability with skills required"
    )
    skill_vcs = forms.ChoiceField(required=False,
        label = "Version Control",
        choices = [('', '-')]+Story.CHOICES_ASSESS,
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
        widget=forms.TextInput(attrs={'plagceholder': "BDFL, core, contributor"})
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
            Fieldset('What year did you make your first contribution?',
                Field('year'),
                Field('month'),
                Field('project', css_class='part-width'),
                layout.HTML('<br /><br />'),
                Field('vcs'),
                layout.HTML('<br /><br />'),
            ),
            Fieldset('About you',
                Field('preferred_name', css_class='part-width'),
                Field('full_name', css_class='part-width'),
                layout.HTML('<br />'),
                PrependedText('github', 'github/', placeholder="[username]"),
                PrependedText('twitter', '@', placeholder="twitter"),
                layout.HTML('<div>&nbsp;</div>'),
                Field('website', css_class='full-width'),
                Field('other', css_class='full-width'),
                layout.HTML('<div>&nbsp;</div>'),
                Field('known_as_1', placeholder="BDFL, core, contributor"),
                Field('for_project_1', placeholder="for Project/s"),
                layout.HTML('<br />'),
                Field('known_as_2', placeholder="BDFL, core, contributor"),
                Field('for_project_2', placeholder="for Project/s"),
                layout.HTML('<br /><br /><br />'),
            ),
            Fieldset('"Self Assessed" skill level the first time you contributed to Free Software:',
                Field('skill_language'),
                Field('skill_professional'),
                Field('skill_vcs'),
                layout.HTML('<br /><br />'),
            ),
            Fieldset('Story about the experience (why, how much work, who was involved, annecdotes):',
                'experience',
            ),
        )
