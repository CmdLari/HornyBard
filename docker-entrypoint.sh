#!/bin/sh

set -e

exec su-exec discord:discord python hornyBard.py "$@"
