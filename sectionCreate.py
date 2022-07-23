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


topicsUnit0 = ["Quadratics",
               "Exponential and Logarithmic Functions",
               "Trigonometry",
               "Graphing Functions",
               "Graphing Calculator Practice"]

unit0SectionInfo = {topicsUnit0[0]: "Quadratics in standard, vertex, and intercept forms."
                                    "Review of factoring, completing the square,"
                                    "the discriminant, and the quadratic formula. "
                                    "Classifying solution types; determining minima and maxima;"
                                    "and identifying defining features of parabolas: intercepts, axis of symmetry,"
                                    "and vertex.",
                    topicsUnit0[1]: "Graphing exponential and logarithmic functions."
                                    "Solving equations of exponents and logarithms, and their relationship"
                                    "as inverse functions.",
                    topicsUnit0[2]: "Overview of trig functions and inverse trig functions."
                                    "Review of graphs, trig identities, domain and range, and the unit circle."
                                    "Solving of trig equations and simplification of trig expressions.",
                    topicsUnit0[3]: "Graphs of common parent functions, including polynomial, exponential, logarithmic,"
                                    "radical, trigonometric, and inverse functions. Discussion of phase shifts, "
                                    "vertical translations, and horizontal and vertical dilation.",
                    topicsUnit0[4]: "Practice using technology to solve equations and graph functions."
                    }

topicsUnit1 = ["Defining a Limit",
               "Limit Properties",
               "Evaluating Limits Algebraically",
               "Determining Continuity",
               "Intermediate Value Theorem",
               "Squeeze Theorem",
               "Formal Definition of a Limit"
               ]

unit1SectionInfo = {topicsUnit1[0]: "Definition of a limit."
                                    "Estimation of limits from tables, graphs, and numerical approximations.",
                    topicsUnit1[1]: "Properties of limits."
                                    "Limits of sums, differences, products, quotients, and compositions of limits.",
                    topicsUnit1[2]: "Calculating limits of indeterminate form \(0/0\) by algebraic manipulation."
                                    "Techniques of factoring, rationalization, adding of fractions,"
                                    "and trig identities.",
                    topicsUnit1[3]: "Formal definition of continuity."
                                    "Finding intervals on which a sum, difference, product, quotient, or composition"
                                    "of functions is continuous, using limit properties."
                                    "vertical translations, and horizontal and vertical dilation.",
                    topicsUnit1[4]: "Introduction and proof of Intermediate Value Theorem."
                                    "Use of theorem to prove existence of numbers in an interval.",
                    topicsUnit1[5]: "Introduction and proof of Squeeze Theorem."
                                    "Derivation of the fundamental limits \(\lim_{x \to 0} \frac{\sin x}{x} = 0\),"
                                    "\(\lim_{x \to 0} \frac{\cos x}{x} = 1,\)"
                                    "and \(\lim_{x \to 0} \frac{e^x - 1}{x} = 1.\)",
                    topicsUnit1[6]: "Use of error analysis, the Delta-Epsilon definition, to formally define a limit."
                                    "Inclusion of geometric intuition and algebraic problem-solving."
                    }

topicsUnit2 = ["Defining a Derivative",
               "Product and Quotient Rules",
               "Chain Rule",
               "Implicit Differentiation",
               "Inverse Differentiation",
               "Hyperbolic Functions",
               "Logarithmic Differentiation"
               ]

unit2SectionInfo = {topicsUnit2[0]: "Limit definition of a derivative, with geometric intuition and motivation."
                                    "Finding tangent and normal lines to establish linear approximations."
                                    "First- and second-order derivatives."
                                    "Derivatives of transcendental functions:"
                                    "\(\sin x,\) \(\cos x,\) \(e^x,\) and \(\ln x.\)",
                    topicsUnit2[1]: "Differentiating products and quotients of functions."
                                    "Algebraic and graphical applications."
                                    "Contains geometric intuition and proof.",
                    topicsUnit2[2]: "Differentiating compositions of functions."
                                    "Algebraic and graphical applications."
                                    "Contains geometric intuition and proof.",
                    topicsUnit2[3]: "Differentiating implicit equations. First- and second-order derivatives.",
                    topicsUnit2[4]: "Differentiating inverse functions. "
                                    "Contains proof and geometric intuition."
                                    "Algebraic, graphical, and tabular applications.",
                    topicsUnit2[5]: "Introduction to hyperbolic functions and their derivatives."
                                    "Contains applications to physics and structural design.",
                    topicsUnit2[6]: "The use of natural logarithms to simplify products, quotients, and compositions"
                                    "of functions for easier differentiation."
                    }

