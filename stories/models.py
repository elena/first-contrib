from ckeditor.fields import RichTextField
from django.db import models


class Name(models.Model):

    preferred_name = models.CharField(max_length=128, null=True)
    full_name = models.CharField(max_length=128, blank=True, null=True)
    github = models.CharField(max_length=128, blank=True, null=True)
    twitter = models.CharField(max_length=128, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    other = models.URLField(blank=True, null=True)


class KnownFor(models.Model):

    name = models.ForeignKey('stories.Name')
    role = models.CharField(max_length=256, blank=True, null=True)
    project = models.CharField(max_length=256, blank=True, null=True)


class Story(models.Model):

    CHOICES_ASSESS = [
        (0, '0 (complete beginner)'),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (0, '10 (master)'),
    ]

    CHOICES_VCS = [
        ('git', 'git'),
        ('hg', 'Mercurial (hg)'),
        ('SVN', 'Subversion (svn)'),
        ('CVS', 'CVS'),
        ('email', 'diff/patch email'),
    ]
    CHOICES_COMMS = [
        ('email', 'Direct Email'),
        ('list', 'Email List'),
        ('irc', 'IRC'),
        ('person', 'In Person'),
        ('phone', 'Phone'),
    ]

    name = models.ForeignKey('stories.Name', null=True, blank=True)
    project = models.CharField(max_length=256, blank=True, null=True)
    project_description = models.CharField(max_length=256, blank=True, null=True)
    vcs = models.CharField(max_length=1024, blank=True, null=True)
    vcs_other = models.CharField(max_length=512, blank=True, null=True)
    comms = models.CharField(max_length=2048, blank=True, null=True)
    comms_other = models.CharField(max_length=512, blank=True, null=True)
    month = models.PositiveSmallIntegerField(blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    experience = RichTextField(blank=True, null=True)
    skill_professional = models.SmallIntegerField(blank=True, null=True)
    skill_language = models.SmallIntegerField(blank=True, null=True)
    skill_vcs = models.SmallIntegerField(blank=True, null=True)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'stories'
