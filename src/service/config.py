import json
from ClusterShell.Task import NodeSet

config = {
	"services" : {}
}

def fetchNodes(service) :
	global config

	nodes = []

	if config['services'].has_key(service) :
		for dependency in config['services'][service]['dependencies'] :
			nodes.extend(fetchNodes(dependency))
		nodes.append((service, config['services'][service]['daemon'], NodeSet.fromlist(map(unicode.encode, config['services'][service]['nodes']))))
	elif config['groups'].has_key(service) :
		for subservice in config['groups'][service]:
			nodes.extend(fetchNodes(subservice))

	return nodes


def checkAction(service, action) :
	global config

	if config['services'].has_key(service) :
		return (action in config['services'][service]['actions'])

	return True


def listActions(service) :
	global config

	actions = ''

	if config['services'].has_key(service) :
		actions = '{' + '|'.join(config['services'][service]['actions']) + '}'

	return actions


def load(filename = 'cs-services.json') :
	global config
	configfd = open(filename, 'r')

	config = json.load(configfd)

	configfd.close()
