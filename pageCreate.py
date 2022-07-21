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


def italics_check(txt):
    txtSplitItalics = re.split('<i>|</i>', txt)
    for j in range(0, len(txtSplitItalics)):
        if j % 2 == 1:
            i(txtSplitItalics[j])
        else:
            if '<span>' in txtSplitItalics[j]:
                span(txtSplitItalics[j].split('<span>')[1])
            elif '</span>' in txtSplitItalics[j]:
                span(txtSplitItalics[j].split('</span>')[0])
            else:
                span(txtSplitItalics[j])


def print_exercises(sectionNumber, sectionLabel, unitNumber):
    sectionLabelHyphenated = sectionLabel.replace(' ', '-')
    p('Click on a problem number to view its solution.', cls='exercises-hint')
    with open(f'sectionMaterials/{sectionLabel}/exerciseList-{sectionLabelHyphenated}.html') as body:
        soup = BeautifulSoup(body, 'html.parser')
    sectionCount = len(soup.findAll('section'))
    exerciseNumber = 0
    exerciseNumberList = [0]
    for v in range(0, sectionCount):
        doc = f'''{soup.find_all('section')[v]}'''
        soup2 = BeautifulSoup(doc, 'html.parser')
        problemsCount = len(soup2.findAll('span'))
        exerciseNumber += problemsCount
        exerciseNumberList.append(exerciseNumber)
        try:
            if soup2.find_all('p')[0].string.lower() == 'grid':
                columns = int(soup2.find('p', {'class': 'columns'}).string)
                directions = soup2.find('p', {'class': 'directions'}).string
                if exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 > 1:
                    with tbody():
                        p(f'For each of exercises {exerciseNumberList[v] + 1}–{exerciseNumberList[v + 1]}, {directions}.',
                          cls='problems-note')
                elif exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 == 1:
                    with tbody():
                        p(f'For each of exercises {exerciseNumberList[v] + 1} and {exerciseNumberList[v + 1]}, {directions}.',
                          cls='problems-note')
                elif exerciseNumberList[v + 1] - exerciseNumberList[v] - 1 == 0:
                    with tbody():
                        p(f'For exercise {exerciseNumberList[v] + 1}, {directions}.',
                          cls='problems-note')
                j = problemsCount
                tableNumberStart = exerciseNumberList[v] + 1
                with table(cls='problems-grid'):
                    with tbody():
                        while j - columns > 0:
                            with tr():
                                for k in range(0, columns):
                                    with td():
                                        a(f'\({k + tableNumberStart - j + problemsCount}.\)',
                                          rel='noopener',
                                          target='_blank',
                                          href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html#problem-{k + tableNumberStart - j + problemsCount}'
                                          )
                                        span(soup2.find_all('span')[
                                                 k - j].string)
                            j -= columns

                        if j > 0:
                            with tr():
                                while j > 0:
                                    with td():
                                        a(f'\({problemsCount - j + tableNumberStart}.\)',
                                          rel='noopener',
                                          target='_blank',
                                          href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html#problem-{problemsCount - j + tableNumberStart}'
                                          )
                                        span(soup2.find_all('span')[problemsCount - j].string)
                                    j -= 1

        except:
            figureCount = 0
            figureLabels = []
            for k in range(0, len(soup2.find_all('span'))):
                displayBody = str(soup2.find_all('span')[k])
                soup2Italics = BeautifulSoup(displayBody, 'html.parser')
                with div(cls='problem-display'):
                    a(f'\({exerciseNumberList[v] + 1 + k}.\)',
                      rel='noopener',
                      target='_blank',
                      href=f'{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html#problem-{exerciseNumberList[v] + 1 + k}'
                      )  # number label of each problem

                    if len(soup2.find_all('span')[k]('figure')) > 0:
                        txtSplitFigure = re.split('<figure><img src="|"/></figure>', displayBody)
                        # the txtSplitFigure has three components:
                        # (0) the problem, which is the body text;
                        # (1) the alt tag, which is the figure label we use as a reference;
                        # (2) the url of the image, which is where the html is to find the image; and
                        # (3) the ending tag.

                        figureLabels.append(txtSplitFigure[1])  # add the alt tag, the figure label,
                        # to the list # figureLabels

                        figureCount += 1

                        if '{fig}' in txtSplitFigure[0]:
                            txtSplitFigure[0] = txtSplitFigure[0].replace(
                                '{fig}', f'Figure {figureCount}')

                        if len(soup2Italics.find_all('i')) > 0:
                            with div(cls='problem-display-body'):
                                txt2 = txtSplitFigure[0]
                                italics_check(txt2)

                        else:
                            if '<span>' in txtSplitFigure[0]:
                                div(txtSplitFigure[0].split('<span>')[1], cls='problem-display-body')
                        style(f".fig-{figureCount}::before{{content: 'FIGURE {figureCount}'}}")
                        with figure(cls=f'fig-{figureCount}'):
                            img(src=f'{txtSplitFigure[1]}', alt=f'fig-{figureCount}')
                        br()


                    else:
                        if len(soup2Italics.find_all('i')) > 0:
                            with div(cls='problem-display-body'):
                                italics_check(displayBody)
                        else:
                            if '<span>' in soup2.find_all('span')[k].string:
                                div(soup2.find_all('span')[k].string.split('<span>')[1], cls='problem-display-body')
                            elif '</span>' in soup2.find_all('span')[k].string:
                                div(soup2.find_all('span')[k].string.split('</span>')[0], cls='problem-display-body')
                            else:
                                div(soup2.find_all('span')[k].string, cls='problem-display-body')


