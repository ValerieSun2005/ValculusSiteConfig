from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re
import os
import generateExerciseContent  # creates exerciseContent.html page from exerciseList.html
import generateSolutionsContent  # creates solutionContent.html page from exerciseList.html


# sectionNumber = input("Input Section Number: ")
# sectionLabel = input("Input Section Label: ")

# sectionNumber = "3.5"
# sectionLabel = "Ur Mom Walrus XXVideos"

modeDisplayList = ['Section', 'Exercises', 'Exercise Solutions']


# mode = input(f"Select Page Mode ({'section'}, {'exercise'}, {'solution'}): ")

def create_page(mode, sectionNumber, sectionLabel, filePath):
    sectionLabelHyphenated = sectionLabel.replace(' ', '-')

    # title of html page
    if mode.lower() == 'section':
        doc = dominate.document(title=f'{sectionNumber}: {sectionLabel}')
    elif mode.lower() == 'exercise':
        doc = dominate.document(title=f'{sectionNumber} Exercises: {sectionLabel}')
    elif mode.lower() == 'solution':
        doc = dominate.document(title=f'{sectionNumber} Exercise Solutions: {sectionLabel}')
    else:
        doc = dominate.document(title=f'{sectionLabel}')

    # head of html page
    with doc.head:
        meta(name='viewport', content='width=device-width, initial-scale=1.0')
        meta(http_equiv='X-UA-Compatible', content='ie-edge')
        meta(name='author', content='Valerie')
        meta(charset='UTF-8')
        link(rel='stylesheet',
             href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')
        # SCREEN LAYOUT
        link(rel='stylesheet', href='../css/layout.css')
        # PRINT LAYOUT
        link(rel='stylesheet', media='print', href='../css/layout-print.css')
        # link(rel='icon', href='http://example.com/favicon.png')
        # SECTION-SPECIFIC LAYOUT
        script(src='https://code.jquery.com/jquery-3.3.1.js',
               integrity='sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=', crossorigin='anonymous')

    # body of html page
    with doc:
        script(type='text/javascript', src='../js/header-load.js')
        header(id='header', cls='tab')

        # create headers of created page
        if mode.lower() == 'section':
            with doc.head:
                # SCREEN LAYOUT
                link(rel='stylesheet', href='../css/notes-style.css')
                # PRINT LAYOUT
                link(rel='stylesheet', media='print', href='../css/notes-style-print.css')
            h1(f'{sectionNumber} — {sectionLabel}')
        elif mode.lower() == 'exercise':
            with doc.head:
                # SCREEN LAYOUT
                link(rel='stylesheet', href='../css/exercises-style.css')
            h1(f'{sectionNumber} Exercises — {sectionLabel}')
        elif mode.lower() == 'solution':
            with doc.head:
                # SCREEN LAYOUT
                link(rel='stylesheet', href='../css/exercises-style.css')
            h1(f'{sectionNumber} Exercise Solutions — {sectionLabel}')
        else:
            h1(f'{sectionLabel}')

        # main()
        with main():
            # pdf panel
            with div(cls='pdf-panel'):
                with div(cls='pdf-panel-left').add(ul()):

                    # create button display panel directly below header
                    if mode.lower() == 'section':
                        with li():
                            with button():
                                with a(f'{modeDisplayList[0]}', cls='link-deactivate', rel='noopener'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[1]}',
                                       href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises.html'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[2]}',
                                       href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html'):
                                    i(cls='fa fa-external-link')
                    if mode.lower() == 'exercise':
                        with li():
                            with button():
                                with a(f'{modeDisplayList[0]}', href=f'{sectionNumber}-{sectionLabelHyphenated}.html'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[1]}', cls='link-deactivate', rel='noopener'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[2]}',
                                       href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html'):
                                    i(cls='fa fa-external-link')
                    if mode.lower() == 'solution':
                        with li():
                            with button():
                                with a(f'{modeDisplayList[0]}',
                                       href=f'{sectionNumber}-{sectionLabelHyphenated}.html'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[1]}',
                                       href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises.html'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[2]}', cls='link-deactivate', rel='noopener'):
                                    i(cls='fa fa-external-link')
                with div(cls='pdf-panel-right').add(ul()):
                    with li():
                        with button():
                            with a('Download', rel='noopener', target='_blank'):
                                i(cls='fa fa-file-pdf-o')

            comment('BEGIN BODY')
            hr(id='mainBodyBegin')
            comment('APPEND CONTENT HERE')  # APPEND FILE CONTENTS HERE

        script(type='text/javascript', src='../js/footer-load.js')
        div(id='footer')
        script(src='../js/mathjax-config.js')
        script(src='https://polyfill.io/v3/polyfill.min.js?features=es6')
        script(_async=True, id='MathJax-script', src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js')
        script(id='AMSmath', _async=True, src='TeX/AMSmath.js')
        script(src='http://code.jquery.com/jquery-latest.min.js')
        script(src='../js/toggle-solutions.js')

    # append content pages to main page body. process:

    # (1) the doc of the html page is rendered by Dominate library and labeled as an official section;
    # (2) the content page is parsed and converted into a string, appendContent;
    # (3) appendContent is appended to the labeled, official section

    if mode.lower() == 'section':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", 'w',
                  encoding='utf-8') as file:
            file.write(doc.render())

        with open(f'sectionMaterials/{sectionLabel}/content-{sectionLabelHyphenated}.html',
                  encoding='utf-8') as file:
            appendContent = file.read()

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", 'r',
                  encoding='utf-8') as file:
            data = file.read()
            data = data.replace('<!--APPEND CONTENT HERE-->', appendContent)

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", "w",
                  encoding='utf-8') as file:
            file.write(data)

    # exercise
    elif mode.lower() == 'exercise':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises.html", 'w',
                  encoding='utf-8') as file:
            file.write(doc.render())

        appendContent = generateExerciseContent.generate_exercise_content(sectionLabel, sectionNumber)

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises.html", "r",
                  encoding='utf-8') as file:
            data = file.read()
            data = data.replace('<!--APPEND CONTENT HERE-->', appendContent)

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises.html", "w",
                  encoding='utf-8') as output:
            output.write(str(doc))

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises.html", "w",
                  encoding='utf-8') as file:
            file.write(data)

    # solution
    elif mode.lower() == 'solution':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html", 'w',
                  encoding='utf-8') as file:
            file.write(doc.render())

        appendContent = generateSolutionsContent.generate_solutions_content(sectionLabel)

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html", "r",
                  encoding='utf-8') as file:
            data = file.read()
            data = data.replace('<!--APPEND CONTENT HERE-->', appendContent)

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html", "w",
                  encoding='utf-8') as output:
            output.write(str(doc))

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html", "w",
                  encoding='utf-8') as file:
            file.write(data)

    # all other pages
    else:
        with open(f"pythonPages/{filePath}", 'w',
                  encoding='utf-8') as file:
            file.write(doc.render())

        with open(f'sectionMaterials/content-sections.html',
                  encoding='utf-8') as file:
            appendContent = file.read()

        with open(f"pythonPages/{filePath}", 'r',
                  encoding='utf-8') as file:
            data = file.read()
            data = data.replace('<!--APPEND CONTENT HERE-->', appendContent)

        with open(f"pythonPages/{filePath}", "w",
                  encoding='utf-8') as file:
            file.write(data)

        # with open(f"pythonPages/{filePath}", "w", encoding="utf-8") as file:
        #     file.write(doc.render())
        #
        # with open(f"sectionMaterials/content-{sectionLabel}.html", encoding='utf-8') as file:
        #     appendContent = file.read()
        #
        # with open(f"pythonPages/{filePath}", "w", encoding="utf-8") as file:
        #     file.write(doc.render())






def create_all_pages(sectionNumber, sectionLabel):
    create_page('section', f'{sectionNumber}', f'{sectionLabel}', '')  # MAKE MAIN SECTION PAGE
    create_page('exercise', f'{sectionNumber}', f'{sectionLabel}', '')  # MAKE EXERCISE PAGE
    create_page('solution', f'{sectionNumber}', f'{sectionLabel}', '')  # MAKE SOLUTION PAGE


# create_all_pages('3.5', 'Curve Sketching')
create_page('', '', 'Sections', 'sections.html')
# create_page('section', '3.5', 'Curve Sketching', '3')
# create_page('exercise', '3.5', 'Curve Sketching', '3')
# create_page('solution', '3.5', 'Curve Sketching', '3')
# create_all_pages('3.5', 'Curve Sketching', '3')

# for i in ['home', 'about', 'contact']:
# li(a(i.title(), href='/%s.html' % i))

