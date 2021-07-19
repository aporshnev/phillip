from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    offer_1 = models.IntegerField(label="Scale 1", widget=widgets.RadioSelect, choices=[1, 2, 3])
    pass


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['offer_1']

    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
