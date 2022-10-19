import sys
import itertools

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

#-------------------------------------------------------------------------------#
class commands:
    HELP = f'''\n{bcolors.WARNING}Dorkfather{bcolors.ENDC} generates a list of dorks based on modules to help you find data sources and information relevant to the keywords you provide.\n
{bcolors.BOLD}{bcolors.OKGREEN}#  {bcolors.ENDC}->\t {bcolors.HEADER}{bcolors.BOLD}Usage:{bcolors.ENDC} {bcolors.WARNING}dorkfather{bcolors.ENDC} {bcolors.OKCYAN}<MODULE> <KEYWORD1,KEYWORD2,KEYWORD3, ...>{bcolors.ENDC}\n'''
    
    MODULES = f'''\n{bcolors.BOLD}{bcolors.OKGREEN}#  {bcolors.ENDC}->\t{bcolors.BOLD}Available modules:
- {bcolors.OKBLUE}{bcolors.BOLD}\t\t'1'{bcolors.ENDC} : {bcolors.WARNING}Dataset Module{bcolors.ENDC} - Generates dorks to find datasets containing information (i.e. Spreadsheets, Files, Databases, Data Dumps) relevant to the specified keywords.
- \t\t\t {bcolors.HEADER}Example:{bcolors.ENDC}
- \t\t\t\tCommand -> {bcolors.WARNING}dorkfather{bcolors.ENDC} 1 passwords
- \t\t\t\tGenerated Dork -> {bcolors.OKBLUE}inurl:google.com/spreadsheets/d/ "passwords"\n{bcolors.ENDC}'''
#-------------------------------------------------------------------------------#

def output(dorks:list):
    with open('dorkfather_generated_dorks.txt','a') as output_file:
        for dork in dorks:
            output_file.write(dork+'\n')

def createCombinations(keywords: list)->list:
    combinations = []
    for L in range(0, len(keywords)+1):
        for subset in itertools.combinations(keywords, L):
            if len(subset) > 1:
                    combinations.append(('"'+'" "'.join(subset)+'"'))
    return combinations

DORK_MODULES = ['intext:','inurl:','filetype:','intitle:','ext:','related:','site:']

DATASET_RELATED_URLS = ['google.com/spreadsheets/','pastebin.com/','ghostbin.me/','anonfiles.com/','drive.google.com/file/d/','controlc.com/','rentry.co/','gist.github.com/']
DATASET_RELATED_WORDS = ['spreadsheet','dataset','dump','data dump','data leak','data leaked','leaked data', 'data breach','data breached','breached data','information','repository','raw data']
DATA_ATTRIBUTES = ['email','username','address','gmail','yahoo','outlook','*mail','instagram','twitter','linkedin']
FILETYPES = ['pdf','csv','tsv','db']

