import sys

if sys.version_info < (3, 7):
    raise ImportError('Your Python version {0} is not supported by dice_roll, please install '
                      'Python 3.7+'.format('.'.join(map(str, sys.version_info[:3]))))

from PowerfulDiceRoller.models import Dice, Result, DiceError, NotFoundMethod, ParseError
from PowerfulDiceRoller.parser import get_result, open_lark
from PowerfulDiceRoller.resources import GRAMMAR_CALCULATOR, GRAMMAR_DICE

__all__ = (
    "Dice",
    "Result",
    "DiceError",
    "NotFoundMethod",
    "ParseError",
    "get_result",
    "open_lark",
    "GRAMMAR_CALCULATOR",
    "GRAMMAR_DICE"
)

__version__ = '1.2'