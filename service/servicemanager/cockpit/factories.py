import datetime
import factory.fuzzy
import random
from .models import Engineer

class EngineerFactory(factory.Factory):
    class Meta:
        model = Engineer
    abbreviation = factory.fuzzy.FuzzyText(length=4)
    shift = factory.fuzzy.FuzzyText(length=6)
    vacation_hours = factory.fuzzy.FuzzyDecimal(low=0,high=200,precision=1)
    sap=factory.fuzzy.FuzzyText(length=6,chars=[0,1,2,3,5,6,7,8,9])

def make_engineers():
    EngineerFactory.create_batch(size=50)