"""
This module was generated by Vizconnect.
Version: 1.05
Generated on: 2014-06-10 13:06:34.205000
"""

import viz
import vizconnect

#################################
# Parent configuration, if any
#################################

def getParentConfiguration():
	#VC: set the parent configuration
	_parent = ''
	
	#VC: return the parent configuration
	return _parent


#################################
# Pre viz.go() Code
#################################

def preVizGo():
	return True


#################################
# Pre-initialization Code
#################################

def preInit():
	"""Add any code here which should be called after viz.go but before any initializations happen.
	Returned values can be obtained by calling getPreInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Group Code
#################################

def initGroups(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawGroup = vizconnect.getRawGroupDict()

	#VC: initialize a new group
	_name = 'origin_node_auto_calibration_cave'
	if vizconnect.isPendingInit('group', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			rawGroup[_name] = viz.addGroup()
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addGroup(rawGroup[_name], _name, make='Virtual', model='Origin')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getGroup(_name).setParent(vizconnect.getTransport('walking'))

	#VC: return values can be modified here
	return None


#################################
# Display Code
#################################

def initDisplays(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawDisplay = vizconnect.getRawDisplayDict()

	#VC: initialize a new display
	_name = 'auto_calibration_cave'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init which needs to happen before viz.go
		if initFlag&vizconnect.INIT_PREVIZGO:
			viz.setOption('viz.stereo', viz.QUAD_BUFFER)
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.MainWindow
			
			#VC: set some parameters
			calibrationFilename = 'C:/Christie/EGG Config Files/EggFinal.cal'
			mappingFilename = 'C:/Christie/EGG Config Files/channel_to_computer_mapping.csv'
			modelFilename = 'C:/Christie/EGG Config Files/vs12004_screen surface_nov10.wrl'
			usingStereo = True
			stereo = viz.QUAD_BUFFER

			projectionRenderScene = 2
			
			#VC: create the raw object
			from vizconnect.util.display.christie_autocal import auto_cal_parser
			import custom_projector_configuration
			from vizconnect.util.display.christie_autocal import projector_manager
			viewpoint = viz.addGroup()
			
			# get an origin node
			originName = 'origin_node_'+_name
			initGroups(vizconnect.INIT_INDEPENDENT, [originName])# ensure it's been created
			originNode = vizconnect.getGroup(originName).getNode3d()
			
			dome = custom_projector_configuration.ProjectorConfiguration(originNode)
			dome.setViewpoint(viewpoint)
			
			_window.originNode = dome.getOrigin()
			_window.displayNode = dome
			_window.viewpointNode = viewpoint
			
			dome.parseFile(	calibrationFilename,
							mappingFilename,
							usingStereo=usingStereo,
							stereoMode=stereo,
							scene=projectionRenderScene)
			
			dome.start()
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Christie', model='Auto Calibration Cave')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getTracker('ppt_subitem1'))

	#VC: set the name of the default
	vizconnect.setDefault('display', 'auto_calibration_cave')

	#VC: return values can be modified here
	return None


#################################
# Tracker Code
#################################

def initTrackers(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTracker = vizconnect.getRawTrackerDict()

	#VC: initialize a new tracker
	_name = 'ppt_subitem1'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			pptHostname = 'localhost'
			markerId = 1
			
			#VC: create the raw object
			vrpn7 = viz.add('vrpn7.dle')
			rawTracker[_name] = vrpn7.addTracker('PPT0@'+pptHostname, markerId-1)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='WorldViz', model='PPT')
	
		#VC: init the offsets
		if initFlag&vizconnect.INIT_OFFSETS:
			_link = vizconnect.getTracker(_name).getLink()
			#VC: clear link offsets
			_link.reset(viz.RESET_OPERATORS)
			
			#VC: reset orientation
			_link.preEuler([0, 0, 0], target=viz.LINK_ORI_OP, priority=-20)
			
			#VC: apply offsets
			_link.preTrans([0, 0, 0.05])
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTracker(_name).setParent(vizconnect.getGroup('origin_node_auto_calibration_cave'))

	#VC: set the name of the default
	vizconnect.setDefault('tracker', 'ppt_subitem1')

	#VC: return values can be modified here
	return None


#################################
# Input Code
#################################

def initInputs(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawInput = vizconnect.getRawInputDict()

	#VC: initialize a new input
	_name = 'spacenavigator'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			from vizconnect.util.input import spaceball_wrapper
			sensor = spaceball_wrapper.SpaceBallWrapper()
			rawInput[_name] = sensor
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='3dConnexion', model='SpaceNavigator')

	#VC: initialize a new input
	_name = 'keyboard'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			d = viz.add('directinput.dle')
			device = d.getKeyboardDevices()[index]
			rawInput[_name] = d.addKeyboard(device)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='Generic', model='Keyboard')

	#VC: initialize a new input
	_name = 'mouse_buttons'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			rawInput[_name] = viz.mouse
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='Generic', model='Mouse Buttons')

	#VC: initialize a new input
	_name = 'ppt_wand_2013'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			hostname = 'localhost'
			markerId = 3
			
			#VC: create the raw object
			from vizconnect.util.input import viz_wand_2013
			rawInput[_name] = viz_wand_2013.add(hostname=hostname, markerId=markerId)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='WorldViz', model='PPT Wand 2013')

	#VC: set the name of the default
	vizconnect.setDefault('input', 'spacenavigator')

	#VC: return values can be modified here
	return None


#################################
# Event Code
#################################

def initEvents(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawEvent = vizconnect.getRawEventDict()

	#VC: initialize a new event
	_name = 'VIZCONNECT_CYCLE_MAPPING_WINDOW'
	if vizconnect.isPendingInit('event', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			from vizconnect.util import events
			rawEvent[_name] = events.CustomEvent(viz.getEventID(_name))
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(event):
					if rawInput['keyboard'].isButtonDown(66):# make=Generic, model=Keyboard, name=keyboard, signal=Key F8
						event.sendOnce(e=viz.Event(mag=1))
				rawEvent[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addEvent(rawEvent[_name], _name, make='Vizconnect', model='Custom')

	#VC: initialize a new event
	_name = 'DRONE_RESTART_GAME'
	if vizconnect.isPendingInit('event', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			from vizconnect.util import events
			rawEvent[_name] = events.CustomEvent(viz.getEventID(_name))
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addEvent(rawEvent[_name], _name, make='Vizconnect', model='Custom')

	#VC: set the name of the default
	vizconnect.setDefault('event', 'VIZCONNECT_CYCLE_MAPPING_WINDOW')

	#VC: return values can be modified here
	return None


#################################
# Transport Code
#################################

def initTransports(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTransport = vizconnect.getRawTransportDict()

	#VC: initialize a new transport
	_name = 'walking'
	if vizconnect.isPendingInit('transport', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			height = 0
			acceleration = 2
			maxSpeed = 10
			rotationAcceleration = 90
			maxRotationSpeed = 20
			autoBreakingDragCoef = 1
			dragCoef = 0.1
			rotationAutoBreakingDragCoef = 0.2
			rotationDragCoef = 0.0001
			transportationGroup = None
			
			#VC: create the raw object
			from transportation import walking
			rawTransport[_name] = walking.Walking(	node=transportationGroup,
									height=height,
									acceleration=acceleration,
									maxSpeed=maxSpeed,
									rotationAcceleration=rotationAcceleration,
									maxRotationSpeed=maxRotationSpeed,
									autoBreakingDragCoef=autoBreakingDragCoef,
									dragCoef=dragCoef,
									rotationAutoBreakingDragCoef=rotationAutoBreakingDragCoef,
									rotationDragCoef=rotationDragCoef)
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(transport):
					if rawInput['keyboard'].isButtonDown(17):# make=Generic, model=Keyboard, name=keyboard, signal=Key W
						transport.moveForward(mag=1)
					if rawInput['spacenavigator'].getEuler()[1] > 0.03:# make=3dConnexion, model=SpaceNavigator, name=spacenavigator, signal=Pitch Down
						transport.moveForward(mag=1.0)
					if rawInput['ppt_wand_2013'].getJoystickPosition()[1] < -0.05:# make=WorldViz, model=PPT Wand 2013, name=ppt_wand_2013, signal=Analog Up
						transport.moveForward(mag=1.0)
					if rawInput['keyboard'].isButtonDown(31):# make=Generic, model=Keyboard, name=keyboard, signal=Key S
						transport.moveBackward(mag=1)
					if rawInput['spacenavigator'].getEuler()[1] < -0.03:# make=3dConnexion, model=SpaceNavigator, name=spacenavigator, signal=Pitch Up
						transport.moveBackward(mag=1.0)
					if rawInput['ppt_wand_2013'].getJoystickPosition()[1] > 0.05:# make=WorldViz, model=PPT Wand 2013, name=ppt_wand_2013, signal=Analog Down
						transport.moveBackward(mag=1.0)
					if rawInput['keyboard'].isButtonDown(30):# make=Generic, model=Keyboard, name=keyboard, signal=Key A
						transport.moveLeft(mag=1)
					if rawInput['spacenavigator'].getEuler()[2] > 0.03:# make=3dConnexion, model=SpaceNavigator, name=spacenavigator, signal=Roll Left
						transport.moveLeft(mag=1.0)
					if rawInput['ppt_wand_2013'].isButtonDown(3):# make=WorldViz, model=PPT Wand 2013, name=ppt_wand_2013, signal=Left Button
						transport.moveLeft(mag=1.0)
					if rawInput['keyboard'].isButtonDown(32):# make=Generic, model=Keyboard, name=keyboard, signal=Key D
						transport.moveRight(mag=1)
					if rawInput['spacenavigator'].getEuler()[2] < -0.03:# make=3dConnexion, model=SpaceNavigator, name=spacenavigator, signal=Roll Right
						transport.moveRight(mag=1.0)
					if rawInput['ppt_wand_2013'].isButtonDown(4):# make=WorldViz, model=PPT Wand 2013, name=ppt_wand_2013, signal=Right Button
						transport.moveRight(mag=1.0)
					if rawInput['spacenavigator'].getPosition()[1] > 0.03:# make=3dConnexion, model=SpaceNavigator, name=spacenavigator, signal=Slide Up
						transport.moveUp(mag=1.0)
					if rawInput['ppt_wand_2013'].isButtonDown(1):# make=WorldViz, model=PPT Wand 2013, name=ppt_wand_2013, signal=Top Button
						transport.moveUp(mag=1.0)
					if rawInput['spacenavigator'].getPosition()[1] < -0.03:# make=3dConnexion, model=SpaceNavigator, name=spacenavigator, signal=Slide Down
						transport.moveDown(mag=1.0)
					if rawInput['ppt_wand_2013'].isButtonDown(2):# make=WorldViz, model=PPT Wand 2013, name=ppt_wand_2013, signal=Bottom Button
						transport.moveDown(mag=1.0)
					if rawInput['spacenavigator'].getEuler()[0] < -0.03:# make=3dConnexion, model=SpaceNavigator, name=spacenavigator, signal=Turn Left
						transport.turnLeft(mag=1.0)
					if rawInput['ppt_wand_2013'].getJoystickPosition()[0] < -0.05:# make=WorldViz, model=PPT Wand 2013, name=ppt_wand_2013, signal=Analog Left
						transport.turnLeft(mag=1.0)
					if rawInput['spacenavigator'].getEuler()[0] > 0.03:# make=3dConnexion, model=SpaceNavigator, name=spacenavigator, signal=Turn Right
						transport.turnRight(mag=1.0)
					if rawInput['ppt_wand_2013'].getJoystickPosition()[0] > 0.05:# make=WorldViz, model=PPT Wand 2013, name=ppt_wand_2013, signal=Analog Right
						transport.turnRight(mag=1.0)
				rawTransport[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTransport(rawTransport[_name], _name, make='Virtual', model='Walking')

	#VC: set the name of the default
	vizconnect.setDefault('transport', 'walking')

	#VC: return values can be modified here
	return None


#################################
# Tool Code
#################################

def initTools(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTool = vizconnect.getRawToolDict()
	
	#VC: return values can be modified here
	return None


#################################
# Avatar Code
#################################

def initAvatars(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawAvatar = vizconnect.getRawAvatarDict()
	
	#VC: return values can be modified here
	return None


#################################
# Application Settings
#################################

def initSettings():
	#VC: apply general application settings
	viz.mouse.setTrap(False)
	viz.mouse.setVisible(viz.MOUSE_AUTO_HIDE)
	vizconnect.setMouseTrapToggleKey('')
	
	#VC: return values can be modified here
	return None


#################################
# Post-initialization Code
#################################

def postInit():
	"""Add any code here which should be called after all of the initialization of this configuration is complete.
	Returned values can be obtained by calling getPostInitResult for this file's vizconnect.Configuration instance."""
	
	viz.window.setFullscreen(True)
	
	return None


#################################
# Stand alone configuration
#################################

def initInterface():
	#VC: start the interface
	vizconnect.interface.go(__file__,
							live=True,
							openBrowserWindow=True,
							startingInterface=vizconnect.interface.INTERFACE_STARTUP)

	#VC: return values can be modified here
	return None


###############################################

if __name__ == "__main__":
	initInterface()
	viz.add('piazza.osgb')
#	viz.add('piazza_animations.osgb')

