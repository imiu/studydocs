#!/usr/bin/env zsh
watchmedo shell-command --patterns='*' --command='py.test -q' ./ &&
watchmedo shell-command --patterns='*' --command='py.test -q' ./tests
