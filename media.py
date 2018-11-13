# -*- coding: utf-8 -*-

"""Aqui é definida a classe Movie que contém os detalhes sobre um filme"""
import webbrowser


class Movie(object):
    """Esta classe armazena informações relacionadas ao filme.
    Atributos:
        title: uma string que armazena o título do filme.
        storyline: uma string que armazena uma curta sinopse do filme.
        poster_image_url: uma string que armazena a URL do poster do filme.
        trailer_youtube_url: uma string que armazena a URL do trailer do filme.
        release_date: uma string que armazena a data de lançamento do filme."""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release_date):
        """Inicializa as variáveis de instância da classe Movie"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.storyline = movie_storyline
        self.release_date = movie_release_date

    def show_trailer(self):
        """Roda o trailer do filme em um navegador de internet"""
        webbrowser.open(self.trailer_youtube_url)
