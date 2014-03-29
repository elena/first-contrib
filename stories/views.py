from django.views import generic
from django.core.urlresolvers import reverse_lazy
from stories.models import Story, Name, KnownFor
from stories.forms import StoryForm


class QuerySetMixin(object):

    model = Story


class StoryAddView(QuerySetMixin, generic.edit.FormView):

    paginate_by = 10
    form_class = StoryForm
    success_url = reverse_lazy('story_success')
    template_name = 'forms.html'

    def form_valid(self, form):
        name = Name()
        name.preferred_name = form.cleaned_data.get('preferred_name')
        name.full_name = form.cleaned_data.get('full_name')
        name.github = form.cleaned_data.get('github')
        name.twitter = form.cleaned_data.get('twitter')
        name.website = form.cleaned_data.get('website')
        name.other = form.cleaned_data.get('other')
        name.save()

        if not (form.cleaned_data.get('known_as_1') == None
            and form.cleaned_data.get('for_project_1') == None):
            kf1 = KnownFor(name=name)
            kf1.role = form.cleaned_data.get('known_as_1')
            kf1.project = form.cleaned_data.get('for_project_1')
            kf1.save()

        if not (form.cleaned_data.get('known_as_2') == None
            and form.cleaned_data.get('for_project_2') == None):
            kf2 = KnownFor(name=name)
            kf2.role = form.cleaned_data.get('known_as_2')
            kf2.project = form.cleaned_data.get('for_project_2')
            kf2.save()

        form.instance.name = name
        form.instance.save()
        return super(StoryAddView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StoryAddView, self).get_context_data(**kwargs)

        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context
