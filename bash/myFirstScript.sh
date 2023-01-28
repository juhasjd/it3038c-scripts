#!/bin/bash

# This script outputs th eIP address and Hostname offf a machine =

echo Machine Type: $MACHTYPE
echo HostName: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME

a=$(ip a | grep 'noprefixroute dynamic ens192' | awk '{print $2}')
echo My IP is $a
