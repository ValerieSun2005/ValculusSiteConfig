from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re


def hyphenateText(text):
    newText = text.replace(' ', '-')
    return newText


exercisesHintText = '<p class="exercises-hint">Click on a problem number to see its solution.</p> \n'

def generate_exercise_content(sectionLabel, sectionNumber):
    sectionLabelHyphenated = hyphenateText(sectionLabel)
    with open(f'sectionMaterials/{sectionLabel}/exerciseList-{sectionLabelHyphenated}.html',
              encoding='utf-8') as body:
        soup = BeautifulSoup(body, 'html.parser')

    exerciseNumber = 0
    exerciseNumberList = [0]
    appendText = '<section>'
    appendText += exercisesHintText
    for v in range(0, len(soup.find_all('section'))):
        sectionHtml = f'''{soup.find_all('section')[v]}'''
        soupSection = BeautifulSoup(sectionHtml, 'html.parser')
        problemsCount = len(soupSection.find_all('div'))
        exerciseNumber += problemsCount
        exerciseNumberList.append(exerciseNumber)

        # check whether the section in the exercise-list html file is grid or display.
        if len(soupSection.find_all('p')) > 0:
            if soupSection.find_all('p')[0].string.lower() == 'grid':  # check for grid
                columns = int(soupSection.find('p', {'class': 'columns'}).string)  # determine number of columns
                # as given by p tag
                directions = soupSection.find('p', {'class': 'directions'}).string  # directions

                # range of exercises for the directions:
                # if the range is more than 2, use en dash (e.g., "Exercises 6–9")
                if exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 > 1:
                    directionTextHTML = '<p class="problems-note">' \
                                        'For each of exercises ' \
                                        f'{exerciseNumberList[v] + 1}–{exerciseNumberList[v + 1]}, ' \
                                        f'{directions}. \n'
                # if the range is 2, use 'and' (e.g., "Exercises 6 and 7")
                elif exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 == 1:
                    directionTextHTML = '<p class="problems-note">' \
                                        'For each of exercises ' \
                                        f'{exerciseNumberList[v] + 1} and {exerciseNumberList[v + 1]}, ' \
                                        f'{directions}. \n'
                # if the range is 1, use singular (e.g., "Exercise 6")
                elif exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 == 0:
                    directionTextHTML = '<p class="problems-note">' \
                                        'For exercise ' \
                                        f'{exerciseNumberList[v] + 1}, ' \
                                        f'{directions}. \n'
                # if the range is 0, skip
                else:
                    directionTextHTML = ''

                j = problemsCount
                tableNumberStart = exerciseNumberList[v] + 1
                gridProblemsPrintHTML = '<table class="problems-grid"> \n' \
                                        '<tbody> \n'

                # numbers each grid exercise
                while j - columns > 0:
                    gridProblemsPrintHTML += '<tr> \n'
                    for k in range(0, columns):
                        gridProblemsPrintHTML += '<td> \n' \
                                                 f'<a href=' \
                                                 f'"{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.' \
                                                 f'html#problem-{k + tableNumberStart - j + problemsCount}" ' \
                                                 f'rel="noopener" target="_blank">' \
                                                 f'\({k + tableNumberStart - j + problemsCount}.\)</a> ' \
                                                 f'{soupSection.find_all("div")[k - j].string} \n' \
                                                 '</td> \n'
                    j -= columns
                    gridProblemsPrintHTML += '</tr> \n'

                if j > 0:  # last row
                    gridProblemsPrintHTML += '<tr> \n'
                    while j > 0:
                        gridProblemsPrintHTML += '<td> \n' \
                                                 f'<a href="{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.' \
                                                 f'html#problem-{problemsCount - j + tableNumberStart}" ' \
                                                 f'rel="noopener" target="_blank">' \
                                                 f'\({problemsCount - j + tableNumberStart}.\)</a> ' \
                                                 f'{soupSection.find_all("div")[problemsCount - j].string} \n' \
                                                 '</td> \n'
                        j -= 1
                    gridProblemsPrintHTML += '</tr> \n'
                gridProblemsPrintHTML += '</tbody> \n' \
                                         '</table> \n'
                appendText += directionTextHTML + gridProblemsPrintHTML
            else:
                pass
        else:
            displayProblemsPrintHTML = ''
            for k in range(0, len(soupSection.find_all('div'))):
                divHtml = f'''{soupSection.find_all('div')[k]}'''
                displayProblemsPrintHTML += f'<!--q{exerciseNumberList[v] + 1 + k}--> \n' \
                                            '<div class="problem-display"> \n' \
                                            f'   <a href="{sectionNumber}-{sectionLabelHyphenated}-' \
                                            f'exercises-solutions.html#problem-{exerciseNumberList[v] + 1 + k}" ' \
                                            f'target="_blank" rel="noopener">' \
                                            f'\({exerciseNumberList[v] + 1 + k}.\)</a> \n' \
                                            '    <div class="problem-display-body">\n' \
                                            f'       {divHtml} \n' \
                                            '   </div>  \n' \
                                            '</div> \n'

            appendText += displayProblemsPrintHTML
        appendText += '</section>'
    return appendText
    # with open(f'sectionMaterials/{sectionLabel}/exerciseContent-{sectionLabelHyphenated}.html', 'w',
    #           encoding='utf-8') as file:
    #     file.write(appendText)