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

    def get_context_data(self, **kwargs):
        context = super(StoryAddView, self).get_context_data(**kwargs)

        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context