def print_exercise_solutions(sectionNumber, sectionLabel, unitNumber):
    sectionLabelHyphenated = sectionLabel.replace(' ', '-')
    with open(f'sectionMaterials/{sectionLabel}/exerciseList-{sectionLabelHyphenated}.html') as body:
        soup = BeautifulSoup(body, 'html.parser')
    sectionCount = len(soup.findAll('section'))
    exerciseNumber = 0
    exerciseNumberList = [0]
    for v in range(0, sectionCount):
        test = soup.find_all('section')[v]
        doc = f'''{test}'''
        soup2 = BeautifulSoup(doc, 'html.parser')
        problemsCount = len(soup2.findAll('span'))
        exerciseNumber += problemsCount
        exerciseNumberList.append(exerciseNumber)
        figureCount = 0
        for k in range(0, len(soup2.find_all('span'))):
            with div(id=f'problem-{exerciseNumberList[v] + 1 + k}'):
                div(f'QUESTION {exerciseNumberList[v] + 1 + k}', cls='box-solution__head')
                with div(cls='box-solution'):
                    with div(cls='box-solution__body'):
                        displayBody = str(soup2.find_all('span')[k])
                        soup2Italics = BeautifulSoup(displayBody, 'html.parser')
                        with div(cls='problem-display'):
                            if len(soup2.find_all('span')[k]('figure')) > 0:
                                txtSplitFigure = re.split('<figure><img src="|"/></figure>', displayBody)
                                figureCount += 1
                                if '{fig}' in txtSplitFigure[0]:
                                    txtSplitFigure[0] = txtSplitFigure[0].replace(
                                        '{fig}', f'Figure {figureCount}')
                                if len(soup2Italics.find_all('i')) > 0:
                                    with div(cls='problem-display-body'):
                                        txt2 = txtSplitFigure[0]
                                        italics_check(txt2)
                                else:
                                    if '<span>' in txtSplitFigure[0]:
                                        div(txtSplitFigure[0].split('<span>')[1], cls='problem-display-body')
                                style(f".fig-{figureCount}::before{{content: 'FIGURE {figureCount}'}}")
                                with figure(cls=f'fig-{figureCount}'):
                                    img(src=f'{txtSplitFigure[1]}', alt='')
                                br()

                            else:
                                if len(soup2Italics.find_all('i')) > 0:
                                    with div(cls='problem-display-body'):
                                        italics_check(displayBody)
                                else:
                                    if '<span>' in soup2.find_all('span')[k].string:
                                        div(soup2.find_all('span')[k].string.split('<span>')[1],
                                            cls='problem-display-body')
                                    elif '</span>' in soup2.find_all('span')[k].string:
                                        div(soup2.find_all('span')[k].string.split('</span>')[0],
                                            cls='problem-display-body')
                                    else:
                                        try:
                                            if soup2.find_all('p')[0].string.lower() == 'grid':
                                                directions = soup2.find('p', {'class': 'directions'}).string
                                                div('For' + soup2.find_all('span')[k].string+', ' + directions + '.', style='width: 100%')
                                        except:
                                            div(soup2.find_all('span')[k].string, style='width: 100%')

                        hr()
                        with div(id=f'solution-{exerciseNumberList[v] + 1 + k}'):
                            span('SOLUTION', cls='solution-text')
                            span(soup2.find_all('div')[k].string)


