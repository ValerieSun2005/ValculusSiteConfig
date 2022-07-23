from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re

with open('ttt.html') as body:
    soup = BeautifulSoup(body, 'html.parser')

# print(soup.find_all('p')[0])

with open('output.html', 'a') as file:
    file.write(
        '<p class="exercises-hint">Click on a problem number to view its solution.</p> \n')

exerciseNumber = 0
exerciseNumberList = [0]

for v in range(0, len(soup.find_all('section'))):
    sectionHtml = f'''{soup.find_all('section')[v]}'''
    soupSection = BeautifulSoup(sectionHtml, 'html.parser')
    problemsCount = len(soupSection.find_all('span'))
    exerciseNumber += problemsCount
    exerciseNumberList.append(exerciseNumber)
    try:
        if soupSection.find_all('p')[0].string.lower() == 'grid':
            columns = int(soupSection.find('p', {'class': 'columns'}).string)
            directions = soupSection.find('p', {'class': 'directions'}).string
            if exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 > 1:
                directionTextHTML = '<p class="problems-note">' \
                                    'For each of exercises ' \
                                    f'{exerciseNumberList[v] + 1}–{exerciseNumberList[v + 1]},' \
                                    f'{directions}.'
            if exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 == 1:
                directionTextHTML = '<p class="problems-note">' \
                                    'For each of exercises ' \
                                    f'{exerciseNumberList[v] + 1} and {exerciseNumberList[v + 1]},' \
                                    f'{directions}.'
            elif exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 == 0:
                directionTextHTML = '<p class="problems-note">' \
                                    'For exercise ' \
                                    f'{exerciseNumberList[v] + 1},' \
                                    f'{directions}.'
            else:
                pass

            j = problemsCount
            tableNumberStart = exerciseNumberList[v] + 1
            gridProblemsPrintHTML = '<table class="problems-grid"> \n ' \
                                    '   <tbody> \n'
            while j - columns > 0:
                gridProblemsPrintHTML += '  <tr> \n'
                for k in range(0, columns):
                    gridProblemsPrintHTML += '<td> \n' \
                                             f'  <a href="">\({problemsCount - j + tableNumberStart}.\)</a>\n' \
                                             f'{soupSection.find_all("span")[problemsCount - j].string}'

            # with table(cls='problems-grid'):
            #     with tbody():
            #         while j - columns > 0:
            #             with tr():
            #                 for k in range(0, columns):
            #                     with td():
            #                         a(f'\({k + tableNumberStart - j + problemsCount}.\)',
            #                           rel='noopener',
            #                           target='_blank',
            #                           href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html#problem-{k + tableNumberStart - j + problemsCount}'
            #                           )
            #                         span(soup2.find_all('span')[
            #                                  k - j].string)
            #             j -= columns
            #
            #         if j > 0:
            #             with tr():
            #                 while j > 0:
            #                     with td():
            #                         a(f'\({problemsCount - j + tableNumberStart}.\)',
            #                           rel='noopener',
            #                           target='_blank',
            #                           href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html#problem-{problemsCount - j + tableNumberStart}'
            #                           )
            #                         span(soup2.find_all('span')[problemsCount - j].string)
            #                     j -= 1
    except:
        pass


for i in range(len(soup.find_all('p'))):
    doc = f'''{soup.find_all('p')[i]}'''
    print(doc)

    appendedText = f'<!--q{i}--> \n' \
                   '<div class="problem-display"> \n' \
                   f'   <a href="{i}" target="_blank" rel="noopener">\({i}\)</a> \n' \
                   '    <div class="problem-display-body">\n' \
                   f'       {doc} \n' \
                   f'   </div>  \n' \
                   f'</div> \n'

    with open('output.html', 'a') as file:
        file.write(f'{appendedText}\n')