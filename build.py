from pybuilder.core import use_plugin, init, task

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.flake8")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

@init
def set_properties(project):
	project.version = "9.9.9.9"
	project.set_property('unittest_module_glob', '*_prueba')
	project.set_property('coverage_threshold_warn', 80)
	project.set_property('coverage_break_build', True)
	project.set_property('flake8_break_build', True)
	

default_task = ['clean', 'analyze', 'publish']
