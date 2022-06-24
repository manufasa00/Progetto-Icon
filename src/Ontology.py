# -*- coding: utf-8 -*-
from owlready2 import *

print("ONTOLOGY\n")
onto = get_ontology("videoteca.owl").load()

# print the main content of ontology
print("Class list in ontology:\n")
print(list(onto.classes()), "\n")

#print the object properties
print("Object property in ontology:\n")
print(list(onto.object_properties()), "\n")

#print the data properties
print("Data property in ontology:\n")
print(list(onto.data_properties()), "\n")

#print the individuals
print("Customer list in ontology:\n")
customers = onto.search(is_a = onto.Customer)
print(customers, "\n")

print("Salesperson list in ontology:\n")
salesperson = onto.search(is_a = onto.Salesperson)
print(salesperson, "\n")

print("Actor list in ontology:\n")
actors = onto.search(is_a = onto.Actor)
print(actors, "\n")

print("Movie list in ontology:\n")
movies = onto.search(is_a = onto.Movie)
print(movies, "\n")

print("Director list in ontology:\n")
directors = onto.search(is_a = onto.Director)
print(directors, "\n")

print("Format list in ontology:\n")
formats = onto.search(is_a = onto.Format)
print(formats, "\n")

print("Genre list in ontology:\n")
genres = onto.search(is_a = onto.Genre)
print(genres, "\n")

print("Shelf list in ontology:\n")
shelfs = onto.search(is_a = onto.Shelf)
print(shelfs, "\n")

print("Shop list in ontology:\n")
shops = onto.search(is_a = onto.Shop)
print(shops, "\n")

#example queries
print("List of movies in DVD format:\n")
film = onto.search(is_a = onto.Movie, hasFormat = onto.search(is_a = onto.DVD))
print(film, "\n")

print("List of comedy films:\n")
film = onto.search(is_a = onto.Movie, hasGenre = onto.search(is_a = onto.Comedy))
print(film, "\n")







