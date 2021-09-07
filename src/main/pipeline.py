
class Pipeline:

    def __init__(self, stages):
        self.stages = stages

    def run(self, num, factor):
        new_val = num
        for stage in self.stages:
            new_val = stage(new_val, factor)
        return new_val
