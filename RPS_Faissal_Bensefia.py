#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################LICENCE####################################
#Copyright (c) 2016 Faissal Bensefia
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
################################################################################
# Date:
#  30/09/2016
# Description:
#  An expandable ASCIIpunk rock, paper, scissors game built using ncurses
import curses
import random
objects=[
	[
		"  ▃▄▙",
		" ▟░█▉",
		" ▜▒▓▘",
		"  ▀  "
	],
	[
		".~~~.",
		"|:::|",
		"|:::|",
		"'~~~'"
	],
	[
		" Q ╱",
		"  ╳ ",
		" O ╲"
	]
]
objectNames=[
	"Rock",
	"Paper",
	"Scissor"
]
#Which item beats what
rules={
	"Rock":"Scissors",
	"Paper":"Rock",
	"Scissor":"Paper"
}
maxObjectWidth=0
for i in objects:
	for ii in i:
		if len(ii)>maxObjectWidth:
			maxObjectWidth=len(ii)

maxNameWidth=max([len(i) for i in objectNames])

scr=curses.initscr()
curses.start_color()
curses.noecho()
curses.curs_set(0)
curses.use_default_colors()
scr.keypad(True)
lastKey=0
selectedOption=0
userPoints=0
cpuPoints=0
while True:
	window_h,window_w=scr.getmaxyx()
	scr.clear()
	scr.addstr(0,(window_w-len("[Up, down, enter to play, Q to quit]"))//2,"[Up, down, enter to play, Q to quit]")
	scr.addstr(1,1,"Player ("+str(userPoints)+")")
	scr.addstr(1,window_w-maxObjectWidth-len("CPU ("+str(cpuPoints)+")")-3,"CPU ("+str(cpuPoints)+")")
	for i,j in enumerate(objects):
		for ii,jj in enumerate(j):
			#Player's sprite
			scr.addstr(3+ii+(i*maxObjectWidth),maxNameWidth+4,jj)
			#CPU's sprite
			scr.addstr(3+ii+(i*maxObjectWidth),window_w-maxObjectWidth-maxNameWidth-4,jj)
		if selectedOption==i:
			scr.addstr(3+i*maxObjectWidth,0,objectNames[i].ljust(maxNameWidth)+" ->")
	scr.refresh()
	lastKey=scr.getch()
	if lastKey==curses.KEY_UP:
		selectedOption=(selectedOption-1)%len(objects)
	elif lastKey==curses.KEY_DOWN:
		selectedOption=(selectedOption+1)%len(objects)
	elif lastKey==ord('\n'):
		#Players choice
		for i,j in enumerate(objects[selectedOption]):
			scr.addstr((window_h//2)+i,window_w//2-maxObjectWidth-4,j)
		#CPU Choice
		selectedCPUOption=random.randrange(len(objects))
		for i,j in enumerate(objects[selectedCPUOption]):
			scr.addstr((window_h//2)+i,window_w//2+4,j)
		if rules[objectNames[selectedCPUOption]]==objectNames[selectedOption]:
			scr.addstr((window_h//2)-2,(window_w-len("CPU wins!"))//2,"CPU wins!")
			cpuPoints+=1
		elif objectNames[selectedCPUOption]==objectNames[selectedOption]:
			scr.addstr((window_h//2)-2,(window_w-len("Tie!"))//2,"Tie!")
		else:
			scr.addstr((window_h//2)-2,(window_w-len("Player wins!"))//2,"Player wins!")
			userPoints+=1
		if scr.getch()==ord('q'):
			curses.endwin()
			exit()
	elif lastKey==ord('q'):
		curses.endwin()
		exit()
