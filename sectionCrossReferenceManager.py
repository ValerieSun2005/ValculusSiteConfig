import os
import re
import pageCreate

def hyphenateText(text):
    newText = text.replace(' ', '-')
    return newText


def sectionPageTag(sectionNameHyphenated):
    return(f'<!--[[[crefId.{sectionNameHyphenated}]]]--> \n')

def exercisePageTag(exerciseNameHyphenated):
    return(f'<!--[[[crefId.{exerciseNameHyphenated}-exercises]]]--> \n')

def crossReference(crossRef):
    crossRefContent = re.split('<!--\[\[\[cref.|]]]-->', crossRef)[1]
    return crossRefContent

os.listdir('sectionMaterials')

res = []  # list all the directories in "sectionMaterials/"

def tagSectionMaterials():
    for path in os.listdir('sectionMaterials'):
        if os.path.isdir(os.path.join('sectionMaterials', path)):
            res.append(path)

    # tag all the section pages

    for i in range(0, len(res)):
        try:
            sectionName = res[i]
            sectionNameHyphenated = hyphenateText(sectionName)
            with open(f'sectionMaterials/{sectionName}/content-{hyphenateText(sectionName)}.html', 'r', encoding='utf-8') \
                    as sectionPage:
                with open(f'sectionMaterials/{sectionName}/content-{hyphenateText(sectionName)}-copy.html', 'a+',
                          encoding='utf-8') as sectionPageCopy:  # make blank copy of html sections page
                    if sectionPageTag(sectionName) == sectionPage.readline():
                        pass  # if a tag already is present, then skip. otherwise, add the tag
                    else:
                        sectionPageCopy.write(sectionPageTag(hyphenateText(res[i])))
                        sectionPageCopy.write(sectionPage.read())   # place tag on first line of blank copy
            os.remove(f'sectionMaterials/{sectionName}/content-{hyphenateText(sectionName)}.html')   # delete original file
            os.rename(f'sectionMaterials/{sectionName}/content-{hyphenateText(sectionName)}-copy.html',
                      f'sectionMaterials/{sectionName}/content-{hyphenateText(sectionName)}.html')  # rename copy to
            # original

        except FileNotFoundError:
            sectionName = res[i]
            print(f"Exception-tag. {sectionName}-exercises was not found and therefore could not be tagged.")

# scan through all the html files in sectionMaterials (both section and exercises pages) to find any references.
# references in the html files are in the form  " <!--[section name, hyphenated]--> ".

def insertReferences():
    for file in os.listdir('Valculus/calculus'):  # scan all the main page files
        with open(os.path.join(os.getcwd(), f'Valculus/calculus/{file}'), 'r') as f:
            fileLines = f.readlines()
            f.close()
        with open(os.path.join(os.getcwd(), f'Valculus/calculus/{file}'), 'r') as f:
            fileContent = f.read()
            f.close()

        crossRefSubstitute = fileContent
        for line in fileLines:
            if '<!--[[[cref.' in line:  # detect any cross-references in file
                crossRef = re.split('<!--\[\[\[cref.|]]]-->', line)[1]
                # scan all the main page files to check cross-ref
                for file2 in os.listdir('Valculus/calculus'):
                    if crossRef in file2 and 'exercises' not in file2:  # ref for section page
                        sectionNum = re.split('-', file2)[0]
                        # the redirect code to cross-ref'd page
                        crossRefLink = f'<a href="{pageCreate.rootDirectory}/calculus/{file2}">{sectionNum}</a>'
                        crossRefSubstitute = crossRefSubstitute.replace(f'<!--[[[cref.{crossRef}]]]-->', crossRefLink)  #replace crossRef with link
                        with open(os.path.join(os.getcwd(), f'Valculus/calculus/{file}'), 'w') as f:
                            f.write(crossRefSubstitute)  # replace crossRef with <a> link
                            f.close()
            else:
                pass

    # recheck all the files for any missing/hanging references
    for file in os.listdir('Valculus/calculus'):  # scan all the main page files
        with open(os.path.join(os.getcwd(), f'Valculus/calculus/{file}'), 'r') as f3:
            fileLines = f3.readlines()
        for line in fileLines:
            if '<!--[[[cref.' in line:
                crossRef = re.split('<!--\[\[\[cref.|]]]-->', line)[1]
                print(f'Exception-ref. In {file}, reference \"{crossRef}\" was not found')