import pandas as pd
import csv

class Lector:
	"""
	This class allow us to read a csv file to get the data, diferenciate and segregate
	between each cell
	"""
	def __init__(self, file_path):
		self.file_path=file_path

	def read(self):
		#file=open(self.file_path)
		#csvreader=csv.reader(file)
		self.file=pd.read_csv(self.file_path, sep='|', usecols=['ID_DISTRITO_LOCAL',
			'TOTAL_PERSONAS_VOTARON', 'PAN', 'PRD','CXQROO','C_PAN_PRD_CQROO','C_PAN_PRD', 'C_PAN_CQROO'])
		#print(self.file['ID_DISTRITO_LOCAL'][0].strip("="))
		#for x in self.file['ID_DISTRITO_LOCAL']:
		#	print(x.strip("=\"").lstrip("\""))
	def segregate_VOTES(self):
		distrito_x_partido={}
		political_parties_list=[]
		for x in range(1, len(self.file['ID_DISTRITO_LOCAL'])-1):
			dist=int(self.file['ID_DISTRITO_LOCAL'][x].strip("=\"").lstrip("\""))
			if distrito_x_partido.get(dist)==None:#print(dist)
				pan=0
				for i in range(1,len(self.file['PAN'])-1):
					if int(self.file['ID_DISTRITO_LOCAL'][i].strip("=\"").lstrip("\""))==dist:
						pan+=self.file['PAN'][i]
					else:
						break
				print(pan)
				political_parties_list.append(('PAN',pan))

				prd=0
				for i in range(1, len(self.file['PRD'])-1):
					if self.file['ID_DISTRITO_LOCAL'][i]==dist:
						prd+=self.file['PRD'][i]
					else:
						break

				political_parties_list.append(('PRD',prd))
				cxqroo=0
				for i in range(1, len(self.file['PRD'])-1):
					if self.file['ID_DISTRITO_LOCAL'][i]==dist:
						cxqroo+=self.file['CXQROO'][i]
					else:
						break
				political_parties_list.append(('CXQROO',cxqroo))

			#political_parties_list=[('PAN',pan),('PRD',prd), ('CXQROO',cxqroo)]
			distrito_x_partido[dist]=Distrito(dist,political_parties_list)
		return distrito_x_partido

	def segregate_COALICION_VOTES(self):
		distrito_x_coalicion={}
		political_parties_list=[]
		for x in range(1, len(self.file['ID_DISTRITO_LOCAL'])-1):
			dist=int(self.file['ID_DISTRITO_LOCAL'][x].strip("=\"").lstrip("\""))
			if distrito_x_coalicion.get(dist)==None:#print(dist)
				c_pan_prd_cqroo=0
				for i in range(1,len(self.file['C_PAN_PRD_CQROO'])-1):
					if self.file['ID_DISTRITO_LOCAL'][i]==dist:
						c_pan_prd_cqroo+=self.file['C_PAN_PRD_CQROO'][i]
					else:
						break
				political_parties_list.append(('C_PAN_PRD_CQROO',c_pan_prd_cqroo))

				c_pan_prd=0
				for i in range(1, len(self.file['C_PAN_PRD'])-1):
					if self.file['ID_DISTRITO_LOCAL'][i]==dist:
						c_pan_prd+=self.file['C_PAN_PRD'][i]
					else:
						break
				political_parties_list.append(('C_PAN_PRD',c_pan_prd))
				c_pan_cxqroo=0
				for i in range(1, len(self.file['C_PAN_CQROO'])-1):
					if self.file['ID_DISTRITO_LOCAL'][i]==dist:
						c_pan_cxqroo+=self.file['C_PAN_CQROO'][i]
					else:
						break

				political_parties_list.append(('C_PAN_CQROO',c_pan_cxqroo))

				distrito_x_coalicion[dist]=Distrito(dist,political_parties_list)
		return distrito_x_coalicion

class Distrito:
	"""
	It allow us to model a district and its correpondent political parties
	"""

	def __init__(self, district_number,political_parties_list):
		"""
		PARAMS:
			partidos_politicos_list: list contains a tuple of political party 
			and vote
		"""
		self.district_number=district_number
		self.political_parties_list=political_parties_list
		#self.coaliciones=coaliciones


	def __str__(self):
		"""
		Returns the distric number, and each tuple of political_parties and coaliciones
		"""
		out="DISTRITO: "+str(self.district_number)+"{"
		for PP,votes in self.political_parties_list:
			out+= PP+" : " +str(votes)+", "
		out+="}"
		return out

l=Lector("QROO_DIP_2022.csv")
l.read()
partido_c=l.segregate_VOTES()
partido_p=l.segregate_COALICION_VOTES()
"""
for x in partido_p:
	print(partido_p[x])
print("===========================")
for x in partido_c:
	print(x)
"""