# -*- coding: utf-8 -*-

import owlready2 as owl
import os



print("ONTOLOGIA\n")
onto = owl.get_ontology("videoteca.owl").load()
print("Lista classi nella ontologia:\n")
print(list(onto.classes()), "\n")

