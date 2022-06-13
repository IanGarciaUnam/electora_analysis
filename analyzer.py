import pandas as pd


class Lector:
	"""
	This class allow us to read a csv file to get the data, diferenciate and segregate
	between each cell
	"""
	def __init__(self, file_path):
		self.file_path=file_path

	def read():
		file=pd.read_csv(self.file_path)
		print(file.to_string())

class Distrito:
	"""
	It allow us to model a district and its correpondent political parties
	"""

	def __init__(self, district_number,political_parties_list,coaliciones):
		"""
		PARAMS:
			partidos_politicos_list: list contains a tuple of political party 
			and vote
		"""
		self.district_number=district_number
		self.political_parties_list=political_parties_list
		self.coaliciones=coaliciones


	def __str__():
		"""
		Returns the distric number, and each tuple of political_parties and coaliciones
		"""
		out="DISTRITO: "+str(self.district_number)+"{"
		for PP,votes in self.political_parties_list:
			out+= PP+" : " +str(votes)+", "
		out+="} -\n Coaliciones {"
		for PP,votes in self.coaliciones:
			out+=PP+" : "+str(votes)
		out+="}"

l=Lector("QROO_DIP_2022.csv")
l.read()