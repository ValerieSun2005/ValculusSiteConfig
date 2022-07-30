import openpyxl
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re
import os
from openpyxl import Workbook
from openpyxl import load_workbook
import pageCreate
import pandas as pd


spreadsheet = openpyxl.load_workbook('sections.xlsx')
doc = dominate.document(title='Sections')

def hyphenateText(text):
    newText = text.replace(' ', '-')
    return newText

def generateContentPages():
    for i in range(0, len(spreadsheet.sheetnames)):
        sectionSheet = spreadsheet[f'{spreadsheet.sheetnames[i]}']
        for j in range(1, sectionSheet.max_row + 1):
            sectionLabelHyphenated = hyphenateText(
                sectionSheet.cell(row=j, column=1).value)  # convert spaces in file name to hyphens
            try:
                os.mkdir(f"sectionMaterials/{sectionSheet.cell(row=j, column=1).value}")
                with open(
                        f"sectionMaterials/{sectionSheet.cell(row=j, column=1).value}/content-{sectionLabelHyphenated}.html",
                        'x') as htmlContent:
                    htmlContent.write('')
                with open(
                        f"sectionMaterials/{sectionSheet.cell(row=j, column=1).value}/exerciseList-{sectionLabelHyphenated}.html",
                        'x') as htmlExerciseList:
                    htmlExerciseList.write('')
            except FileExistsError:
                pass

def generateLabeledSections():
    path = 'pythonPages/calculus'
    for k in os.listdir(path):
        os.remove(os.path.join(path, k))
    for i in range(0, len(spreadsheet.sheetnames)):
        sectionSheet = spreadsheet[f'{spreadsheet.sheetnames[i]}']
        for j in range(1, sectionSheet.max_row + 1):
            pageCreate.create_all_pages(f'{i}.{j}', sectionSheet.cell(row=j, column=1).value)

def createSectionPage():
    with doc.head:
        link(rel='stylesheet', href='css/section.css')
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
                                  href=f'{i}.{j}-{hyphenateText(sectionSheet.cell(row = j, column = 1).value)}')
                                span('ⓘ', cls='section-info')
                with div(cls='resources'):
                    with ul():
                        li()
                img(cls=f'header-image', src='../images/Calculus/home/[i].jpg')

    with open('sectionMaterials/content-sections.html', 'w', encoding='utf-8') as file:
        file.write(doc.render())

generateLabeledSections()