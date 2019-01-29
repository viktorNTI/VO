import argparse, os, csv #Importera modulerna 
parser = argparse.ArgumentParser() #Bestämmer vad variabeln parser ska göra
parser.add_argument("--file", "-f",type=str ,help="increase output file verbosity") #Specifierar vad cmdline ska kunna hantera via argument
args = parser.parse_args() #Returnerar data från filen vi specifierade med argumentet tidigare
print(args.file) #Bestämmer vilken fil den ska ta ifrån
with open(args.file, newline=" ") as csvfile: #
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

