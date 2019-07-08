import csv

with open('title.basics.tsv', 'r') as productions:

    productionsReader = csv.reader(productions, delimiter='\t')

    with open('testingWriterMovies.tsv', 'w') as movies:
        moviesWriter = csv.writer(movies, delimiter='\t')

        for line in productionsReader:
            if line[0] == "tconst": #prints tbv headers at top of page
                moviesWriter.writerow(line)
            if line[1] == "movie": #if the titleType of the production is a movie
                moviesWriter.writerow(line)
