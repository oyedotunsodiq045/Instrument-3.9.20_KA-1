from otree.api import *

c = Currency

author = 'Sodiq Oyedotun'

doc = """
Your task is to determine the level of effort you want to exert at your job at ABC Company, doing so for 10 rounds. 
"""


class Constants(BaseConstants):
    players_per_group = 3
    num_rounds = 1
    name_in_url = 'abcapp'
    jackpot = Currency(100)
    lecturer_one = 'Dr. Jared Koreff'
    lecturer_one_university = 'Trinity University'
    lecturer_two = 'Dr. Stephanie Miller'
    lecturer_two_university = 'Quinnipiac University'
    lecturer_three = 'Dr. Kazeem Akinyele'
    lecturer_three_university = 'University of Wisconsin Oshkosh'
    information_sheet = 'abcapp/information_sheet.html'
    background = 'abcapp/background.html'
    contract = 'abcapp/contract.html'
    effort_levels = 'abcapp/effort_levels.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS


# PAGES
class ConsentForm(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    

class BackgroundInformation(Page):
    pass


class IncentiveContract(Page):
    pass


class EffortLevels(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


# page_sequence = [
#     ConsentForm,
#     BackgroundInformation,
#     IncentiveContract,
#     EffortLevels,
#     Results,
# ]

page_sequence = [
    ConsentForm,
    BackgroundInformation,
    IncentiveContract,
    EffortLevels,
]