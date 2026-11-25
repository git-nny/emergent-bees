import dot_types as d

if __name__ == "__main__":


  simulation = d.create_simulation()

  # Testpunkte
  simulation.add_dot(1, 2, 3, 4, 5)

  print(simulation.dots)

