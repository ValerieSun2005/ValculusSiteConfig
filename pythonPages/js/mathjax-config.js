window.MathJax = {
    options: {
        enableMenu: false,    
    },
    
    svg: {
        fontCache: 'global',
    },

    "fast-preview": { 
        "disabled": false 
    }, 

    tex: {
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
            eqRefer: ["\\text{Eq. } \\eqref{#1}", 1],
            deriv: ["\\frac{\\dd #1}{\\dd #2}", 2]
        }
    },

};
    
