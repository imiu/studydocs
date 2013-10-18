#!/usr/bin/env zsh
watchmedo shell-command --patterns='*' --command='sml < hw2test.sml | grep -E "false|$" && echo "\n------------------------------\n"' ./

