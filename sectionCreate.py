import os
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re
# import pageCreate
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook


def hyphenateText(text):
    newText = text.replace(' ', '-')
    return newText


spreadsheet = openpyxl.load_workbook('sections.xlsx')

# for i in range(0, len(unit3SectionInfo)):
#     print(unit3SectionInfo[topicsUnit3[i]])

for i in range(0, len(spreadsheet.sheetnames)):
    sectionSheet = spreadsheet[f'{spreadsheet.sheetnames[i]}']
    for j in range(1, sectionSheet.max_row + 1):
        sectionLabelHyphenated = hyphenateText(
            sectionSheet.cell(row=j, column=1).value)  # convert spaces in file name to hyphens
        try:
            os.mkdir(f"F:/Valculus/sectionMaterials/{sectionSheet.cell(row=j, column=1).value}")
            with open(
                    f"F:/Valculus/sectionMaterials/{sectionSheet.cell(row=j, column=1).value}/content-{sectionLabelHyphenated}.html",
                    'x') as htmlContent:
                htmlContent.write('')
            with open(
                    f"F:/Valculus/sectionMaterials/{sectionSheet.cell(row=j, column=1).value}/exerciseList-{sectionLabelHyphenated}.html",
                    'x') as htmlExerciseList:
                htmlExerciseList.write('')
        except:
            pass

        # try:
        #     pageCreate.create_all_pages(f'{i}.{j + 1}', f'{topics_list[i][j]}', f'{i}')
        # except:
        #     pass

unitOfRenamedSection = int(input('In What Unit Is the Section You Want to Rename? Unit: '))

try:
    sheetRenamedSection = spreadsheet[
        f'{spreadsheet.sheetnames[unitOfRenamedSection]}']  # finds sheet of unit to rename
    oldSectionName = input('Old Section Name: ')
    for i in range(1, sheetRenamedSection.max_row + 1):
        if sheetRenamedSection.cell(row=i, column=1).value == oldSectionName:  # searches all the rows in column A
            print('hi', i)
            break
        else:
            pass
    newSectionName = input('New Section Name (Rename as): ')
    sheetRenamedSection[f'A{i}'] = newSectionName
    spreadsheet.save('sections.xlsx')
except IndexError:
    print(f"Error: '{unitOfRenamedSection}' is not between 0 and {len(spreadsheet.sheetnames) - 1}")
except ValueError:
    print(f"Error: '{unitOfRenamedSection}' is not an integer between 0 and {len(spreadsheet.sheetnames) - 1}")

# sectionListPrint = "<ul>"
#
# for i in range(0, len(topics_list)):
#     for j in range(0, len(topics_list[i])):
#         sectionListPrint = sectionListPrint + \
#                            f'<li><a href="{i}.{j + 1}-{hyphenateText(topics_list[i][j])}.html">{i}.{j + 1} — {topics_list[i][j]}</a></li>'
#         print(j, i)

# print(sectionListPrint)

# fin = open("sectionMaterials/content-sections.html", "rt", encoding='utf-8')
# fout = open("pythonPages/sections.html", "wt", encoding='utf-8')
#
# for i in range(0, len(topics_list)):
#     sectionListPrint = "<ul>"
#     fin = open("pythonPages/sections.html", "rt", encoding='utf-8')
#     for j in range(0, len(topics_list[i])):
#         sectionListPrint = sectionListPrint + \
#                            f'<li><a href="{i}.{j + 1}-{hyphenateText(topics_list[i][j])}.html">{i}.{j + 1} — ' \
#                            f'{topics_list[i][j]}</a></li>'
#     print(sectionListPrint)
#     for line in fin:
#         fout.write(line.replace(f'<!--#unit{i}sections#-->', sectionListPrint))


# hey u hoe, u see those placeholders in the content-sections.html file for the section list? yea bitch, \
# u gotta figure out how to make a loop that replaces each one of those placeholders with the appropriate unit number.
