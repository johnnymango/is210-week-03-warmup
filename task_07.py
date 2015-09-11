#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


import task_06

WORDS = task_06.WORDS

if 'granaries' in WORDS: GRANARIES_EXIST = 'Yes, This word exists.'
else: GRANARIES_EXIST = 'Sorry, This word does not exist.'

print GRANARIES_EXIST