topicsUnit3 = ["Minimum and Maximum Values",
               "Concavity and Inflection Points",
               "Mean Value Theorem and Rolle's Theorem",
               "Indeterminate Forms and L'Hopital's Rule",
               "Curve Sketching",
               "Related Rates",
               "Optimization",
               "Newton's Method"
               ]

unit3SectionInfo = {topicsUnit3[0]: "Overview of critical points and the First Derivative Test."
                                    "Extreme Value Theorem to establish presence of a function's minimum or maximum."
                                    "Process of finding relative and absolute extrema.",
                    topicsUnit3[1]: "Definition of concavity and points of inflection."
                                     "Geometric interpretation of concavity and its effect on a graph's shape.",
                    topicsUnit3[2]: "Overview and proof of Mean Value Theorem and Rolle's Theorem."
                                    "Use of Rolle's Theorem to prove the existence of zeros on an interval.",
                    topicsUnit3[3]: "Evaluating limits of indeterminate forms: \(\frac{0}{0},\)"
                                    "\(\frac{\infty}{\infty},\) \(0 \times \infty,\) \(\infty - \infty,\)"
                                    "\(0^0,\) \(1^\infty,\) and \(\infty^0.\)",
                    topicsUnit3[4]: "Link graphs of \(f,\) \(f',\) and \(f''.\)"
                                    "Using calculus-based procedures to sketch graphs of curves.",
                    topicsUnit3[5]: "Problems in which quantities change."
                                    "Inclusion of geometric, physical, and map problems.",
                    topicsUnit3[6]: "The use of natural logarithms to simplify products, quotients, and compositions"
                                    "of functions for easier differentiation."
                    }

topicsUnit4 = ["Defining an Antiderivative",
               "Definite Integrals",
               "Fundamental Theorem of Calculus",
               "U-Substitution",
               "Mean Value Theorem for Integrals"
               ]

topicsUnit5 = ["Areas Between Curves",
               "Arc Length",
               "Volumes by Solids of Revolution",
               "Surface Area of Revolution",
               "Probability",
               "Work",
               "Center of Mass",
               "Hydrostatic Pressure"
               ]

topicsUnit6 = ["Integration by Parts",
               "Trigonometric Integrals",
               "Trigonometric Substitution",
               "Integration by Partial Fractions",
               "Improper Integrals"
               ]

topicsUnit7 = ["Defining a Differential Equation",
               "Verifying Solutions to Differential Equations",
               "Slope Fields",
               "Euler's Method",
               "Separation of Variables",
               "Exponential and Logistic Growth",
               ]

topicsUnit8 = ["Overview of Parametric Functions",
               "Differentiating Parametric Functions",
               "Position, Velocity, and Acceleration",
               "Speed and Distance Traveled",
               "Areas of Parametric Curves",
               "Parametric Arc Length",
               ]

topicsUnit9 = ["Overview of Polar Functions",
               "Differentiating Polar Functions",
               "Areas of Polar Curves",
               "Surface Area of Polar Curves",
               "Conic Sections of Polar Functions"
               ]

topicsUnit10 = ["Overview of Infinite Sequences and Series",
                "Infinite Geometric Series",
                "Binomial Series",
                "Telescoping Series",
                "Comparison Tests",
                "Alternating Series Test",
                "Absolute and Conditional Convergence",
                "Ratio and Root Tests",
                "Integral Test",
                "Power Series with Geometric Series",
                "Maclaurin and Taylor Series",
                "Alternating Series Error Bound",
                "Lagrange Error Bound",
                "Remainders with Integral Test"
                ]

topicsInfo = [unit0SectionInfo, unit1SectionInfo, unit2SectionInfo, unit3SectionInfo]

topicsList = [topicsUnit0,
              topicsUnit1,
              topicsUnit2,
              topicsUnit3,
              topicsUnit4,
              topicsUnit5,
              topicsUnit6,
              topicsUnit7,
              topicsUnit8,
              topicsUnit9,
              topicsUnit10]

topicsUnitNames = [
    "Preliminaries",
    "Limits and Continuity",
    "Differentiation",
    "Applications of Differentiation",
    "Integration",
    "Applications of Integration",
    "Further Integration Techniques",
    "Differential Equations",
    "Parametric Calculus",
    "Polar Calculus",
    "Infinite Series and Sequences",
]

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
