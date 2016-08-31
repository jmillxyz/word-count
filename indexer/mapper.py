from multiprocessing import Pool


class Mapper:

    def __init__(self, prep_fn, map_fn, num_workers=None):
        """Initialize a Mapper object.

        Each Mapper will apply map_fn to data, using num_workers in a
        multiprocessing pool.

        Args:
            prep_fn (func): Prepare data for map_fn.

            map_fn (func): The function to use, with input.

            num_workers (int): The number of multiprocessing pool workers.
            Defaults to the number of host CPUs.

        Returns:
            Mapper instance.
        """
        self.prep_fn = prep_fn
        self.map_fn = map_fn
        self.pool = Pool(num_workers)

    def __call__(self, inputs):
        """Process the inputs through the mapping function.

        """
        prep_results = self.pool.map(self.prep_fn, inputs)
        map_results = self.pool.map(self.map_fn, prep_results)
        self.pool.close()
        self.pool.join()
        return map_results

