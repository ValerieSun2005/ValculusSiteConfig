window.MathJax = {
    options: {
        enableMenu: false,    
    },

    "fast-preview": { 
        "disabled": false 
    }, 
    

    loader: {load: ['[tex]/color']},

    tex: {
        packages: {'[+]': ['color']},
        tags: 'ams',
        macros: {
            RR: "{\\bf R}",
            bold: ["{\\bf #1}", 1],
            notimplies: "\, \, \; \not \!\!\!\!\!\!\! \implies",
            dd: "{\\textrm{d}}",
            box: "\\bbox[border: 2px solid white, 2pt]",
            ppkn: "\\text{Ѽ}",
            heart:"\\text{♡}",
            flower: "\\text{✿}",
            ds: "\\displaystyle",
            ba: "\\begin{aligned}",
            ea: "\\end{aligned}",
            bc: "\\begin{cases}",
            ec: "\\end{cases}",
            nspace: "\\hspace{2.52mm}",
            geq: "\\geqslant",
            leq: "\\leqslant",
            txt: "\\textrm",
            deg: "\\textrm{deg}",
            be: "\\begin{equation}",
            ee: "\\end{equation}",
            and:"\\qquad \\text{and} \\qquad",
            comma: "\\, ,",
            period: "\\, .",
            ques: "\\; ?",
            col: "\\! :",
            scol: "\\, ; \\,",
            // eqref: ["\\color{pink}{(\\ref{#1})}", 1],
            eqRefer: ["\\text{Equation } \\eqref{#1}", 1],
            deriv: ["\\frac{\\dd #1}{\\dd #2}", 2],
            abs: ["\\left \\lvert #1 \\right \\rvert", 1],
            par: ["\\left ( #1 \\right )", 1],
            di: "\\, \\dd",
            nl: "\\\\[1ex]",
            indZero: "\\frac{0}{0}",
            indInfty: "\\infty/\\infty"
        }
    },

    svg: {
        fontCache: 'global',
        styles:{
            "svg-href": {
                fill: "red", stroke: "red"
              },
        },
    },
};
    
