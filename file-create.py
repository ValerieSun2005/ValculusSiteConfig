import os
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import re
import pageCreate

topics_unit_0 = ["Quadratics",
                 "Exponential and Logarithmic Functions",
                 "Trigonometry",
                 "Graphs of Common Functions",
                 "Graphing Calculator Practice"]

topics_unit_1 = ["Defining a Limit",
                 "Limit Properties",
                 "Evaluating Limits Algebraically",
                 "Determining Continuity",
                 "The Intermediate Value Theorem",
                 "The Squeeze Theorem",
                 "Important Limits"
                 ]

topics_unit_2 = ["Defining a Derivative",
                 "The Product and Quotient Rules",
                 "The Chain Rule",
                 "Implicit Differentiation",
                 "Inverse Differentiation",
                 "Hyperbolic Functions",
                 "Logarithmic Differentiation"
                 ]

topics_unit_3 = ["Minimum and Maximum Values",
                 "Concavity and Inflection Points",
                 "The Mean Value Theorem and Rolle's Theorem",
                 "Indeterminate Forms and L'Hopital's Rule",
                 "Curve Sketching",
                 "Related Rates",
                 "Optimization",
                 "Newton's Method"
                 ]

topics_unit_4 = ["Defining an Antiderivative",
                 "Definite Integrals",
                 "Fundamental Theorem of Calculus",
                 "U-Substitution",
                 "Mean Value Theorem for Integrlas"
                 ]

topics_unit_5 = ["Areas Between Curves",
                 "Arc Length",
                 "Volumes by Solids of Revolution",
                 "Surface Area of Revolution",
                 "Probability",
                 "Work",
                 "Center of Mass",
                 "Hydrostatic Pressure"
                 ]

topics_unit_6 = ["Integration by Parts",
                 "Trigonometric Integrals",
                 "Trigonometric Substitution",
                 "Integration by Partial Fractions",
                 "Improper Integrals"
                 ]

topics_unit_7 = ["Defining a Differential Equation",
                 "Verifying Solutions to Differential Equations",
                 "Slope Fields",
                 "Euler's Method",
                 "Separation of Variables",
                 "Exponential and Logistic Growth",
                 ]

topics_unit_8 = ["Overview of Parametric Functions",
                 "Differentiating Parametric Functions",
                 "Position, Velocity, and Acceleration",
                 "Speed and Distance Traveled",
                 "Areas of Parametric Curves",
                 "Parametric Arc Length",
                 ]

topics_unit_9 = ["Overview of Polar Functions",
                 "Differentiating Polar Functions",
                 "Areas of Polar Curves",
                 "Surface Area of Polar Curves",
                 "Conic Sections of Polar Functions"
                 ]

topics_unit_10 = ["Overview of Infinite Sequences and Series",
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
                  "Alternating Series Error Bound"
                  "Lagrange Error Bound",
                  "Remainders with Integral Test"
                  ]

topics_list = [topics_unit_0,
               topics_unit_1,
               topics_unit_2,
               topics_unit_3,
               topics_unit_4,
               topics_unit_5,
               topics_unit_6,
               topics_unit_7,
               topics_unit_8,
               topics_unit_9,
               topics_unit_10]


for i in range(0, 11):
    try:
        os.mkdir(f"F:/Valculus/sectionMaterials/{i}")
    except:
        pass

    for j in range(0, len(topics_list[i])):
        try:
            os.mkdir(f"F:/Valculus/sectionMaterials/{i}/{i}.{j + 1}-{topics_list[i][j]}")
        except:
            pass

        # with open(f"F:/Valculus/sectionMaterials/{i}/{i}.{j + 1}-{topics_list[i][j]}/{i}.{j + 1}-exerciseList.html",
        #           'w') as htmlContent:
        #     htmlContent.write('')
        # with open(f"F:/Valculus/sectionMaterials/{i}/{i}.{j + 1}-{topics_list[i][j]}/{i}.{j + 1}-content.html",
        #           'w') as htmlExerciseList:
        #     htmlExerciseList.write('')
        try:
            pageCreate.create_all_pages(f'{i}.{j + 1}', f'{topics_list[i][j]}', f'{i}')
        except:
            pass


