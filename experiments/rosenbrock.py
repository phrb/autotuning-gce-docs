#! /usr/bin/env python2.7

import adddeps
import argparse
import logging

import opentuner
from opentuner.measurement import MeasurementInterface
from opentuner.search.manipulator import ConfigurationManipulator
from opentuner.search.manipulator import FloatParameter

import measurement_client
from measurement_client.client import MeasurementClient
from measurement_client.gce_interface.interface import GCEInterface

log = logging.getLogger(__name__)

parsers = opentuner.argparsers() + measurement_client.argparsers()

parser = argparse.ArgumentParser(parents = parsers)
parser.add_argument('--dimensions', type=int, default=2,
                    help='dimensions for the Rosenbrock function')
parser.add_argument('--domain', type=float, default=1000,
                    help='bound for variables in each dimension')
parser.add_argument('--function', default='rosenbrock',
                    choices=('rosenbrock', 'sphere', 'beale'),
                    help='function to use')

class Rosenbrock(MeasurementInterface):
    def run(self, desired_result, input, limit):
        cfg = desired_result.configuration.data
        val = 0.0
        x0 = cfg[0]
        x1 = cfg[1]
        val += 100.0 * (x1 - x0 ** 2) ** 2 + (x0 - 1) ** 2
        return opentuner.resultsdb.models.Result(time=val)

    def manipulator(self):
        manipulator = ConfigurationManipulator()
        for d in xrange(self.args.dimensions):
            manipulator.add_parameter(FloatParameter(d,
                                                     -self.args.domain,
                                                     self.args.domain))
        return manipulator

    def save_final_config(self, configuration):
        self.driver.gce_interface.delete_all()
        print "Final configuration", configuration.data

    @classmethod
    def main(cls, args, *pargs, **kwargs):
        from opentuner.tuningrunmain import TuningRunMain
        return TuningRunMain(cls(args, *pargs, **kwargs), args,
                             measurement_driver = MeasurementClient).main()


if __name__ == '__main__':
    args = parser.parse_args()
    Rosenbrock.main(args)
