import re

def generateAnswerKey(filePath):
    indexToAnswerLetter = {
        '0': "A",
        '1': "B",
        '2': "C",
        '3': "D",
        '4': "E"
    }

    ACount = 0
    BCount = 0
    CCount = 0
    DCount = 0
    ECount = 0

    answerKeyContent = ''

    with open(f'{filePath}',
              encoding='utf-8') as file:
        i = 0
        j = 0
        problemLines = []
        for line in file:
            if '\\choices' in line:
                problemLines.append(line)
            elif line[0] == '{':
                problemLines.append(line)
            elif '\\end{question}' in line:
                i += 1
                problemLines.append(line)
                if len(problemLines) != 7:
                    print(f"Warning. Question {i} only has {len(problemLines)} detected answer choices.",
                          problemLines)
                else:
                    del problemLines[0]
                    del problemLines[-1]

                    for j in range(0, len(problemLines)):
                        if '\\ans' in problemLines[j]:
                            answer = indexToAnswerLetter[str(j)]
                            try:
                                answerKeyContent += f'{{\\bf{i}}}. & {answer} \\\\ \n'
                                if j == 0:
                                    ACount += 1
                                elif j == 1:
                                    BCount += 1
                                elif j == 2:
                                    CCount += 1
                                elif j == 3:
                                    DCount += 1
                                elif j == 4:
                                    ECount += 1

                            except KeyError:
                                print(f"Question {i}. Error;", f"Index—{j};", problemLines)
                problemLines = []
            else:
                pass

    print(f'{filePath} Answer Distribution. A—{ACount};', f'B—{BCount};',
          f'C—{CCount};', f'D—{DCount};', f'E—{ECount}')
    return(answerKeyContent)


# generateAnswerKey('content/Limits-and-Continuity-content.tex')
# with open('content/ttt.txt', 'w', encoding='utf-8') as f:
#     f.write(str(generateAnswerKey('content/Limits-and-Continuity-content.tex')))
#     f.close()