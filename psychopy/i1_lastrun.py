#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.3),
    on 四月 08, 2026, at 09:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware, parallel
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
from psychopy import visual, core
import pandas as pd
import string

file_path = 'text2.xlsx'  # 文件路径

# 读取Excel文件
df = pd.read_excel(file_path)

# 获取所有句子
all_sentences = df['句子'].astype(str).tolist()

# 初始化全局索引，跟踪当前的句子
current_sentence_index = 0
# Run 'Before Experiment' code from code_3


# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.3'
expName = 'untitled'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\zihanzhang\\image_2\\i1_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    # create speaker 'sound_1'
    deviceManager.addDevice(
        deviceName='sound_1',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instruction" ---
    text = visual.TextStim(win=win, name='text',
        text='阅读并记住每句话，\n完成记忆后开始回想刚才的话，\n期间尽量减少肢体运动，\n减少思绪游移，\n按下回车键开始实验',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "trials_1" ---
    p_port_6 = parallel.ParallelPort(address='0x0378')
    # Run 'Begin Experiment' code from code
    # Split the text into characters - Note: this now happens per trial, not here globally
    # Therefore, we won't split any text into characters at this point.
    
    # Initialize global variables that will be used across multiple trials
    char_stims = []  # This will be used to hold character TextStim objects for the current sentence
    chars = []  # This will store the list of characters for the current sentence
    
    # Set initial position and spacing for the characters on the screen
    start_x = -0.9  # Adjust based on text length
    spacing = 0.05  # Adjust spacing as needed
    text_8 = visual.TextStim(win=win, name='text_8',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "recall_1" ---
    p_port = parallel.ParallelPort(address='0x0378')
    # Run 'Begin Experiment' code from code_2
    # Split the text into characters - Note: this now happens per trial, not here globally
    # Therefore, we won't split any text into characters at this point.
    
    # Initialize global variables that will be used across multiple trials
    char_stims = []  # This will be used to hold character TextStim objects for the current sentence
    chars = []  # This will store the list of characters for the current sentence
    
    # Set initial position and spacing for the characters on the screen
    start_x = -0.9  # Adjust based on text length
    spacing = 0.05  # Adjust spacing as needed
    text_6 = visual.TextStim(win=win, name='text_6',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "blank" ---
    p_port_4 = parallel.ParallelPort(address='0x0378')
    text_5 = visual.TextStim(win=win, name='text_5',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "rest_intro" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text='请调整自己的精神，\n接下来是10分钟的静息状态，\n尽量保持情绪平稳的冥想状态，\n可以闭眼或睁眼地放松，\n身体保持静止',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "rest" ---
    p_port_3 = parallel.ParallelPort(address='0x0378')
    text_9 = visual.TextStim(win=win, name='text_9',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "sound_intro" ---
    p_port_5 = parallel.ParallelPort(address='0x0378')
    sound_1 = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker='sound_1',    name='sound_1'
    )
    sound_1.setVolume(1.0)
    text_11 = visual.TextStim(win=win, name='text_11',
        text='好了，冥想结束，\n接下来是下一组实验',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "wait" ---
    text_10 = visual.TextStim(win=win, name='text_10',
        text='阅读并记住每句话，\n完成记忆后开始回想刚才的话，\n期间尽量减少肢体运动，减少思绪游移\n如果你准备好了，按下回车键继续实验',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "trials_2" ---
    p_port_7 = parallel.ParallelPort(address='0x0378')
    # Run 'Begin Experiment' code from code_3
    # Split the text into characters - Note: this now happens per trial, not here globally
    # Therefore, we won't split any text into characters at this point.
    
    # Initialize global variables that will be used across multiple trials
    char_stims = []  # This will be used to hold character TextStim objects for the current sentence
    chars = []  # This will store the list of characters for the current sentence
    
    # Set initial position and spacing for the characters on the screen
    start_x = -0.9  # Adjust based on text length
    spacing = 0.05  # Adjust spacing as needed
    
    text_3 = visual.TextStim(win=win, name='text_3',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "recall_2" ---
    p_port_2 = parallel.ParallelPort(address='0x0378')
    # Run 'Begin Experiment' code from code_4
    # Split the text into characters - Note: this now happens per trial, not here globally
    # Therefore, we won't split any text into characters at this point.
    
    # Initialize global variables that will be used across multiple trials
    char_stims = []  # This will be used to hold character TextStim objects for the current sentence
    chars = []  # This will store the list of characters for the current sentence
    
    # Set initial position and spacing for the characters on the screen
    start_x = -0.9  # Adjust based on text length
    spacing = 0.05  # Adjust spacing as needed
    
    text_4 = visual.TextStim(win=win, name='text_4',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "blank" ---
    p_port_4 = parallel.ParallelPort(address='0x0378')
    text_5 = visual.TextStim(win=win, name='text_5',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "end" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='实验结束\n按0键退出',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instruction" ---
    # create an object to store info about Routine instruction
    instruction = data.Routine(
        name='instruction',
        components=[text, key_resp_2],
    )
    instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for instruction
    instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction.tStart = globalClock.getTime(format='float')
    instruction.status = STARTED
    thisExp.addData('instruction.started', instruction.tStart)
    instruction.maxDuration = None
    # keep track of which components have finished
    instructionComponents = instruction.components
    for thisComponent in instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=True)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction
    instruction.tStop = globalClock.getTime(format='float')
    instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction.stopped', instruction.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_1 = data.TrialHandler2(
        name='loop_1',
        nReps=126.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(loop_1)  # add the loop to the experiment
    thisLoop_1 = loop_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_1.rgb)
    if thisLoop_1 != None:
        for paramName in thisLoop_1:
            globals()[paramName] = thisLoop_1[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_1 in loop_1:
        currentLoop = loop_1
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_1.rgb)
        if thisLoop_1 != None:
            for paramName in thisLoop_1:
                globals()[paramName] = thisLoop_1[paramName]
        
        # --- Prepare to start Routine "trials_1" ---
        # create an object to store info about Routine trials_1
        trials_1 = data.Routine(
            name='trials_1',
            components=[p_port_6, text_8],
        )
        trials_1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        # 使用 global 关键字声明 current_sentence_index
        global current_sentence_index
        
        # 检查是否还有句子可以显示
        if current_sentence_index < len(all_sentences):
            current_sentence = all_sentences[current_sentence_index]
            chars = list(current_sentence)
            char_stims = []
            spacing = min(0.07, 1.8 / len(chars))  # 确保文本不会超出屏幕宽度
            total_text_length = len(chars) * spacing  # 总的文本长度
        
            # 计算起始位置，使得文本在屏幕正中央
            start_x = -total_text_length / 2 + 0.04 # 根据字符总长度将起始位置左移一半
        
            # 创建每个字符的 TextStim 对象
            for i, char in enumerate(chars):
                stim = visual.TextStim(
                    win=win,
                    text=char,
                    font='SimSun',
                    pos=(start_x + i * spacing, 0),  # 水平位置根据起始位置和字符间距计算
                    height=0.08,  # 字符的高度，可以根据屏幕大小调整
                    color='white'
                )
                char_stims.append(stim)
            
            # 初始化字符计时器和索引
            char_timer = core.Clock()
            char_timer.reset()
            current_char_index = 0
        else:
            # 没有更多句子可用，结束实验
            core.quit()
        # store start times for trials_1
        trials_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trials_1.tStart = globalClock.getTime(format='float')
        trials_1.status = STARTED
        thisExp.addData('trials_1.started', trials_1.tStart)
        trials_1.maxDuration = 10
        # keep track of which components have finished
        trials_1Components = trials_1.components
        for thisComponent in trials_1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trials_1" ---
        # if trial has changed, end Routine now
        if isinstance(loop_1, data.TrialHandler2) and thisLoop_1.thisN != loop_1.thisTrial.thisN:
            continueRoutine = False
        trials_1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > trials_1.maxDuration-frameTolerance:
                trials_1.maxDurationReached = True
                continueRoutine = False
            # *p_port_6* updates
            
            # if p_port_6 is starting this frame...
            if p_port_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_6.frameNStart = frameN  # exact frame index
                p_port_6.tStart = t  # local t and not account for scr refresh
                p_port_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_6.started', t)
                # update status
                p_port_6.status = STARTED
                p_port_6.status = STARTED
                win.callOnFlip(p_port_6.setData, int(50))
            
            # if p_port_6 is stopping this frame...
            if p_port_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_6.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_6.tStop = t  # not accounting for scr refresh
                    p_port_6.tStopRefresh = tThisFlipGlobal  # on global time
                    p_port_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_6.stopped', t)
                    # update status
                    p_port_6.status = FINISHED
                    win.callOnFlip(p_port_6.setData, int(0))
            # Run 'Each Frame' code from code
            # 使用 string.punctuation 定义所有的标点符号，也可以根据需要自己定义特殊的标点符号集
            punctuation = string.punctuation + "，。？！：；、“”‘’"  # 包含常见中文标点符号
            
            # 确保 Routine 继续运行
            continueRoutine = True
            
            # 设置每个字符高亮显示的持续时间（秒）
            char_duration = 0.4
            
            # 检查是否需要更新高亮的字符
            if char_timer.getTime() >= char_duration:
                char_timer.reset()
                current_char_index += 1
            
                # 跳过标点符号
                while current_char_index < len(chars) and chars[current_char_index] in punctuation:
                    current_char_index += 1
            
            # 绘制字符
            if current_char_index < len(chars):
                for i, stim in enumerate(char_stims):
                    if i == current_char_index:
                        # 当前字符高亮显示（例如，红色）
                        stim.color = 'red'
                    else:
                        stim.color = 'white'
                    stim.draw()
            else:
                # 所有字符已显示完毕，结束 Routine
                continueRoutine = False
            
            # *text_8* updates
            
            # if text_8 is starting this frame...
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.started')
                # update status
                text_8.status = STARTED
                text_8.setAutoDraw(True)
            
            # if text_8 is active this frame...
            if text_8.status == STARTED:
                # update params
                pass
            
            # if text_8 is stopping this frame...
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.tStopRefresh = tThisFlipGlobal  # on global time
                    text_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_8.stopped')
                    # update status
                    text_8.status = FINISHED
                    text_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trials_1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trials_1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trials_1" ---
        for thisComponent in trials_1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trials_1
        trials_1.tStop = globalClock.getTime(format='float')
        trials_1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trials_1.stopped', trials_1.tStop)
        if p_port_6.status == STARTED:
            win.callOnFlip(p_port_6.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if trials_1.maxDurationReached:
            routineTimer.addTime(-trials_1.maxDuration)
        elif trials_1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "recall_1" ---
        # create an object to store info about Routine recall_1
        recall_1 = data.Routine(
            name='recall_1',
            components=[p_port, text_6],
        )
        recall_1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        # 检查是否还有句子可以显示
        if current_sentence_index < len(all_sentences):
            current_sentence = all_sentences[current_sentence_index]
            chars = list(current_sentence)
            chars.append('1')
        
            char_stims = []
            spacing = min(0.07, 1.8 / len(chars))  # 确保文本不会超出屏幕宽度
            total_text_length = len(chars) * spacing  # 总的文本长度
        
            # 计算起始位置，使得文本在屏幕正中央
            start_x = -total_text_length / 2 + 0.04 # 根据字符总长度将起始位置左移一半
        
            # 创建每个字符的 TextStim 对象
            for i, char in enumerate(chars):
                stim = visual.TextStim(
                    win=win,
                    text='',
                    font='SimSun',
                    pos=(start_x + i * spacing, 0),  # 水平位置根据起始位置和字符间距计算
                    height=0.08,  # 字符的高度，可以根据屏幕大小调整
                    color='white'
                )
                char_stims.append(stim)
            
            # 初始化字符计时器和索引
            char_timer = core.Clock()
            char_timer.reset()
            current_char_index = 0
        else:
            # 没有更多句子可用，结束实验
            core.quit()
        # store start times for recall_1
        recall_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        recall_1.tStart = globalClock.getTime(format='float')
        recall_1.status = STARTED
        thisExp.addData('recall_1.started', recall_1.tStart)
        recall_1.maxDuration = 10
        # keep track of which components have finished
        recall_1Components = recall_1.components
        for thisComponent in recall_1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "recall_1" ---
        # if trial has changed, end Routine now
        if isinstance(loop_1, data.TrialHandler2) and thisLoop_1.thisN != loop_1.thisTrial.thisN:
            continueRoutine = False
        recall_1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > recall_1.maxDuration-frameTolerance:
                recall_1.maxDurationReached = True
                continueRoutine = False
            # *p_port* updates
            
            # if p_port is starting this frame...
            if p_port.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port.frameNStart = frameN  # exact frame index
                p_port.tStart = t  # local t and not account for scr refresh
                p_port.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port.started', t)
                # update status
                p_port.status = STARTED
                p_port.status = STARTED
                win.callOnFlip(p_port.setData, int(100))
            
            # if p_port is stopping this frame...
            if p_port.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port.tStop = t  # not accounting for scr refresh
                    p_port.tStopRefresh = tThisFlipGlobal  # on global time
                    p_port.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port.stopped', t)
                    # update status
                    p_port.status = FINISHED
                    win.callOnFlip(p_port.setData, int(0))
            # Run 'Each Frame' code from code_2
            # 使用 string.punctuation 定义所有的标点符号，也可以根据需要自己定义特殊的标点符号集
            punctuation = string.punctuation + "，。？！：；、“”‘’"  # 包含常见中文标点符号
            
            # 确保 Routine 继续运行
            continueRoutine = True
            
            # 设置每个字符高亮显示的持续时间（秒）
            char_duration = 0.4
            
            # 检查是否需要更新高亮的字符
            if char_timer.getTime() >= char_duration:
                char_timer.reset()
                current_char_index += 1
            
                # 跳过标点符号
                while current_char_index < len(chars) and chars[current_char_index] in punctuation:
                    current_char_index += 1
            
            # 绘制字符
            if current_char_index < len(chars):
                for i, stim in enumerate(char_stims):
                    if i == current_char_index:
                        # 当前字符高亮显示（例如，红色）
                        stim.color = 'red'
                    else:
                        stim.color = 'white'
                    stim.draw()
            else:
                # 所有字符已显示完毕，结束 Routine
                continueRoutine = False
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            
            # if text_6 is stopping this frame...
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.tStopRefresh = tThisFlipGlobal  # on global time
                    text_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.stopped')
                    # update status
                    text_6.status = FINISHED
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                recall_1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recall_1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recall_1" ---
        for thisComponent in recall_1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for recall_1
        recall_1.tStop = globalClock.getTime(format='float')
        recall_1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('recall_1.stopped', recall_1.tStop)
        if p_port.status == STARTED:
            win.callOnFlip(p_port.setData, int(0))
        # Run 'End Routine' code from code_2
        current_sentence_index += 1
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if recall_1.maxDurationReached:
            routineTimer.addTime(-recall_1.maxDuration)
        elif recall_1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[p_port_4, text_5],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = 1.8
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        # if trial has changed, end Routine now
        if isinstance(loop_1, data.TrialHandler2) and thisLoop_1.thisN != loop_1.thisTrial.thisN:
            continueRoutine = False
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > blank.maxDuration-frameTolerance:
                blank.maxDurationReached = True
                continueRoutine = False
            # *p_port_4* updates
            
            # if p_port_4 is starting this frame...
            if p_port_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_4.frameNStart = frameN  # exact frame index
                p_port_4.tStart = t  # local t and not account for scr refresh
                p_port_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_4.started', t)
                # update status
                p_port_4.status = STARTED
                p_port_4.status = STARTED
                win.callOnFlip(p_port_4.setData, int(101))
            
            # if p_port_4 is stopping this frame...
            if p_port_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_4.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_4.tStop = t  # not accounting for scr refresh
                    p_port_4.tStopRefresh = tThisFlipGlobal  # on global time
                    p_port_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_4.stopped', t)
                    # update status
                    p_port_4.status = FINISHED
                    win.callOnFlip(p_port_4.setData, int(0))
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # if text_5 is stopping this frame...
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.tStopRefresh = tThisFlipGlobal  # on global time
                    text_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_5.stopped')
                    # update status
                    text_5.status = FINISHED
                    text_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        if p_port_4.status == STARTED:
            win.callOnFlip(p_port_4.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.800000)
        thisExp.nextEntry()
        
    # completed 126.0 repeats of 'loop_1'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "rest_intro" ---
    # create an object to store info about Routine rest_intro
    rest_intro = data.Routine(
        name='rest_intro',
        components=[text_7],
    )
    rest_intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for rest_intro
    rest_intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    rest_intro.tStart = globalClock.getTime(format='float')
    rest_intro.status = STARTED
    thisExp.addData('rest_intro.started', rest_intro.tStart)
    rest_intro.maxDuration = 3
    # keep track of which components have finished
    rest_introComponents = rest_intro.components
    for thisComponent in rest_intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest_intro" ---
    rest_intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > rest_intro.maxDuration-frameTolerance:
            rest_intro.maxDurationReached = True
            continueRoutine = False
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # if text_7 is stopping this frame...
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.tStopRefresh = tThisFlipGlobal  # on global time
                text_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.stopped')
                # update status
                text_7.status = FINISHED
                text_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            rest_intro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rest_intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest_intro" ---
    for thisComponent in rest_intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for rest_intro
    rest_intro.tStop = globalClock.getTime(format='float')
    rest_intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('rest_intro.stopped', rest_intro.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if rest_intro.maxDurationReached:
        routineTimer.addTime(-rest_intro.maxDuration)
    elif rest_intro.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "rest" ---
    # create an object to store info about Routine rest
    rest = data.Routine(
        name='rest',
        components=[p_port_3, text_9],
    )
    rest.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for rest
    rest.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    rest.tStart = globalClock.getTime(format='float')
    rest.status = STARTED
    thisExp.addData('rest.started', rest.tStart)
    rest.maxDuration = 600
    # keep track of which components have finished
    restComponents = rest.components
    for thisComponent in rest.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest" ---
    rest.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > rest.maxDuration-frameTolerance:
            rest.maxDurationReached = True
            continueRoutine = False
        # *p_port_3* updates
        
        # if p_port_3 is starting this frame...
        if p_port_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_3.frameNStart = frameN  # exact frame index
            p_port_3.tStart = t  # local t and not account for scr refresh
            p_port_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_3.started', t)
            # update status
            p_port_3.status = STARTED
            p_port_3.status = STARTED
            win.callOnFlip(p_port_3.setData, int(200))
        
        # if p_port_3 is stopping this frame...
        if p_port_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_3.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_3.tStop = t  # not accounting for scr refresh
                p_port_3.tStopRefresh = tThisFlipGlobal  # on global time
                p_port_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_3.stopped', t)
                # update status
                p_port_3.status = FINISHED
                win.callOnFlip(p_port_3.setData, int(0))
        
        # *text_9* updates
        
        # if text_9 is starting this frame...
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_9.started')
            # update status
            text_9.status = STARTED
            text_9.setAutoDraw(True)
        
        # if text_9 is active this frame...
        if text_9.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            rest.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rest.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in rest.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for rest
    rest.tStop = globalClock.getTime(format='float')
    rest.tStopRefresh = tThisFlipGlobal
    thisExp.addData('rest.stopped', rest.tStop)
    if p_port_3.status == STARTED:
        win.callOnFlip(p_port_3.setData, int(0))
    thisExp.nextEntry()
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "sound_intro" ---
    # create an object to store info about Routine sound_intro
    sound_intro = data.Routine(
        name='sound_intro',
        components=[p_port_5, sound_1, text_11],
    )
    sound_intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    sound_1.setSound('1.wav', hamming=True)
    sound_1.setVolume(1.0, log=False)
    sound_1.seek(0)
    # store start times for sound_intro
    sound_intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    sound_intro.tStart = globalClock.getTime(format='float')
    sound_intro.status = STARTED
    thisExp.addData('sound_intro.started', sound_intro.tStart)
    sound_intro.maxDuration = 10
    # keep track of which components have finished
    sound_introComponents = sound_intro.components
    for thisComponent in sound_intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sound_intro" ---
    sound_intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > sound_intro.maxDuration-frameTolerance:
            sound_intro.maxDurationReached = True
            continueRoutine = False
        # *p_port_5* updates
        
        # if p_port_5 is starting this frame...
        if p_port_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_port_5.frameNStart = frameN  # exact frame index
            p_port_5.tStart = t  # local t and not account for scr refresh
            p_port_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('p_port_5.started', t)
            # update status
            p_port_5.status = STARTED
            p_port_5.status = STARTED
            win.callOnFlip(p_port_5.setData, int(201))
        
        # if p_port_5 is stopping this frame...
        if p_port_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > p_port_5.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                p_port_5.tStop = t  # not accounting for scr refresh
                p_port_5.tStopRefresh = tThisFlipGlobal  # on global time
                p_port_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('p_port_5.stopped', t)
                # update status
                p_port_5.status = FINISHED
                win.callOnFlip(p_port_5.setData, int(0))
        
        # *sound_1* updates
        
        # if sound_1 is starting this frame...
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            # update status
            sound_1.status = STARTED
            sound_1.play(when=win)  # sync with win flip
        
        # if sound_1 is stopping this frame...
        if sound_1.status == STARTED:
            if bool(False) or sound_1.isFinished:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.tStopRefresh = tThisFlipGlobal  # on global time
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                # update status
                sound_1.status = FINISHED
                sound_1.stop()
        
        # *text_11* updates
        
        # if text_11 is starting this frame...
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_11.started')
            # update status
            text_11.status = STARTED
            text_11.setAutoDraw(True)
        
        # if text_11 is active this frame...
        if text_11.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[sound_1]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            sound_intro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sound_intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sound_intro" ---
    for thisComponent in sound_intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for sound_intro
    sound_intro.tStop = globalClock.getTime(format='float')
    sound_intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('sound_intro.stopped', sound_intro.tStop)
    if p_port_5.status == STARTED:
        win.callOnFlip(p_port_5.setData, int(0))
    sound_1.pause()  # ensure sound has stopped at end of Routine
    thisExp.nextEntry()
    # the Routine "sound_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "wait" ---
    # create an object to store info about Routine wait
    wait = data.Routine(
        name='wait',
        components=[text_10, key_resp],
    )
    wait.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for wait
    wait.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    wait.tStart = globalClock.getTime(format='float')
    wait.status = STARTED
    thisExp.addData('wait.started', wait.tStart)
    wait.maxDuration = None
    # keep track of which components have finished
    waitComponents = wait.components
    for thisComponent in wait.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wait" ---
    wait.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        
        # if text_10 is starting this frame...
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_10.started')
            # update status
            text_10.status = STARTED
            text_10.setAutoDraw(True)
        
        # if text_10 is active this frame...
        if text_10.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            wait.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wait.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wait" ---
    for thisComponent in wait.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for wait
    wait.tStop = globalClock.getTime(format='float')
    wait.tStopRefresh = tThisFlipGlobal
    thisExp.addData('wait.stopped', wait.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "wait" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop_2 = data.TrialHandler2(
        name='loop_2',
        nReps=126.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(loop_2)  # add the loop to the experiment
    thisLoop_2 = loop_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_2.rgb)
    if thisLoop_2 != None:
        for paramName in thisLoop_2:
            globals()[paramName] = thisLoop_2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop_2 in loop_2:
        currentLoop = loop_2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_2.rgb)
        if thisLoop_2 != None:
            for paramName in thisLoop_2:
                globals()[paramName] = thisLoop_2[paramName]
        
        # --- Prepare to start Routine "trials_2" ---
        # create an object to store info about Routine trials_2
        trials_2 = data.Routine(
            name='trials_2',
            components=[p_port_7, text_3],
        )
        trials_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        # 检查是否还有句子可以显示
        if current_sentence_index < len(all_sentences):
            current_sentence = all_sentences[current_sentence_index]
            chars = list(current_sentence)
            char_stims = []
            spacing = min(0.07, 1.8 / len(chars))  # 确保文本不会超出屏幕宽度
            total_text_length = len(chars) * spacing  # 总的文本长度
        
            # 计算起始位置，使得文本在屏幕正中央
            start_x = -total_text_length / 2 + 0.04 # 根据字符总长度将起始位置左移一半
        
            # 创建每个字符的 TextStim 对象
            for i, char in enumerate(chars):
                stim = visual.TextStim(
                    win=win,
                    text=char,
                    font='SimSun',
                    pos=(start_x + i * spacing, 0),  # 水平位置根据起始位置和字符间距计算
                    height=0.08,  # 字符的高度，可以根据屏幕大小调整
                    color='white'
                )
                char_stims.append(stim)
            
            # 初始化字符计时器和索引
            char_timer = core.Clock()
            char_timer.reset()
            current_char_index = 0
        else:
            # 没有更多句子可用，结束实验
            core.quit()
        # store start times for trials_2
        trials_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trials_2.tStart = globalClock.getTime(format='float')
        trials_2.status = STARTED
        thisExp.addData('trials_2.started', trials_2.tStart)
        trials_2.maxDuration = 10
        # keep track of which components have finished
        trials_2Components = trials_2.components
        for thisComponent in trials_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trials_2" ---
        # if trial has changed, end Routine now
        if isinstance(loop_2, data.TrialHandler2) and thisLoop_2.thisN != loop_2.thisTrial.thisN:
            continueRoutine = False
        trials_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > trials_2.maxDuration-frameTolerance:
                trials_2.maxDurationReached = True
                continueRoutine = False
            # *p_port_7* updates
            
            # if p_port_7 is starting this frame...
            if p_port_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_7.frameNStart = frameN  # exact frame index
                p_port_7.tStart = t  # local t and not account for scr refresh
                p_port_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_7.started', t)
                # update status
                p_port_7.status = STARTED
                p_port_7.status = STARTED
                win.callOnFlip(p_port_7.setData, int(50))
            
            # if p_port_7 is stopping this frame...
            if p_port_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_7.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_7.tStop = t  # not accounting for scr refresh
                    p_port_7.tStopRefresh = tThisFlipGlobal  # on global time
                    p_port_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_7.stopped', t)
                    # update status
                    p_port_7.status = FINISHED
                    win.callOnFlip(p_port_7.setData, int(0))
            # Run 'Each Frame' code from code_3
            # 使用 string.punctuation 定义所有的标点符号，也可以根据需要自己定义特殊的标点符号集
            punctuation = string.punctuation + "，。？！：；、“”‘’"  # 包含常见中文标点符号
            
            # 确保 Routine 继续运行
            continueRoutine = True
            
            # 设置每个字符高亮显示的持续时间（秒）
            char_duration = 0.4
            
            # 检查是否需要更新高亮的字符
            if char_timer.getTime() >= char_duration:
                char_timer.reset()
                current_char_index += 1
            
                # 跳过标点符号
                while current_char_index < len(chars) and chars[current_char_index] in punctuation:
                    current_char_index += 1
            
            # 绘制字符
            if current_char_index < len(chars):
                for i, stim in enumerate(char_stims):
                    if i == current_char_index:
                        # 当前字符高亮显示（例如，红色）
                        stim.color = 'red'
                    else:
                        stim.color = 'white'
                    stim.draw()
            else:
                # 所有字符已显示完毕，结束 Routine
                continueRoutine = False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # if text_3 is stopping this frame...
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    # update status
                    text_3.status = FINISHED
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trials_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trials_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trials_2" ---
        for thisComponent in trials_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trials_2
        trials_2.tStop = globalClock.getTime(format='float')
        trials_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trials_2.stopped', trials_2.tStop)
        if p_port_7.status == STARTED:
            win.callOnFlip(p_port_7.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if trials_2.maxDurationReached:
            routineTimer.addTime(-trials_2.maxDuration)
        elif trials_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "recall_2" ---
        # create an object to store info about Routine recall_2
        recall_2 = data.Routine(
            name='recall_2',
            components=[p_port_2, text_4],
        )
        recall_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        # 检查是否还有句子可以显示
        if current_sentence_index < len(all_sentences):
            current_sentence = all_sentences[current_sentence_index]
            chars = list(current_sentence)
            chars.append('1')
        
            char_stims = []
            spacing = min(0.07, 1.8 / len(chars))  # 确保文本不会超出屏幕宽度
            total_text_length = len(chars) * spacing  # 总的文本长度
        
            # 计算起始位置，使得文本在屏幕正中央
            start_x = -total_text_length / 2 + 0.04 # 根据字符总长度将起始位置左移一半
        
            # 创建每个字符的 TextStim 对象
            for i, char in enumerate(chars):
                stim = visual.TextStim(
                    win=win,
                    text='',
                    font='SimSun',
                    pos=(start_x + i * spacing, 0),  # 水平位置根据起始位置和字符间距计算
                    height=0.08,  # 字符的高度，可以根据屏幕大小调整
                    color='white'
                )
                char_stims.append(stim)
            
            # 初始化字符计时器和索引
            char_timer = core.Clock()
            char_timer.reset()
            current_char_index = 0
        else:
            # 没有更多句子可用，结束实验
            core.quit()
        # store start times for recall_2
        recall_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        recall_2.tStart = globalClock.getTime(format='float')
        recall_2.status = STARTED
        thisExp.addData('recall_2.started', recall_2.tStart)
        recall_2.maxDuration = 10
        # keep track of which components have finished
        recall_2Components = recall_2.components
        for thisComponent in recall_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "recall_2" ---
        # if trial has changed, end Routine now
        if isinstance(loop_2, data.TrialHandler2) and thisLoop_2.thisN != loop_2.thisTrial.thisN:
            continueRoutine = False
        recall_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > recall_2.maxDuration-frameTolerance:
                recall_2.maxDurationReached = True
                continueRoutine = False
            # *p_port_2* updates
            
            # if p_port_2 is starting this frame...
            if p_port_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_2.frameNStart = frameN  # exact frame index
                p_port_2.tStart = t  # local t and not account for scr refresh
                p_port_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_2.started', t)
                # update status
                p_port_2.status = STARTED
                p_port_2.status = STARTED
                win.callOnFlip(p_port_2.setData, int(100))
            
            # if p_port_2 is stopping this frame...
            if p_port_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_2.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_2.tStop = t  # not accounting for scr refresh
                    p_port_2.tStopRefresh = tThisFlipGlobal  # on global time
                    p_port_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_2.stopped', t)
                    # update status
                    p_port_2.status = FINISHED
                    win.callOnFlip(p_port_2.setData, int(0))
            # Run 'Each Frame' code from code_4
            # 使用 string.punctuation 定义所有的标点符号，也可以根据需要自己定义特殊的标点符号集
            punctuation = string.punctuation + "，。？！：；、“”‘’"  # 包含常见中文标点符号
            
            # 确保 Routine 继续运行
            continueRoutine = True
            
            # 设置每个字符高亮显示的持续时间（秒）
            char_duration = 0.4
            
            # 检查是否需要更新高亮的字符
            if char_timer.getTime() >= char_duration:
                char_timer.reset()
                current_char_index += 1
            
                # 跳过标点符号
                while current_char_index < len(chars) and chars[current_char_index] in punctuation:
                    current_char_index += 1
            
            # 绘制字符
            if current_char_index < len(chars):
                for i, stim in enumerate(char_stims):
                    if i == current_char_index:
                        # 当前字符高亮显示（例如，红色）
                        stim.color = 'red'
                    else:
                        stim.color = 'white'
                    stim.draw()
            else:
                # 所有字符已显示完毕，结束 Routine
                continueRoutine = False
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.started')
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # if text_4 is stopping this frame...
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.tStopRefresh = tThisFlipGlobal  # on global time
                    text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.stopped')
                    # update status
                    text_4.status = FINISHED
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                recall_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recall_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recall_2" ---
        for thisComponent in recall_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for recall_2
        recall_2.tStop = globalClock.getTime(format='float')
        recall_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('recall_2.stopped', recall_2.tStop)
        if p_port_2.status == STARTED:
            win.callOnFlip(p_port_2.setData, int(0))
        # Run 'End Routine' code from code_4
        current_sentence_index += 1
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if recall_2.maxDurationReached:
            routineTimer.addTime(-recall_2.maxDuration)
        elif recall_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[p_port_4, text_5],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = 1.8
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        # if trial has changed, end Routine now
        if isinstance(loop_2, data.TrialHandler2) and thisLoop_2.thisN != loop_2.thisTrial.thisN:
            continueRoutine = False
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.8:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > blank.maxDuration-frameTolerance:
                blank.maxDurationReached = True
                continueRoutine = False
            # *p_port_4* updates
            
            # if p_port_4 is starting this frame...
            if p_port_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port_4.frameNStart = frameN  # exact frame index
                p_port_4.tStart = t  # local t and not account for scr refresh
                p_port_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port_4.started', t)
                # update status
                p_port_4.status = STARTED
                p_port_4.status = STARTED
                win.callOnFlip(p_port_4.setData, int(101))
            
            # if p_port_4 is stopping this frame...
            if p_port_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port_4.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port_4.tStop = t  # not accounting for scr refresh
                    p_port_4.tStopRefresh = tThisFlipGlobal  # on global time
                    p_port_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port_4.stopped', t)
                    # update status
                    p_port_4.status = FINISHED
                    win.callOnFlip(p_port_4.setData, int(0))
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # if text_5 is stopping this frame...
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.tStopRefresh = tThisFlipGlobal  # on global time
                    text_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_5.stopped')
                    # update status
                    text_5.status = FINISHED
                    text_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        if p_port_4.status == STARTED:
            win.callOnFlip(p_port_4.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.800000)
        thisExp.nextEntry()
        
    # completed 126.0 repeats of 'loop_2'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[text_2, key_resp_3],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['num_0'], ignoreKeys=["escape"], waitRelease=True)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
