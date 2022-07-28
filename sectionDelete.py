import os
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re
import pageCreate
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

spreadsheet = openpyxl.load_workbook('sections.xlsx')

def hyphenateText(text):
    newText = text.replace(' ', '-')
    return newText

# def deleteSection():
path = 'pythonPages/calculus'
for i in os.listdir(path):
    os.remove(os.path.join(path, f))