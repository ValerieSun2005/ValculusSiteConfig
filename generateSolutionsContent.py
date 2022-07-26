from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re


def hyphenateText(text):
    newText = text.replace(' ', '-')
    return newText


def generate_solution_content(sectionLabel):
    sectionLabelHyphenated = hyphenateText(sectionLabel)
    with open(f'sectionMaterials/{sectionLabel}/exerciseList-{sectionLabelHyphenated}.html') as body:
        soup = BeautifulSoup(body, 'html.parser')
    appendText = ''
    for k in range(0, len(soup.find_all('span'))):
        exerciseHtml = f'''{soup.find_all('span')[k]}'''
        solutionHtml = f'''{soup.find_all('div')[k]}'''
        appendText += f'<div id="problem-{1 + k}"> \n' \
                      f'  <div class="box-solution__head"> QUESTION {1 + k} </div> \n' \
                      f'  <div class="box-solution">\n' \
                      f'   <div class="box-solution__body"> \n' \
                      f'        <div class="box-solution__problem"> \n ' \
                      f'           {exerciseHtml} \n' \
                      f'        </div> \n' \
                      f'        <hr> \n' \
                      f'        <div id="solution-{1 + k}"> \n' \
                      f'            <span class="solution-text">SOLUTION</span> \n' \
                      f'            {solutionHtml} \n' \
                      f'        </div> \n' \
                      '       </div>  \n' \
                      '   </div> \n' \
                      '</div> \n'
        with open(f'sectionMaterials/{sectionLabel}/solutionContent-{sectionLabelHyphenated}.html', 'w',
                  encoding='utf-8') as file:
            file.write(appendText)

generate_solution_content('Curve Sketching')
