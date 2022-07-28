from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re


def hyphenateText(text):
    newText = text.replace(' ', '-')
    return newText


def generate_solutions_content(sectionLabel):
    sectionLabelHyphenated = hyphenateText(sectionLabel)
    with open(f'sectionMaterials/{sectionLabel}/exerciseList-{sectionLabelHyphenated}.html') as body:
        soup = BeautifulSoup(body, 'html.parser')
    appendText = ''
    exerciseNumber = 0
    exerciseNumberList = [0]
    for v in range(0, len(soup.find_all('section'))):
        sectionHtml = f'''{soup.find_all('section')[v]}'''
        soupSection = BeautifulSoup(sectionHtml, 'html.parser')
        problemsCount = len(soupSection.find_all('div'))
        exerciseNumber += problemsCount
        exerciseNumberList.append(exerciseNumber)

        for k in range(0, len(soupSection.find_all('div'))):
            exerciseHtml = f'''{soup.find_all('div')[k + exerciseNumberList[v]]}'''
            solutionHtml = f'''{soup.find_all('span')[k + exerciseNumberList[v]]}'''
            if len(soupSection.find_all('p')) > 0:
                directions = soupSection.find('p', {'class': 'directions'}).string

                # re-expresses "exerciseHtml" from an inline expression to a display equation
                exerciseSplitDiv = re.split('<div>|</div>', exerciseHtml)[1]
                exerciseDisplayMode = exerciseSplitDiv.replace('\(', '\[').replace('\)', '\comma \]')

                # format of "For [this exercise], [directions]"
                appendText += f"<div id=\"problem-{1 + exerciseNumberList[v] + k}\"> \n" \
                              f"  <div class=\"box-solution__head\"> " \
                              f"    QUESTION {1 + exerciseNumberList[v] + k} </div> \n" \
                              f"  <div class=\"box-solution\">\n" \
                              f"   <div class=\"box-solution__body\"> \n" \
                              f"        <div class=\"box-solution__problem\"> \n " \
                              f"           For {exerciseDisplayMode} {directions}. \n" \
                              f"        </div> \n" \
                              f"        <hr> \n" \
                              f"        <div id=\"solution-{1 + exerciseNumberList[v] + k}\"> \n" \
                              f"            <span class=\"solution-text\">SOLUTION</span> \n" \
                              f"            {solutionHtml} \n" \
                              "        </div> \n" \
                              "       </div>  \n" \
                              "   </div> \n" \
                              "</div>"
            else:
                appendText += f"<div id=\"problem-{1 + exerciseNumberList[v] + k}\"> \n" \
                              f"  <div class=\"box-solution__head\"> " \
                              f"    QUESTION {1 + exerciseNumberList[v] + k} </div> \n" \
                              f"  <div class=\"box-solution\">\n" \
                              f"   <div class=\"box-solution__body\"> \n" \
                              f"        <div class=\"box-solution__problem\"> \n " \
                              f"           {exerciseHtml} \n" \
                              f"        </div> \n" \
                              f"        <hr> \n" \
                              f"        <div id=\"solution-{1 + exerciseNumberList[v] + k}\"> \n" \
                              f"            <span class=\"solution-text\">SOLUTION</span> \n" \
                              f"            {solutionHtml} \n" \
                              "        </div> \n" \
                              "       </div>  \n" \
                              "   </div> \n" \
                              "</div>"
    return appendText

