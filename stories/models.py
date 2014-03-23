from ckeditor.fields import RichTextField
from django.db import models


class Name(models.Model):

    preferred_name = models.CharField(max_length=128)
    full_name = models.CharField(max_length=128, blank=True)
    github = models.CharField(max_length=128, blank=True)
    twitter = models.CharField(max_length=128, blank=True)
    website = models.URLField(blank=True)
    other = models.URLField(blank=True)


class KnownFor(models.Model):

    name = models.ForeignKey('stories.Name')
    role = models.CharField(max_length=50)
    project = models.CharField(max_length=50)


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

    CHOICES_VCS = [('git', 'git'),
                   ('hg', 'Mercurial (hg)'),
                   ('SVN', 'Subversion (svn)'),
                   ('CVS', 'CVS'),
                   ('email', 'diff/patch email'),
                   ('other', "something else (describe in 'experience' box below)"),
    ]

    name = models.ForeignKey('stories.Name')
    project = models.CharField(max_length=128)
    project_description = models.CharField(max_length=256, blank=True)
    vcs = models.CharField(max_length=64, choices=CHOICES_VCS)
    vcs_other = models.CharField(max_length=256, blank=True)
    month = models.PositiveSmallIntegerField(blank=True)
    year = models.PositiveSmallIntegerField()
    experience = RichTextField(blank=True)
    skill_professional = models.SmallIntegerField(blank=True)
    skill_language = models.SmallIntegerField(blank=True)
    skill_vcs = models.SmallIntegerField(blank=True)

    added_at = models.DateTimeField(auto_now_add=True)