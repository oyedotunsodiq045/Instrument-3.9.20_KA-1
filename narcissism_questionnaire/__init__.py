from otree.api import *

c = Currency

author = 'Sodiq Oyedotun'

doc = """
Please answer the following questions about yourself. There are no right or wrong answers.
"""


class Constants(BaseConstants):
    name_in_url = 'narcissism_questionnaire'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelect)


class Player(BasePlayer):
    q1 = make_q('People see me as a natural leader.')
    q2 = make_q('I hate being the center of attention. (R)')
    q3 = make_q('Many group activities tend to be dull without me.')
    q4 = make_q('I know that I am special because everyone keeps telling me so.')
    q5 = make_q('I like to get acquainted with important people.')
    q6 = make_q('I feel embarrassed if someone compliments me. (R)')
    q7 = make_q('I have been compared to famous people.')
    q8 = make_q('I am an average person. (R)')
    q9 = make_q('I insist on getting the respect I deserve.')
    q10 = make_q('This question is being used to fill up space for combine scores calculation')

    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    conscientiousness = models.FloatField()
    neuroticism = models.FloatField()
    openness = models.FloatField()


def combine_score(positive, negative):
    return 3 + (positive - negative) / 2


# PAGES
class NarcissismQuestionnaire(Page):
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


page_sequence = [NarcissismQuestionnaire, Results]
