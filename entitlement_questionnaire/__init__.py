from otree.api import *

c = Currency

doc = """
Please respond to the following items using the number that best reflects your own beliefs [ENTITLEMENT QUESTIONNAIRE].
"""


class Constants(BaseConstants):
    name_in_url = 'entitlement_questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)


class Player(BasePlayer):
    q1 = make_q('I honestly feel I am more deserving than others')
    q2 = make_q('Great things should come for me.')
    q3 = make_q('If I were on the Titanic, I would deserve to be on the first lifeboat!')
    q4 = make_q('I demand the best because I’m worth it')
    q5 = make_q('I do not necessarily deserve special treatment')
    q6 = make_q('I deserve more things in my life')
    q7 = make_q('People like me deserve an extra break now and then')
    q8 = make_q('Things should go my way')
    q9 = make_q('I feel entitled to more of everything')
    q10 = make_q('This questions is being used to fill up space for combine scores calculation')

    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    conscientiousness = models.FloatField()
    neuroticism = models.FloatField()
    openness = models.FloatField()


def combine_score(positive, negative):
    return 3 + (positive - negative) / 2


# PAGES
class EntitlementQuestions(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.extraversion = combine_score(player.q6, player.q1)
        player.agreeableness = combine_score(player.q2, player.q7)
        player.conscientiousness = combine_score(player.q8, player.q3)
        player.neuroticism = combine_score(player.q9, player.q4)
        player.openness = combine_score(player.q10, player.q5)


class Results(Page):
    pass


page_sequence = [EntitlementQuestions, Results]
