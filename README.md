# pyGSO

Python implementation of the Glowworm Swarm Optimization (GSO) algorithm.

Algorithm is described in:
Krishnanand, K.N. and Ghose, D. 2009.
Glowworm swarm optimization for simultaneous capture of multiple local
optima of multimodal functions. *Swarm Intelligence*, **3**, 2, June 2009,
87-124. DOI: [ https://doi.org/10.1007/s11721-008-0021-5]( https://doi.org/10.1007/s11721-008-0021-5)

## How to use it?

Following example is self-explanatory:

```python
# Custom optimization function inherits from ObjectiveFunction class:
class Rastrigin(ObjectiveFunction):
    """Rastrigin function"""

    def __call__(self, coordinates):
        return Rastrigin.calculate(coordinates[0], coordinates[1])

    @staticmethod
    def calculate(x, y):
        return (
            20.0 + (x*x - 10.0*cos(2*pi*x) + y*y - 10.0*cos(2*pi*y))
        )

# New instance of the function to optimize
objective_function = Rastrigin()

# Limits of the function to be sampled, one instance of Boundary 
# for each dimension:
bounding_box = BoundingBox([Boundary(-3.0, 3.0), Boundary(-3.0, 3.0)])

# Number of glowworms of the simulation
number_of_glowworms = 200

# Random number generator for producing starting glowworm positions in the
# function landscape
seed = 324324
random_number_generator = MTGenerator(seed)

# Parameters of the algorithm (rho, beta, etc. with default values)
parameters = GSOParameters()

# Algorithm factory
builder = GSOBuilder() 
gso = builder.create(
    number_of_glowworms,
    random_number_generator,
    parameters,
    objective_function,
    bounding_box,
)

# Run this optimization for 50 steps
gso.run(50)
```

To check the final space position of the glowworms:

```python
print(gso.swarm)
```

More information about the library use might be found on [test_gso.py](test/test_gso.py).
