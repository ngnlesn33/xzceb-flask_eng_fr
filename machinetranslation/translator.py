"""
Translator Module

This module provides functions for text translation.
"""
from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):
    """

    :param englishText:
    :type englishText:
    :return:
    :rtype:
    """
    frenchText = MyMemoryTranslator(source="english",
                                    target="french").translate(englishText)
    return frenchText


def frenchToEnglish(frenchText):
    """

    :param frenchText:
    :type frenchText:
    :return:
    :rtype:
    """
    englishText = MyMemoryTranslator(source="french",
                                     target="english").translate(frenchText)
    return englishText
