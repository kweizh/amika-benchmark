#!/bin/bash

# This script deletes the 'orphaned-box' sandbox and explicitly removes its volumes.
# It uses the --delete-volumes flag to ensure rwcopy volumes are cleaned up.
# The --force flag is used to skip the confirmation prompt.

amika sandbox delete orphaned-box --delete-volumes --force
