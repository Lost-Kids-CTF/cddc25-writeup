#!/bin/bash

nsjail -Ml --port 6666 --user 99999 --group 99999 --time_limit 300 --chroot /jail -- oldgame -cols 10 -rows 10 -mines 99