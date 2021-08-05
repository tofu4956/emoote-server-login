from django.test import TestCase
from graphene.types import datetime
from userdatas.models import Entry, Userdata
import graphene
from graphene_django import DjangoObjectType
from django.test import TestCase

# Create your tests here.

class EntryNode(DjangoObjectType):
    class Meta:
        model = Entry

class Query(graphene.ObjectType):
        entry = graphene.Field(EntryNode, id=graphene.Int())