#! /usr/bin/env python2.7

from subprocess import call

repo           = "--repo=https://github.com/phrb/gce_autotuning_example.git"
project        = "--project=autotuning-1116"
interface_path = "--interface-path=rosenbrock.py"
interface_name = "--interface-name=Rosenbrock"
instances      = "--instances=4"
parallelism    = "--parallelism=16"
results_log    = "--results-log=results.log"
stop_after     = "--stop-after=180"

cmd = "/usr/bin/env python2.7 rosenbrock.py {0} {1} {2} {3} {4} {5} {6} {7}".format(stop_after,
                                                                                    repo,
                                                                                    project,
                                                                                    interface_path,
                                                                                    interface_name,
                                                                                    instances,
                                                                                    parallelism,
                                                                                    results_log)

print cmd

retcode = call(cmd, shell=True)
