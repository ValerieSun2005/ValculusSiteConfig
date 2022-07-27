from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re

# sectionNumber = input("Input Section Number: ")
# sectionLabel = input("Input Section Label: ")

# sectionNumber = "3.5"
# sectionLabel = "Ur Mom Walrus XXVideos"

modeDisplayList = ['Section', 'Exercises', 'Exercise Solutions']


# mode = input(f"Select Page Mode ({'section'}, {'exercise'}, {'solution'}): ")

def create_page(mode, sectionNumber, sectionLabel, unitNumber):
    sectionLabelHyphenated = sectionLabel.replace(' ', '-')

    # title of html page
    if mode.lower() == 'section':
        doc = dominate.document(title=f'{sectionNumber}: {sectionLabel}')
    if mode.lower() == 'exercise':
        doc = dominate.document(title=f'{sectionNumber} Exercises: {sectionLabel}')
    if mode.lower() == 'solution':
        doc = dominate.document(title=f'{sectionNumber} Exercise Solutions: {sectionLabel}')

    # head of html page
    with doc.head:
        meta(name='viewport', content='width=device-width, initial-scale=1.0')
        meta(http_equiv='X-UA-Compatible', content='ie-edge')
        meta(name='author', content='Valerie')
        # meta(charset='UTF-8')
        link(rel='stylesheet',
             href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')
        # SCREEN LAYOUT
        link(rel='stylesheet', href='../css/layout.css')
        # PRINT LAYOUT
        link(rel='stylesheet', media='print', href='../css/layout-print.css')
        # link(rel='icon', href='http://example.com/favicon.png')
        # SECTION-SPECIFIC LAYOUT
        link(rel='stylesheet', href=f'../css/calculus/{sectionNumber}.css')
        script(src='https://code.jquery.com/jquery-3.3.1.js',
               integrity='sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=', crossorigin='anonymous')

    # body of html page
    with doc:
        script(type='text/javascript', src='../js/header-load.js')
        header(id='header', cls='tab')
        if mode.lower() == 'section':
            with doc.head:
                # SCREEN LAYOUT
                link(rel='stylesheet', href='../css/notes-style.css')
                # PRINT LAYOUT
                link(rel='stylesheet', media='print', href='../css/notes-style-print.css')
            h1(f'{sectionNumber} — {sectionLabel}')
        if mode.lower() == 'exercise':
            with doc.head:
                # SCREEN LAYOUT
                link(rel='stylesheet', href='../css/exercises-style.css')
            h1(f'{sectionNumber} Exercises — {sectionLabel}')
        if mode.lower() == 'solution':
            with doc.head:
                # SCREEN LAYOUT
                link(rel='stylesheet', href='../css/exercises-style.css')
            h1(f'{sectionNumber} Exercise Solutions — {sectionLabel}')

        # main()
        with main():
            # pdf panel
            with div(cls='pdf-panel'):
                with div(cls='pdf-panel-left').add(ul()):
                    if mode.lower() == 'section':
                        with li():
                            with button():
                                with a(f'{modeDisplayList[0]}', cls='link-deactivate', rel='noopener'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[1]}', href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises.html'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[2]}', href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html'):
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
                                with a(f'{modeDisplayList[2]}', href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html'):
                                    i(cls='fa fa-external-link')
                    if mode.lower() == 'solution':
                        with li():
                            with button():
                                with a(f'{modeDisplayList[0]}', href=f'{sectionNumber}-{sectionLabelHyphenated}.html'):
                                    i(cls='fa fa-external-link')
                        with li():
                            with button():
                                with a(f'{modeDisplayList[1]}', href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises.html'):
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

            hr(id='mainBodyBegin')
            comment('BEGIN BODY')  # APPEND FILE CONTENTS HERE




        script(type='text/javascript', src='../js/footer-load.js')
        div(id='footer')
        script(src='../js/mathjax-config.js')
        script(src='https://polyfill.io/v3/polyfill.min.js?features=es6')
        script(_async=True, id='MathJax-script', src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js')
        script(id='AMSmath', _async=True, src='TeX/AMSmath.js')
        script(src='http://code.jquery.com/jquery-latest.min.js')
        script(src='../js/toggle-solutions.js')

    # for main section: python renders html page, then another html page, content[...].html,  is inserted
    if mode.lower() == 'section':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", 'w',
                  encoding='utf-8') as file:
            file.write(doc.render())

        with open(f'sectionMaterials/{sectionLabel}/content-{sectionLabelHyphenated}.html',
                  encoding='utf-8') as sectionContent:
            soup = BeautifulSoup(sectionContent, 'html.parser')
            appendContent = f'''{soup}'''

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", 'r',
                  encoding='utf-8') as f:
            doc = BeautifulSoup(f, "html.parser")
            appendSpot = doc.select_one("#mainBodyBegin")

        appendSpot.append(BeautifulSoup(appendContent, 'html.parser'))

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", 'w',
                  encoding='utf-8') as output:
            output.write(str(doc))


    if mode.lower() == 'exercise':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises.html", 'w',
                  encoding='utf-8') as file:
            file.write(doc.render())

        with open(f'sectionMaterials/{sectionLabel}/exerciseContent-{sectionLabelHyphenated}.html',
                  encoding='utf-8') as exerciseContent:
            soup = BeautifulSoup(exerciseContent, "html.parser")
            appendContent = f'''{soup}'''

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises.html", "r",
                  encoding='utf-8') as f:
            doc = BeautifulSoup(f, "html.parser")
            appendSpot = doc.select_one("#mainBodyBegin")
        appendSpot.append(BeautifulSoup(appendContent, 'html.parser'))

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises.html", "w",
                  encoding='utf-8') as output:
            output.write(str(doc))

    if mode.lower() == 'solution':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html", 'w',
                  encoding='utf-8') as file:
            file.write(doc.render())

        with open(f'sectionMaterials/{sectionLabel}/solutionContent-{sectionLabelHyphenated}.html',
                  encoding='utf-8') as exerciseContent:
            soup = BeautifulSoup(exerciseContent, "html.parser")
            appendContent = f'''{soup}'''

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html", "r",
                  encoding='utf-8') as f:
            doc = BeautifulSoup(f, "html.parser")
            appendSpot = doc.select_one("#mainBodyBegin")
        appendSpot.append(BeautifulSoup(appendContent, 'html.parser'))

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html", "w",
                  encoding='utf-8') as output:
            output.write(str(doc))


def create_all_pages(sectionNumber, sectionLabel, unitNumber):
    create_page('section', f'{sectionNumber}', f'{sectionLabel}', unitNumber)  # MAKE MAIN SECTION PAGE
    create_page('exercise', f'{sectionNumber}', f'{sectionLabel}', unitNumber)  # MAKE EXERCISE PAGE
    create_page('solution', f'{sectionNumber}', f'{sectionLabel}', unitNumber)  # MAKE SOLUTION PAGE


create_page('section', '3.5', 'Curve Sketching', '3')
create_page('exercise', '3.5', 'Curve Sketching', '3')
create_page('solution', '3.5', 'Curve Sketching', '3')
# create_all_pages('3.5', 'Curve Sketching', '3')

# for i in ['home', 'about', 'contact']:
# li(a(i.title(), href='/%s.html' % i))

