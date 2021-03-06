# BUGS =====


# TODO LIST =====

# options: reset pwd, logout
# mainmenu: multiplayer -> local, online
# online: login, register -> host (room), join
# trail effect with glow for weapons
# optimize rear camera
# use a ghost on the car (bigger than the car) for the AI
# https://github.com/cflavio/yorg/issues/23
# fixes for 1.10


# WAITING =====

# (Panda3D 1.10) joypad
# (Panda3D 1.10) remove thirdparty libraries (manage them with deploy-ng)
# (Panda3D 1.10) deployng: use logging for logging
# (Panda3D 1.10) port to python 3
# (Panda3D 1.10) fix curr_ver == 'deploy-ng' in engine.logic
# https://github.com/cflavio/yorg/issues/22
# hardware instancing (gl_InstanceID requires 1.40)


# MAYBE/SOMEDAY =====

# make scons for yyagl
# make a submodule for racing - yyarl
# refactor: use only eng.client (remove eng.server and yorg_client)
# refactor: don't share eng with every colleague, instead share only the
#   useful components e.g. PhysComponent has PhysComponent.phys_mgr and
#   PhysComponent.log_mgr
# refactor: remove mediator from colleague
# refactor: where proper (i.e. where observers aren't tied to the observable)
#   replace observer with publisher-subscriber
# refactor: attach/attach_obs, detach/detach_obs
# refactor: Facade.__init__(self, mth_lst, prop_lst), internally it invokes
#   the methods _fwd_mth, _fwd_prop
# drifting force function of linear and angular velocities
# uml create automatic class diagrams with fields and methods for each class
# unit tests
# fix shaders
# embed into a wx / pyqt window
# do automatic update (assets shared among platforms)
# add friendship
# django webapp for scores
