# Autotuning with the Google Compute Engine

This repository contains an example application that uses GCE resources and the OpenTuner autotuning framework.

The `MeasurementClient` class is an OpenTuner `MeasurementDriver` that uses an interface to the GCE API
to send result requests to a server in a GCE virtual machine. The server is hosted in [this repository](https://github.com/phrb/measurement-server).

This git repository contains the `measurement_client` ([repo](https://github.com/phrb/measurement_client))
and the `gce_interface`([repo](https://github.com/phrb/gce_interface)) as git submodules. To clone this
project and its submodules run:

```
$ git clone --recursive https://github.com/phrb/gce_autotuning_example.git
```

To run the example, you have to either copy the [full startup script](https://github.com/phrb/gce_interface/blob/master/startup-script.sh) to this project 
or build a private image, using the commands in the script. You also have to install 
the dependencies that can be found in the startup script. In a Debian Jessie, run:

```
$ sudo apt-get install git python-pip python-dev python-matplotlib libsqlite3-dev libfreetype6-dev
$ sudo pip install --upgrade oauth2client google-api-python-client
$ sudo pip install opentuner
```

Search for the correspondent packages for different distributions.
Now you have to change the project name in `run.py` and enable `gcloud` on your machine. Then you can run:

```
$ python run.py
```

You can also pass options directly to the tuner. Check `run.py` or run the following for more information:

```
$ python rosenbrock.py -h
```
