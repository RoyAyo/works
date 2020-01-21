import numpy as np

class Program():
	#standards for all outputs
	self.standard_ph_max = 8.5
	self.standard_ph_min = 6.5
	self.standard_turbidity_max = 3.5  #NTU 
	self.standard_turbidity_min = 3.0  #Ntu

	def __init__(flow_rate,turbidity,pH):
		self.flow_rate = flow_rate   #L/hr
		self.turbidity = turbidity 	#NTU
		self.pH = pH
		#we are using a continuous system so this ensures the program never stops running
		while True:
			workflow()

	def workflow():
		while True:
			(self.new_turbidity,self.new_pH) = chemical_tank(self.turbidity,self.pH)
			for i in range(0,3):
				if i < 2:
					(self.new_turbidity,self.new_pH) = cells(self.turbidity,self.pH)
				else:
					(self.new_turbidity,self.new_pH) = cells(self.turbidity,self.pH)
					self.new_turbidity = turbidity_meter()
					if ((self.new_turbidity >= self.standard_turbidity_min) and (self.new_turbidity <= self.standard_turbidity_max)):
						pass
					else:
						continue
					self.new_pH = pH_meter()
					if ((self.new_pH >= self.standard_ph_min) and (self.new_pH <= self.standard_ph_max)):
						break
					else:
						chlorinate(self.new_pH)
						continue
		return True

	def chemical_tank(turbidity,pH):
		self.chlorine = 0.02 #g/l 
		self.soda_ash = 0.089 #g/l
		self.chemical_tank_vol = 5000 #L

		#chlorine and soda ash is added to sample
		#returns unknown new values
		return (new_turbidity,new_pH)


	def cells(turbidity,pH):
		self.cell_volume = 60000 #in L
		self.cell_pressure = 5 #in bar

		#the cell takes in the inlet sample and returns new unknown turbidity and pH until the 3rd cell
		
		return (new_turbidity,new_pH)


	def turbidity_meter():
		return turbidity

	def pH_meter():
		return pH


	def chlorinate(pH):
		if pH < self.standard_ph_min:
			self.chlorine -= 0.2(self.chlorine)
		else:
			self.chlorine += 0.2(self.chlorine)

		return True

#initial influent
water = Program(3000,0.5,4.25)