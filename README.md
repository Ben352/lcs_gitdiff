# Git Diff

This project is an implementation of the git diff command. The command is based on the Longest Common Subsequence algorithm.
There are 3 different levels implement. The command can calculate the difference on a character level, word level and line level.

## Commands
The basic command for character level differnece is:
- `python3 diff file1 file 2`
The level can be specified with the `-l` argument
- `python3 diff file1 file2 -l word` for word level
- `python3 diff file1 file2 -l line` for line level
