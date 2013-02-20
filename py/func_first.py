#!/usr/bin/env


class Unpacker(object):
    slices = {
        'header': slice(0, 3),
        'trailer': slice(12, 18),
        'middle': slice(6, 9),
    }

    def __init__(self, record):
        self.record = record

    def __getattr__(self, attr):
        if attr in self.slices:
            return self.record[self.slices[attr]]
        raise AttributeError(
            "'Unpacker' object has no attribute '{}'".format(attr)
        )
