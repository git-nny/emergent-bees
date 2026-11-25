# Emergent-Bees

## Klassen

``` mermaid
classDiagram

    Dot_Mother --> Dot_Type : erzeugt
    Dot_Type --> Dot_Instances
    GUI --> Dot_Instances
    SimulationConfig --> GUI

    class Dot_Mother{
        + int random_noise = random int
    }

    class Dot_Type{
        + int type_id
        + interact()
        + int time_to_live
        + int styling
        + float max_range
    }

    class Dot_Instances{
        + int type_id
        + [int, int] current_movement
        + nparray current_position_x
        + nparray current_position_y
        + int array_size
    } 

    class GUI{
        window()
        regulator()

    }


    class SimulationConfig{

            + int n_particles
            + int n_types
            + int seed

    + calculate new positions()

    }
```

- Reibung, Interaktion für Geschwindigkeit
- in array-struktur
    Container -> nd.array 
    - Dinge eher einzeln mit Typ Numpy array

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