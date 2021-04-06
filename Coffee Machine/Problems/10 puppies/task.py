class Puppy:
    n_puppies = 0

    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return object.__new__(cls)
