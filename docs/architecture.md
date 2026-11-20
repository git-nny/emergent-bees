# Emergent-Bees

## Klassen

``` mermaid
classDiagram

    Dot <-- Dot_Type
    Dot_Type <-- Dot_Instance

    class Dot{
        + class_id
        + current_movement
        + current_position
    }

    class Dot_Type{
        + int type_id
        + interact()
        + int time_to_live
        + int styling
    }

    class Dot_Instance{
        + int type_id
    } 
```

## Typen
Dot
-> Sachen, die alle Dots gemein haben und gemeinsam erben. Geschwindigkeit findet sich in Größe des Bewegungsvektors (?)

Dot_Type
-> einzelne Dot Klassen. Styling, Attraction, verbleibende Lebenszeit werden gespeichert

Dot_Instance
-> der einzelne Punkt (keine eigene Klasse, sondern Instanz des Typens)

## Inhalt:
    
- Wer führt einen Simulationsschritt aus? -> der User :)
- Wie gelangt der aktuelle Zustand zur Visualisierung? Numpy berechnet, zweites Programm nur zum Rendern
- Wie können Simulation und Benchmark ohne GUI laufen?
-> print-statements für 1-2 Punkte :) und nur ein Punkt (mit festem Seed?)


## Special Gimmicks (Game of Life)
- Lebensdauer?
- Fortpflanzung (via Maiose)