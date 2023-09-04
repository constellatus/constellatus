import os
import logging
import eons

class TEST_EXECUTOR(eons.Executor):

	def __init__(this):

		super().__init__(name="test executor", descriptionStr="TESTING ONLY")

	#Override of eons.Executor method. See that class for details
	def Configure(this):
		super().Configure()

		# this.logLevel = logging.getLogger().level

	# Disable the registry, so we're forced to use Constellatus.
	def RegisterAllClasses(this):
		pass

	#Override of eons.Executor method. See that class for details
	def Function(this):
		logging.getLogger().setLevel(logging.CRITICAL)

		super().Function()

		this.repo.online = False
		this.repo.registry = None
		this.repo.store = None
		this.observatory.online = True
		this.observatory.url = "http://localhost:1137"

		hello = this.GetRegistered("hello_world", "functor")
		hello.feature.autoReturn = False
		hello(executor=this)

	def PostCall(this):
		# logging.getLogger().setLevel(this.logLevel)
		pass

