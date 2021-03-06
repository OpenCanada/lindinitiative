from __future__ import absolute_import, unicode_literals

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


@python_2_unicode_compatible
class Organization(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=255)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def __str__(self):
        return self.name


register_snippet(Organization)


Organization.panels = [
    FieldPanel('name'),
    FieldPanel('website'),
    ImageChooserPanel('logo'),
]


class EventListPage(Page):
    subpage_types = ['EventPage']

    events_per_page = models.IntegerField(default=20)

    @property
    def subpages(self):
        # Get list of live event pages that are descendants of this page
        subpages = EventPage.objects.live().descendant_of(self).order_by('-date')

        return subpages

    def get_context(self, request):
        events = self.subpages

        page = request.GET.get('page')
        paginator = Paginator(events, self.events_per_page)
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        context = super(EventListPage, self).get_context(request)
        context['events'] = events
        return context

    content_panels = Page.content_panels + [
        FieldPanel('events_per_page')
    ]


@python_2_unicode_compatible
class EventPage(Page):
    date = models.DateTimeField("Event Date")
    location = models.CharField(max_length=255)
    event_link = models.URLField(max_length=255)
    body = RichTextField()
    organization = models.ForeignKey(
        'Organization',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def __str__(self):
        return "{}".format(
            self.title
        )

    content_panels = [
        FieldPanel("title"),
        FieldPanel("date"),
        FieldPanel("location"),
        FieldPanel("event_link"),
        FieldPanel("body"),
        SnippetChooserPanel('organization', Organization),
    ]
