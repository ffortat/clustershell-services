from Tkinter import *
import sys

class ServicesFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
		self.frame = frame = Frame(goshujinsama)

		self.services = serviceslist = Listbox(frame, height=10, width=15)
		self.nodes = nodeslist = Listbox(frame)

		nodelabel = Label(frame, text="Nodes :")
		editbutton = Button(frame, text="Edit")
		startbutton = Button(frame, text="Start")
		stopbutton = Button(frame, text="Stop")
		restartbutton = Button(frame, text="Restart")
		statusbutton = Button(frame, text="Statut")

		serviceslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		nodelabel.grid(row=0, column=1, sticky=W)
		nodeslist.grid(row=1, column=1, columnspan=4,sticky=W+N+S+E)
		editbutton.grid(row=4, column=0, sticky=W+E)
		startbutton.grid(row=4, column=1, sticky=W)
		stopbutton.grid(row=4, column=2, sticky=W)
		restartbutton.grid(row=4, column=3, sticky=W)
		statusbutton.grid(row=4, column=4, sticky=W)

		editbutton['command'] = application.switchtoservicesedit

		self.loadservices()

		self.services.bind('<ButtonRelease-1>', self.selectservice)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()

	def loadservices(self) :
		for service in self.application.config['services'] :
			self.services.insert(END, service)

	def loadnodes(self, service) :
		while self.nodes.get(0) :
			self.nodes.delete(0)
		for node in self.application.config['services'][service]['nodes'] :
			self.nodes.insert(END, node)

	def selectservice(self, event) :
		service = self.services.get(self.services.curselection()[0])
		self.loadnodes(service)