# Use test data as input (easier than overriding stdin)
if 'Puzzle-Playground' in __file__:
    simulated = """"""

    def input_generator():
        for line in simulated.split('\n'):
            yield line
    gen = input_generator()

    def input():
        return next(gen)
    