def makeDorks(module: str, keywords: list)->list:
    dorks = []

    keywords_l = keywords[0].split(',')
    combs = createCombinations(keywords_l)

    if module == '1':

        # Using 'intext:' + Related words + Attributes
        for word in keywords_l:
            for r_word in DATASET_RELATED_WORDS:
                dorks.append(f'{DORK_MODULES[0]}{word} "{r_word}"')
                for attribute in DATA_ATTRIBUTES:
                    dorks.append(f'{DORK_MODULES[0]}{word} "{r_word}" "{attribute}"')


        for combination in combs:
            for r_word in DATASET_RELATED_WORDS:
                dorks.append(f'all{DORK_MODULES[0]}({combination}) "{r_word}"')
                for attribute in DATA_ATTRIBUTES:
                    dorks.append(f'all{DORK_MODULES[0]}{combination} "{r_word}" "{attribute}"')
            
        # Using 'inurl:' + Related URLs + Attributes
        for word in keywords_l:
            for url in DATASET_RELATED_URLS:
                dorks.append(f'{DORK_MODULES[1]}{url} "{word}"')
                for attribute in DATA_ATTRIBUTES:
                    dorks.append(f'{DORK_MODULES[1]}{url} "{word}" "{attribute}"')

        for combination in combs:
            for url in DATASET_RELATED_URLS:
                dorks.append(f'{DORK_MODULES[1]}{url} {combination}')
                for attribute in DATA_ATTRIBUTES:
                    dorks.append(f'{DORK_MODULES[1]}{url} {combination} "{attribute}"')
        
        # Using 'filetype:' + Related filetypes + Related Words + Attributes
        for word in keywords_l:
            for filetype in FILETYPES:
                dorks.append(f'{DORK_MODULES[2]}{filetype} "{word}"')
                for r_word in DATASET_RELATED_WORDS:
                    dorks.append(f'{DORK_MODULES[2]}{filetype} "{word}" "{r_word}"')
                    for attribute in DATA_ATTRIBUTES:
                        if f'{DORK_MODULES[2]}{filetype} "{word}" "{attribute}"' not in dorks: dorks.append(f'{DORK_MODULES[2]}{filetype} "{word}" "{attribute}"')
                        dorks.append(f'{DORK_MODULES[2]}{filetype} "{word}" "{r_word}" "{attribute}"')


        for combination in combs:
            for filetype in FILETYPES:
                dorks.append(f'{DORK_MODULES[2]}{filetype} {combination}')
                for r_word in DATASET_RELATED_WORDS:
                    dorks.append(f'{DORK_MODULES[2]}{filetype} {combination} "{r_word}"')
                    for attribute in DATA_ATTRIBUTES:
                        if f'{DORK_MODULES[2]}{filetype} {combination} "{attribute}"' not in dorks: dorks.append(f'{DORK_MODULES[2]}{filetype} {combination} "{attribute}"')
                        dorks.append(f'{DORK_MODULES[2]}{filetype} {combination} "{r_word}" "{attribute}"')
        
        #Using 'intitle:' + Related words + Attributes
        for word in keywords_l:
            for r_word in DATASET_RELATED_WORDS: 
                dorks.append(f'{DORK_MODULES[3]}{word} "{r_word}"')
                for attribute in DATA_ATTRIBUTES:
                    dorks.append(f'{DORK_MODULES[3]}{word} "{r_word}" "{attribute}"')
        
        for combination in combs:
            for r_word in DATASET_RELATED_WORDS: 
                dorks.append(f'all{DORK_MODULES[3]}({combination}) "{r_word}"')
                for attribute in DATA_ATTRIBUTES:
                    dorks.append(f'all{DORK_MODULES[3]}({combination}) "{r_word}" "{attribute}"')
        
        #Using 'ext:' + Related filetypes + Related Words + Attributes
        for word in keywords_l:
            for filetype in FILETYPES:
                dorks.append(f'{DORK_MODULES[4]}{filetype} "{word}"')
                for r_word in DATASET_RELATED_WORDS:
                    dorks.append(f'{DORK_MODULES[4]}{filetype} "{word}" "{r_word}"')
                    for attribute in DATA_ATTRIBUTES:
                        if f'{DORK_MODULES[4]}{filetype} "{word}" "{attribute}"' not in dorks: dorks.append(f'{DORK_MODULES[4]}{filetype} "{word}" "{attribute}"')
                        dorks.append(f'{DORK_MODULES[4]}{filetype} "{word}" "{r_word}" "{attribute}"')


        for combination in combs:
            for filetype in FILETYPES:
                dorks.append(f'{DORK_MODULES[4]}{filetype} {combination}')
                for r_word in DATASET_RELATED_WORDS:
                    dorks.append(f'{DORK_MODULES[4]}{filetype} {combination} "{r_word}"')
                    for attribute in DATA_ATTRIBUTES:
                        if f'{DORK_MODULES[4]}{filetype} {combination} "{attribute}"' not in dorks: dorks.append(f'{DORK_MODULES[4]}{filetype} {combination} "{attribute}"')
                        dorks.append(f'{DORK_MODULES[4]}{filetype} {combination} "{r_word}" "{attribute}"')
        
        #Using 'related:' + Related URLs + Attributes
        for word in keywords_l:
            for url in DATASET_RELATED_URLS:
                dorks.append(f'{DORK_MODULES[5]}{url} "{word}"')
                for attribute in DATA_ATTRIBUTES:
                    dorks.append(f'{DORK_MODULES[5]}{url} "{word}" "{attribute}"')

        for combination in combs:
            for url in DATASET_RELATED_URLS:
                dorks.append(f'{DORK_MODULES[5]}{url} {combination}')
                for attribute in DATA_ATTRIBUTES:
                    dorks.append(f'{DORK_MODULES[5]}{url} {combination} "{attribute}"')

    return dorks

def main():
    parsed_arguments = sys.argv[1:]
    try: 
        match parsed_arguments[0]:
            case '1':
                dorks = makeDorks(parsed_arguments[0],parsed_arguments[1:])
            case 'modules':
                print(commands.MODULES)
                return
            case 'help':
                print(commands.HELP)
                return
            case _:
                print(f"{bcolors.BOLD}{bcolors.FAIL}!  {bcolors.ENDC}->\t"f"Module with name {bcolors.WARNING}'{parsed_arguments[0]}'{bcolors.ENDC} was not found, try {bcolors.OKGREEN}'dorkfather modules'{bcolors.ENDC} to see the available modules or {bcolors.OKGREEN}'dorkfather help'{bcolors.ENDC} to see how dorkfather works.")
                return
    except:
        print(commands.HELP)
        return
    
    output(dorks)
    print(f'\n{bcolors.BOLD}{bcolors.OKGREEN}#  {bcolors.ENDC}->\t{bcolors.BOLD}{bcolors.OKGREEN}{bcolors.BOLD}Finished:{bcolors.ENDC} {bcolors.WARNING}Dorkfather{bcolors.ENDC} generated {len(dorks)} dorks.\n')
    
if __name__ == '__main__':
    main()