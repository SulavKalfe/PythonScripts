@echo off

REM sp= speaker
doskey sp=start /b blnc.py s ^& exit

REM ep= earphone
doskey ep=start /b blnc.py e ^& exit

REM fs= full sound
doskey fs=start /b sound.py 100 ^& exit

REM ms= mute sound
doskey ms=start /b sound.py 0 ^& exit

REM rs= regular sound
doskey rs=start /b sound.py 60 ^& exit

REM cs= change sound
doskey cs=start /b sound.py $* ^& exit

doskey e=start /b exit ^& exit

REM fb= full brightness
doskey fb=start /b brightness.py 100 ^& exit

REM rb= regular brightness
doskey rb=start /b brightness.py 35 ^& exit

REM cb= change brightness
doskey cb=start /b brightness.py $* ^& exit

REM yt= youtube
doskey yt=start /b websites.py 0 ^& exit

REM rt= reddit
doskey rt=start /b websites.py 1 ^& exit

REM ttv= twitch ttv
doskey ttv=start /b websites.py 2 ^& exit

REM gpt= chatgpt
doskey gpt=start /b websites.py 3 ^& exit

REM ha= hianime
doskey ha=start /b websites.py 4 ^& exit

REM sc= snapchat
doskey sc=start /b websites.py 5 ^& exit

REM gh= github
doskey gh=start /b websites.py 6 ^& exit

REM es= epic store
doskey es=start /b websites.py 10 ^& exit

REM fg= fitgirl
doskey fg=start /b privatetabsites.py 7 ^& exit

REM st= streamed
doskey st=start /b privatetabsites.py 8 ^& exit

REM fmhy= free media heck yeah
doskey fmhy=start /b privatetabsites.py 9 ^& exit

REM sw=search website
doskey sw=start /b searchsite.py ^& exit

REM spw= search website in private window
doskey spw=start /b searchsiteinprivate.py ^& exit

REM ddg= duckduckgo
doskey ddg=start /b searchinddg.py ^& exit

REM gle= google
doskey gle=start /b searchingoogle.py ^& exit

REM pddg= private ddg
doskey pddg=start /b searchinprivateddg.py ^& exit

REM tt= translate text
doskey tt=start /b translatetext.py ^& exit

REM ti= translate image
doskey ti=start /b translateimage.py ^& exit

REM ca= coding apps
doskey ca=start /b opencodingapp.py3 ^& exit

REM av= add variable
doskey av=start /b replaceslash.py ^& exit

REM cwa= continue watching anime
doskey cwa=start /b continuewatching.py 0 ^& exit

REM cws= continue watching series
doskey cws=start /b continuewatching.py 1 ^& exit

REM rwa= replace watched anime
doskey rwa=start /b replacewatching.py 0 ^& exit

REM rws= replace watched series
doskey rws=start /b replacewatching.py 1 ^& exit

REM ris= reverse image search
doskey ris=start /b reverseimagesearch.py ^& exit

REM cdp= create django project
doskey cdp= createdjangoproject.py