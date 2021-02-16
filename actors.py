import os, json

# https://github.com/prust/wikipedia-movie-data/blob/master/movies.json

movies_file = "./movies.json"

def load_movie_file(image_info_file):
    obj = None
    if os.path.isfile(image_info_file):
        print("opening info file: %s" % image_info_file)
        with open(image_info_file) as json_file:
            try:
                obj = json.load(json_file)
            except ValueError:
                print("Unable to parse json data from file");
    else: # file does not exist
        # TODO
        print("info file does not exist: %s" % image_info_file)

    return obj


############################################

movie_data = load_movie_file(movies_file)

actors = ['cameron diaz', 'tom cruise']

movie_count = 0
for movie in movie_data:
    cast = map(unicode.lower,movie['cast'])

    for (idx, a) in enumerate(actors):
        if a not in cast:
            break
        if idx == len(actors) - 1:
            print("\t{}".format(movie['title']))
            movie_count = movie_count + 1
if movie_count == 0:
    print("\t no movies found")
