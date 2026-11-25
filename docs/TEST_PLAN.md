# Kernlogik
## Anforderungen
### Partikel Allgemein
- Dots können nicht die gleiche current_position_x und current_position_y haben (keine Überlappung)
- current_movement kann nur 2-D sein (nicht mehr, nicht weniger)
- ein Partikelarray hat nur ein Partikeltyp

### Simulation / Welt
- Berechnung des current_postion passiert erst in der Simulation, current_position wird ständig überschrieben
- die Welt hat periodische Grenzen, Wrap-around oder reflektierende Grenzen (Auf Typ einigen!)
- mind. 4 Partikeltypen müssen unterstützt werden
- Partikeltypen sind unterscheidbar
- Erweiterung der Arrays soll einfach zu Ändern sein
- Die Partikel agieren nur innerhalb ihrer Interaktionsmatrix
- In der Interaktionsmatrix ist jeder Partikeltyp enthalten
- Der Einfluss der Partikeltypen ist nur innerhalb ihres Einflussradius
- Noise funktioniert