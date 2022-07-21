import dominate
from dominate.tags import *
import sectionCreate

# print(sectionCreate.topics_unit_10)

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

    for i in range(0, len(sectionCreate.topicsList)):
        # here i = unitNumber
        hr()
        h3(str(i) + ' — ' + sectionCreate.topicsUnitNames[i])
        with div(cls='section-unit'):
            with div(cls='sections'):
                with ul():
                    for j in range(0, len(sectionCreate.topicsList[i])):
                        # here j = sectionNumber, so i.j+1 = sectionLabel
                        with li():
                            a(f'{i}.{j + 1} — {sectionCreate.topicsList[i][j]}',
                              href=f'{i}.{j + 1}-{sectionCreate.hyphenateText(sectionCreate.topicsList[i][j])}')
                            span('ⓘ', cls='section-info')
            with div(cls='resources'):
                with ul():
                    li()
            img(cls=f'header-image', src='../images/Calculus/home/[i].jpg')

with open('sectionMaterials/content-sections.html', 'w', encoding='utf-8') as file:
    file.write(doc.render())