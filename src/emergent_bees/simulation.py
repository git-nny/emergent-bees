import dot_types as d 

if __name__ == "__main__":


  simulation = d.create_simulation()

  # Testpunkt
  simulation.add_dot(1, 5, 3, 4, 5)
  simulation.add_dot(1, 8, 3, 4, 5)
  simulation.add_dot(1, 2, 6, 4, 5)
  simulation.add_dot(1, 4, 3, 4, 5)
  simulation.add_dot(1, 2, 6, 4, 5)

  #print(simulation.dots)
  for _ in range(20):
    print(simulation.wiggle_dots())

