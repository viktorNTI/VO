import argparse, os, csv #Importera modulerna 
parser = argparse.ArgumentParser() #Bestämmer vad variabeln parser ska göra
parser.add_argument("--file", "-f", type=str , help="increase output file verbosity") #Specifierar vad cmdline ska kunna hantera via argument
args = parser.parse_args() #Returnerar data från filen vi specifierade med argumentet tidigare
print(args.file) #Bestämmer att den ska hämta från "file"
with open(args.file, newline='') as csvfile: #Öppnar den tidigare specifierade "file" som en CSV-fil
    reader = csv.DictReader(csvfile) #Använder reader funktionen för att läsa CSV-filen vi just öppnade
    for row in reader: #För varje rad i filen...
        print(row) #...Så skriver vi ut varje rad


#python VO.py --file students.csv 
#Kommandot vi kör i terminalen som låter oss skriva ut allt i CSV-filen