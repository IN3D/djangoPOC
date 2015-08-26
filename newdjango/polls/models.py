from mongoengine import *


class Campaign(Document):
    name = StringField(max_length=200)
    started = DateTimeField(help_text='date started')


class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)


class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    campaign = ReferenceField(Campaign)
    choices = ListField(EmbeddedDocumentField(Choice))
