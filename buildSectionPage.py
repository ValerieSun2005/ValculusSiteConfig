import openpyxl
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re
from openpyxl import Workbook
from openpyxl import load_workbook
import sectionCreate
import pandas as pd

# print(sectionCreate.topics_unit_10)

spreadsheet = openpyxl.load_workbook('sections.xlsx')
doc = dominate.document(title='Sections')



with doc:
    img(cls='header-image', src='../images/Calculus/home/calculus.jpg', alt='')
    p('Welcome to Calculus.\
    The following sections are designed for all calculus students, \
    including students taking AP® Calculus and the college courses \
    Calculus I and Calculus II. \
    Each section provides an overview of the concept and contains exercises and solutions. \
    PDFs of the notes, exercises, and solutions are also presented in the sections.\
    Supplemental resources&#8288;—&#8288;such  \
    as cheat sheets, Quizlets, and practice tests&#8288;—&#8288; are included \
    in each chapter.\
    For copyright policy, please visit the <a href="">Terms of Use</a> page.\
    If you catch any mistakes, please contact me. \
    Happy studying!')

    for i in range(0, len(spreadsheet.sheetnames)):
        sectionSheet = spreadsheet[f'{spreadsheet.sheetnames[i]}']
        # here i = unitNumber
        hr()
        h3(str(i) + ' — ' + f'{spreadsheet.sheetnames[i]}')
        with div(cls='section-unit'):
            with div(cls='sections'):
                with ul():
                    for j in range(1, sectionSheet.max_row + 1):
                        # here j = sectionNumber; thus, i.j+1 = sectionLabel
                        with li():
                            a(f'{i}.{j} — {sectionSheet.cell(row = j, column = 1).value}',
                              href=f'{i}.{j}-{sectionCreate.hyphenateText(sectionSheet.cell(row = j, column = 1).value)}')
                            span('ⓘ', cls='section-info')
            with div(cls='resources'):
                with ul():
                    li()
            img(cls=f'header-image', src='../images/Calculus/home/[i].jpg')

with open('sectionMaterials/content-sections.html', 'w', encoding='utf-8') as file:
    file.write(doc.render())