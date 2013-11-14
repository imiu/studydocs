#!/usr/bin/env zsh
watchmedo shell-command --ignore-patterns='*pycache*' --command='py.test' ./