def create_page(mode, sectionNumber, sectionLabel, unitNumber):
    sectionLabelHyphenated = sectionLabel.replace(' ', '-')
    if mode.lower() == 'section':
        doc = dominate.document(title=f'{sectionNumber}: {sectionLabel}')
    if mode.lower() == 'exercise':
        doc = dominate.document(title=f'{sectionNumber} Exercises: {sectionLabel}')
    if mode.lower() == 'solution':
        doc = dominate.document(title=f'{sectionNumber} Exercise Solutions: {sectionLabel}')

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
        with main():
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
            comment('BEGIN BODY')

            if mode.lower() == 'exercise':
                print_exercises(sectionNumber, sectionLabel, unitNumber)

            if mode.lower() == 'solution':
                print_exercise_solutions(sectionNumber, sectionLabel, unitNumber)

        script(type='text/javascript', src='../js/footer-load.js')
        div(id='footer')
        script(src='../js/mathjax-config.js')
        script(src='https://polyfill.io/v3/polyfill.min.js?features=es6')
        script(_async=True, id='MathJax-script', src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js')
        script(id='AMSmath', _async=True, src='TeX/AMSmath.js')
        script(src='http://code.jquery.com/jquery-latest.min.js')
        script(src='../js/toggle-solutions.js')

    # for main section: python renders html page, then another html page - content[...].html - is inserted
    if mode.lower() == 'section':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", 'w', encoding='utf-8') as file:
            file.write(doc.render())

        with open(f'sectionMaterials/{sectionLabel}/content-{sectionLabelHyphenated}.html', encoding='utf-8') as body:
            soup = BeautifulSoup(body, "html.parser")

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", "r", encoding='utf-8') as f:
            doc = BeautifulSoup(f, "html.parser")
            appendSpot = doc.select_one("#mainBodyBegin")
        content = str(soup.find_all("section")[0])
        appendSpot.append(BeautifulSoup(content, 'html.parser'))

        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}.html", "w", encoding='utf-8') as output:
            output.write(str(doc))


    if mode.lower() == 'exercise':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises.html", 'w', encoding='utf-8') as file:
            file.write(doc.render())

    if mode.lower() == 'solution':
        with open(f"pythonPages/calculus/{sectionNumber}-{sectionLabelHyphenated}-exercises-solutions.html", 'w', encoding='utf-8') as file:
            file.write(doc.render())


def create_all_pages(sectionNumber, sectionLabel, unitNumber):
    create_page('section', f'{sectionNumber}', f'{sectionLabel}', unitNumber)  # MAKE MAIN SECTION PAGE
    create_page('exercise', f'{sectionNumber}', f'{sectionLabel}', unitNumber)  # MAKE EXERCISE PAGE
    create_page('solution', f'{sectionNumber}', f'{sectionLabel}', unitNumber)  # MAKE SOLUTION PAGE


create_all_pages('3.5', 'Curve Sketching', '3')

# for i in ['home', 'about', 'contact']:
# li(a(i.title(), href='/%s.html' % i))

