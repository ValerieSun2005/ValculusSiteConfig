# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re
import pageCreate


def hyphenateText(text):
    newText = text.replace(' ', '-')
    return (newText)

# for i in range(0, len(unit3SectionInfo)):
#     print(unit3SectionInfo[topicsUnit3[i]])

# for i in range(0, 1 + len(topics_list)):
#     for j in range(0, len(topics_list[i])):
#         sectionLabelHyphenated = hyphenateText(topics_list[i][j])   # convert spaces in file name to hyphens
#         try:
#             os.mkdir(f"F:/Valculus/sectionMaterials/{topics_list[i][j]}")
#             with open(f"F:/Valculus/sectionMaterials/{topics_list[i][j]}/content-{sectionLabelHyphenated}.html",
#                       'x') as htmlContent:
#                 htmlContent.write('')
#             with open(f"F:/Valculus/sectionMaterials/{topics_list[i][j]}/exerciseList-{sectionLabelHyphenated}.html",
#                       'x') as htmlExerciseList:
#                 htmlExerciseList.write('')
#         except:
#             pass
#
#         try:
#             pageCreate.create_all_pages(f'{i}.{j + 1}', f'{topics_list[i][j]}', f'{i}')
#         except:
#             pass


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
