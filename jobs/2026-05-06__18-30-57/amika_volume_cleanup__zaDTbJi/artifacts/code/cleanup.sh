#!/bin/bash

# Delete the sandbox named 'orphaned-box' and explicitly remove its volumes
amika sandbox delete orphaned-box --delete-volumes --force
