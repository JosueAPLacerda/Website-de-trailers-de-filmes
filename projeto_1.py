# -*- coding: utf-8 -*-
import fresh_tomatoes
import media


def main():
    the_shining = media.Movie("The Shining",
                              "The Shining is a 1980 horror film produced and directed by Stanley Kubrick.",
                              "https://tyrannyoftradition.files.wordpress.com/2012/03/the-shining-poster.jpg",
                              "https://www.youtube.com/watch?v=5Cb3ik6zP2I&t=18s",
                              "12/25/1980")

    pi = media.Movie("Pi",
                     "Pi (stylized as π) is a 1998 American psychological thriller film written and directed by Darren"
                     " Aronofsky in his directorial debut.",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRttvbw14rh6S0ESqc3hopg71rylHYRtmcjSGe15LK_Z"
                     "4_ZPCvu",
                     "https://www.youtube.com/watch?v=gtLzuHd1mj4",
                     "08/07/1998")

    seven = media.Movie("Seven",
                        "Seven is american neo-noir crime thriller film directed by David Fincher and written by Andrew"
                        " Kevin Walker.",
                        "https://i.pinimg.com/originals/c7/ec/62/c7ec6285f6ba7fdbd29e3a9f3b5244f9.jpg",
                        "https://www.youtube.com/watch?v=pc3HGyfcd40",
                        "12/15/1995")

    eyes_wide_shut = media.Movie("Eyes Wide Shut",
                                 "Eyes Wide Shut is a 1999 erotic drama film directed, produced, and co-written by Stan"
                                 "ley Kubrick.",
                                 "https://images-na.ssl-images-amazon.com/images/I/81+ZHy6bdbL.jpg",
                                 "https://www.youtube.com/watch?v=zoTNVSArKxM",
                                 "07/16/1990")

    on_the_road = media.Movie("On the Road",
                              "On the Road is a novel by American writer Jack Kerouac, based on the travels of Kerouac "
                              "and his friends across the United States.",
                              "https://upload.wikimedia.org/wikipedia/pt/thumb/8/8f/On_the_Road.jpg/200px-On_the_Road"
                              ".jpg",
                              "https://www.youtube.com/watch?v=su75_mcryO4",
                              "07/13/2012")

    a_beautiful_mind = media.Movie("A Beautiful Mind",
                                   "A Beautiful Mind is a 2001 American biographical drama film based on the life of "
                                   "John Nash, a Nobel Laureate in Economics.",
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/A_Beautiful_Mind_Poster.jpg/2"
                                   "20px-A_Beautiful_Mind_Poster.jpg",
                                   "https://www.youtube.com/watch?v=WFJgUm7iOKw",
                                   "02/15/2002")
    movies = [the_shining, pi, seven, eyes_wide_shut, on_the_road, a_beautiful_mind]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
